# [`holospy.reconstruct`](#module-holospy.reconstruct)

<!-- !! processed by numpydoc !! -->

### holospy.reconstruct.aperture_function(r, apradius, rsmooth)

A smooth aperture function that decays from apradius-rsmooth to apradius+rsmooth.

* **Parameters:**
  **r**
  ```rst
  ndarray
  ```

  : Array of input data (e.g. frequencies)

  **apradius**
  ```rst
  python:float
  ```

  : Radius (center) of the smooth aperture. Decay starts at apradius - rsmooth.

  **rsmooth**
  ```rst
  python:float
  ```

  : Smoothness in halfwidth. rsmooth = 1 will cause a decay from 1 to 0 over 2 pixel.
* **Returns:**
  [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)

<!-- !! processed by numpydoc !! -->

### holospy.reconstruct.estimate_sideband_position(data, sampling, central_band_mask_radius=None, sb='lower', high_cf=True)

Finds the position of the sideband and returns its position.

* **Parameters:**
  **data**
  ```rst
  numpy.ndarray
  ```

  : The data of the hologram.

  **sampling**
  ```rst
  python:tuple
  ```

  : The sampling rate in both image directions.

  **central_band_mask_radius**
  ```rst
  python:float, optional
  ```

  : The aperture radius used to mask out the centerband.

  **sb**
  ```rst
  python:str, optional
  ```

  : Chooses which sideband is taken. ‘lower’, ‘upper’, ‘left’, or ‘right’.

  **high_cf**
  ```rst
  bool, optional
  ```

  : If False, the highest carrier frequency allowed for the sideband location is equal to
    half of the Nyquist frequency (Default: True).
* **Returns:**
  [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple)
  : The sideband position (y, x), referred to the unshifted FFT.

<!-- !! processed by numpydoc !! -->

### holospy.reconstruct.estimate_sideband_size(sb_position, shape, sb_size_ratio=0.5)

Estimates the size of sideband filter

* **Parameters:**
  **shape**
  ```rst
  numpy:array_like
  ```

  : Holographic data array

  **sb_position**
  ```rst
  python:tuple
  ```

  : The sideband position (y, x), referred to the non-shifted FFT.

  **sb_size_ratio**
  ```rst
  python:float, optional
  ```

  : Size of sideband as a fraction of the distance to central band
* **Returns:**
  [`float`](https://docs.python.org/3/builtins/functions.html#float)
  : Size of sideband filter

<!-- !! processed by numpydoc !! -->

### holospy.reconstruct.freq_array(shape, sampling)

Makes up a frequency array.

* **Parameters:**
  **shape**
  ```rst
  python:tuple
  ```

  : The shape of the array.

  **sampling**
  ```rst
  python:tuple
  ```

  : The sampling rates of the array.
* **Returns:**
  [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
  : Frequencies

<!-- !! processed by numpydoc !! -->

### holospy.reconstruct.reconstruct(data, sampling, sb_size, sb_position, sb_smoothness, output_shape=None, plotting=False)

Core function for holographic reconstruction.

* **Parameters:**
  **data**
  ```rst
  numpy:array_like
  ```

  : Holographic data array

  **sampling**
  ```rst
  python:tuple
  ```

  : Sampling rate of the hologram in y and x direction.

  **sb_size**
  ```rst
  python:float
  ```

  : Size of the sideband filter in pixel.

  **sb_position**
  ```rst
  python:tuple
  ```

  : Sideband position in pixel.

  **sb_smoothness**
  ```rst
  python:float
  ```

  : Smoothness of the aperture in pixel.

  **output_shape**
  ```rst
  python:tuple, optional
  ```

  : New output shape.

  **plotting**
  ```rst
  bool
  ```

  : Plots the masked sideband used for reconstruction.
* **Returns:**
  [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
  : Reconstructed electron wave

<!-- !! processed by numpydoc !! -->
