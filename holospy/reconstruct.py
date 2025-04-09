# -*- coding: utf-8 -*-
# Copyright 2007-2025 The HyperSpy developers
#
# This file is part of HyperSpy.
#
# HyperSpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HyperSpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HyperSpy. If not, see <https://www.gnu.org/licenses/#GPL>.

import logging

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft2, fftshift, ifft2

_logger = logging.getLogger(__name__)


def estimate_sideband_position(
    data, sampling, central_band_mask_radius=None, sb="lower", high_cf=True
):
    """
    Finds the position of the sideband and returns its position.

    Parameters
    ----------
    data : numpy.ndarray
        The data of the hologram.
    sampling : tuple
        The sampling rate in both image directions.
    central_band_mask_radius : float, optional
        The aperture radius used to mask out the centerband.
    sb : str, optional
        Chooses which sideband is taken. 'lower', 'upper', 'left', or 'right'.
    high_cf : bool, optional
        If False, the highest carrier frequency allowed for the sideband location is equal to
        half of the Nyquist frequency (Default: True).

    Returns
    -------
    tuple
        The sideband position (y, x), referred to the unshifted FFT.
    """
    sb_position = (0, 0)
    f_freq = freq_array(data.shape, sampling)
    # If aperture radius of centerband is not given, it will be set to 5 % of
    # the Nyquist frequ.:
    if central_band_mask_radius is None:
        central_band_mask_radius = 0.05 * np.max(f_freq)
    # A small aperture masking out the centerband.
    ap_cb = 1.0 - aperture_function(f_freq, central_band_mask_radius, 1e-6)
    if not high_cf:  # Cut out higher frequencies, if necessary:
        ap_cb *= aperture_function(f_freq, np.max(f_freq) / (2 * np.sqrt(2)), 1e-6)
    # Imitates 0:
    fft_holo = fft2(data) / np.prod(data.shape)
    fft_filtered = fft_holo * ap_cb
    # Sideband position in pixels referred to unshifted FFT
    cb_position = (
        fft_filtered.shape[0] // 2,
        fft_filtered.shape[1] // 2,
    )  # cb: center band
    if sb == "lower":
        fft_sb = abs(fft_filtered[: cb_position[0], :])
        sb_position = np.asarray(np.unravel_index(fft_sb.argmax(), fft_sb.shape))
    elif sb == "upper":
        fft_sb = abs(fft_filtered[cb_position[0] :, :])
        sb_position = np.unravel_index(fft_sb.argmax(), fft_sb.shape)
        sb_position = np.asarray(np.add(sb_position, (cb_position[0], 0)))
    elif sb == "left":
        fft_sb = abs(fft_filtered[:, : cb_position[1]])
        sb_position = np.asarray(np.unravel_index(fft_sb.argmax(), fft_sb.shape))
    elif sb == "right":
        fft_sb = abs(fft_filtered[:, cb_position[1] :])
        sb_position = np.unravel_index(fft_sb.argmax(), fft_sb.shape)
        sb_position = np.asarray(np.add(sb_position, (0, cb_position[1])))
    # Return sideband position:
    return sb_position


def estimate_sideband_size(sb_position, shape, sb_size_ratio=0.5):
    """
    Estimates the size of sideband filter

    Parameters
    ----------
    shape : array_like
            Holographic data array
    sb_position : tuple
        The sideband position (y, x), referred to the non-shifted FFT.
    sb_size_ratio : float, optional
        Size of sideband as a fraction of the distance to central band

    Returns
    -------
    float
        Size of sideband filter

    """

    h = (
        np.array(
            (
                np.asarray(sb_position) - np.asarray([0, 0]),
                np.asarray(sb_position) - np.asarray([0, shape[1]]),
                np.asarray(sb_position) - np.asarray([shape[0], 0]),
                np.asarray(sb_position) - np.asarray(shape),
            )
        )
        * sb_size_ratio
    )
    return np.min(np.linalg.norm(h, axis=1))


def reconstruct(
    data,
    sampling,
    sb_size,
    sb_position,
    sb_smoothness,
    output_shape=None,
    plotting=False,
):
    """Core function for holographic reconstruction.

    Parameters
    ----------
    data : array_like
        Holographic data array
    sampling : tuple
        Sampling rate of the hologram in y and x direction.
    sb_size : float
        Size of the sideband filter in pixel.
    sb_position : tuple
        Sideband position in pixel.
    sb_smoothness : float
        Smoothness of the aperture in pixel.
    output_shape : tuple, optional
        New output shape.
    plotting : bool
        Plots the masked sideband used for reconstruction.

    Returns
    -------
    numpy.ndarray
        Reconstructed electron wave

    """

    holo_size = data.shape
    f_sampling = np.divide(1, [a * b for a, b in zip(holo_size, sampling)])

    fft_exp = fft2(data) / np.prod(holo_size)

    f_freq = freq_array(data.shape, sampling)

    sb_size *= np.mean(f_sampling)
    sb_smoothness *= np.mean(f_sampling)
    aperture = aperture_function(f_freq, sb_size, sb_smoothness)

    fft_shifted = np.roll(fft_exp, sb_position[0], axis=0)
    fft_shifted = np.roll(fft_shifted, sb_position[1], axis=1)

    fft_aperture = fft_shifted * aperture

    if plotting:
        _, axs = plt.subplots(1, 1, figsize=(4, 4))
        axs.imshow(abs(fftshift(fft_aperture)), clim=(0, 0.1))
        axs.scatter(sb_position[1], sb_position[0], s=10, color="red", marker="x")
        axs.set_xlim(
            int(holo_size[0] / 2) - sb_size / np.mean(f_sampling),
            int(holo_size[0] / 2) + sb_size / np.mean(f_sampling),
        )
        axs.set_ylim(
            int(holo_size[1] / 2) - sb_size / np.mean(f_sampling),
            int(holo_size[1] / 2) + sb_size / np.mean(f_sampling),
        )

    if output_shape is not None:
        y_min = int(holo_size[0] / 2 - output_shape[0] / 2)
        y_max = int(holo_size[0] / 2 + output_shape[0] / 2)
        x_min = int(holo_size[1] / 2 - output_shape[1] / 2)
        x_max = int(holo_size[1] / 2 + output_shape[1] / 2)

        fft_aperture = fftshift(fftshift(fft_aperture)[y_min:y_max, x_min:x_max])

    wav = ifft2(fft_aperture) * np.prod(data.shape)

    return wav


def aperture_function(r, apradius, rsmooth):
    """
    A smooth aperture function that decays from apradius-rsmooth to apradius+rsmooth.

    Parameters
    ----------
    r : ndarray
        Array of input data (e.g. frequencies)
    apradius : float
        Radius (center) of the smooth aperture. Decay starts at apradius - rsmooth.
    rsmooth : float
        Smoothness in halfwidth. rsmooth = 1 will cause a decay from 1 to 0 over 2 pixel.

    Returns
    -------
    numpy.ndarray
    """

    return 0.5 * (1.0 - np.tanh((abs(r) - apradius) / (0.5 * rsmooth)))


def freq_array(shape, sampling):
    """
    Makes up a frequency array.

    Parameters
    ----------
    shape : tuple
        The shape of the array.
    sampling : tuple
        The sampling rates of the array.

    Returns
    -------
    numpy.ndarray
        Frequencies
    """
    f_freq_1d_y = np.fft.fftfreq(shape[0], sampling[0])
    f_freq_1d_x = np.fft.fftfreq(shape[1], sampling[1])
    f_freq_mesh = np.meshgrid(f_freq_1d_x, f_freq_1d_y)
    f_freq = np.hypot(f_freq_mesh[0], f_freq_mesh[1])

    return f_freq
