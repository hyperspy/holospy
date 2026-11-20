# [`holospy.tools`](#module-holospy.tools)

<!-- !! processed by numpydoc !! -->

### holospy.tools.calculate_carrier_frequency(data, sb_position, scale)

Calculates fringe carrier frequency of a hologram

* **Parameters:**
  **data**
  : The data of the hologram.

  **sb_position**
  : Position of the sideband with the reference to non-shifted FFT

  **scale**
  : Scale of the axes that will be used for the calculation.
* **Returns:**
  [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
  : Carrier frequency

<!-- !! processed by numpydoc !! -->

### holospy.tools.estimate_fringe_contrast_fourier(data, sb_position, apodization='hanning')

Estimates average fringe contrast of a hologram  by dividing amplitude
of maximum pixel of sideband by amplitude of FFT’s origin.

* **Parameters:**
  **data**
  : The data of the hologram.

  **sb_position**
  : Position of the sideband with the reference to non-shifted FFT

  **apodization**
  : Use ‘hanning’, ‘hamming’ or None to apply apodization window in real space before FFT
    Apodization is typically needed to suppress the striking  due to sharp edges
    of the which often results in underestimation of the fringe contrast. (Default: ‘hanning’)
* **Returns:**
  [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
  : Fringe contrast as a float

<!-- !! processed by numpydoc !! -->
