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

import warnings
from pathlib import Path

import hyperspy.api as hs

__all__ = [
    "Fe_needle_hologram",
    "Fe_needle_reference_hologram",
]


def __dir__():
    return sorted(__all__)


def _resolve_dir():
    """Returns the absolute path to this file's directory."""
    return Path(__file__).resolve().parent


def Fe_needle_hologram():
    """
    Load an object hologram image.

    Notes
    -----
    Sample: Fe needle with YOx nanoparticle inclusions. See reference for more
    details

        Migunov, V. et al. Model-independent measurement of the charge density
        distribution along an Fe atom probe needle using off-axis electron
        holography without mean inner potential effects. J. Appl. Phys. 117,
        134301 (2015). https://doi.org/10.1063/1.4916609

    TEM: FEI Titan G2 60-300 HOLO

        Boothroyd, C. et al. FEI Titan G2 60-300 HOLO. Journal of large-scale
        research facilities JLSRF 2, 44 (2016).
        https://doi.org/10.17815/jlsrf-2-70

    Signal is loaded "read-only" to ensure data access regardless of
    install location
    """

    file_path = _resolve_dir().joinpath("01_holo_Vbp_130V_0V_bin2_crop.hdf5")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        return hs.load(file_path, mode="r", reader="hspy")


def Fe_needle_reference_hologram():
    """
    Load a reference hologram image.

    Notes
    -----
    Sample: Fe needle with YOx nanoparticle inclusions. See reference for more
    details

        Migunov, V. et al. Model-independent measurement of the charge density
        distribution along an Fe atom probe needle using off-axis electron
        holography without mean inner potential effects. J. Appl. Phys. 117,
        134301 (2015). https://doi.org/10.1063/1.4916609

    TEM: FEI Titan G2 60-300 HOLO

        Boothroyd, C. et al. FEI Titan G2 60-300 HOLO. Journal of large-scale
        research facilities JLSRF 2, 44 (2016).
        https://doi.org/10.17815/jlsrf-2-70

    Signal is loaded "read-only" to ensure data access regardless of
    install location
    """

    file_path = _resolve_dir().joinpath("00_ref_Vbp_130V_0V_bin2_crop.hdf5")

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        return hs.load(file_path, mode="r", reader="hspy")
