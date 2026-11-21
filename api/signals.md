# [`holospy.signals`](#module-holospy.signals)

| [`HologramImage`](#holospy.signals.HologramImage)(\*args, \*\*kwargs)     | Signal class for holograms acquired via off-axis electron holography.      |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [`LazyHologramImage`](#holospy.signals.LazyHologramImage)(\*args, \*\*kwargs) | Lazy signal class for holograms acquired via off-axis electron holography. |

<a id="module-holospy.signals"></a>

Modules containing the HoloSpy signals and their lazy counterparts.

HologramImage
: For holography data

LazyHologramImage
: For holography data processed lazily

<!-- !! processed by numpydoc !! -->

### *class* holospy.signals.HologramImage(\*args, \*\*kwargs)

Bases: [`Signal2D`](https://hyperspy.org/hyperspy-doc/current/reference/api.signals/Signal2D.html#hyperspy.api.signals.Signal2D)

Signal class for holograms acquired via off-axis electron holography.

<!-- !! processed by numpydoc !! -->

Create a signal instance.

* **Parameters:**
  **data**
  ```rst
  numpy.ndarray
  ```

  : The signal data. It can be an array of any dimensions.

  **axes**
  ```rst
  [dict/axes], optional
  ```

  : List of either dictionaries or axes objects to define the axes (see
    the documentation of the [`AxesManager`](https://hyperspy.org/hyperspy-doc/current/reference/base_classes/axes.html#hyperspy.axes.AxesManager)
    class for more details).

  **attributes**
  ```rst
  python:dict, optional
  ```

  : A dictionary whose items are stored as attributes.

  **metadata**
  ```rst
  python:dict, optional
  ```

  : A dictionary containing a set of parameters
    that will to stores in the `metadata` attribute.
    Some parameters might be mandatory in some cases.

  **original_metadata**
  ```rst
  python:dict, optional
  ```

  : A dictionary containing a set of parameters
    that will to stores in the `original_metadata` attribute. It
    typically contains all the parameters that has been
    imported from the original data file.

  **ragged**
  ```rst
  bool or python:None, optional
  ```

  : Define whether the signal is ragged or not. Overwrite the
    `ragged` value in the `attributes` dictionary. If None, it does
    nothing. Default is None.

<!-- !! processed by numpydoc !! -->

#### estimate_sideband_position(ap_cb_radius=None, sb='lower', high_cf=True, show_progressbar=False, num_workers=None)

Estimates the position of the sideband and returns its position.

* **Parameters:**
  **ap_cb_radius**
  ```rst
  python:float, python:None
  ```

  : The aperture radius used to mask out the centerband.

  **sb**
  ```rst
  python:str, optional
  ```

  : Chooses which sideband is taken. `'lower'` or `'upper'`

  **high_cf**
  ```rst
  bool, optional
  ```

  : If False, the highest carrier frequency allowed for the sideband location is equal to
    half of the Nyquist frequency (Default: True).

  **show_progressbar**
  ```rst
  python:None or bool
  ```

  : If `True`, display a progress bar. If `None`, the default from
    the preferences settings is used.

  **num_workers**
  ```rst
  python:None or python:int
  ```

  : Number of worker used by dask. If None, default
    to dask default value.
* **Returns:**
  [`hyperspy.api.signals.Signal1D`](https://hyperspy.org/hyperspy-doc/current/reference/api.signals/Signal1D.html#hyperspy.api.signals.Signal1D)
  : Sideband positions (y, x), referred to the unshifted FFT.
* **Raises:**
  [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError)
  : If the signal axes are non-uniform axes.

### Examples

```pycon
>>> import holospy as holo
>>> s = holo.data.Fe_needle_hologram()
>>> sb_position = s.estimate_sideband_position()
>>> sb_position.data
```

array([124, 452])

<!-- !! processed by numpydoc !! -->

#### estimate_sideband_size(sb_position, show_progressbar=False, num_workers=None)

Estimates the size of the sideband and returns its size.

* **Parameters:**
  **sb_position**
  ```rst
  hyperspy.api.signals.BaseSignal
  ```

  : The sideband position (y, x), referred to the non-shifted FFT.

  **show_progressbar**
  ```rst
  python:None or bool
  ```

  : If `True`, display a progress bar. If `None`, the default from
    the preferences settings is used.

  **num_workers**
  ```rst
  python:None or python:int
  ```

  : Number of worker used by dask. If None, default
    to dask default value.
* **Returns:**
  [`hyperspy.api.signals.Signal1D`](https://hyperspy.org/hyperspy-doc/current/reference/api.signals/Signal1D.html#hyperspy.api.signals.Signal1D)
  : Sideband size referred to the unshifted FFT.
* **Raises:**
  [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError)
  : If the signal axes are non-uniform axes.

### Examples

```pycon
>>> import holospy as holo
>>> s = holo.data.Fe_needle_hologram()
>>> sb_position = s.estimate_sideband_position()
>>> sb_size = s.estimate_sideband_size(sb_position)
>>> sb_size.data
array([ 68.87670143])
```

<!-- !! processed by numpydoc !! -->

#### reconstruct_phase(reference=None, sb_size=None, sb_smoothness=None, sb_unit=None, sb='lower', sb_position=None, high_cf=True, output_shape=None, plotting=False, store_parameters=True, show_progressbar=False, num_workers=None)

Reconstruct electron holograms. Operates on multidimensional
hyperspy signals. There are several usage schemes:

* Reconstruct 1d or Nd hologram without reference
* Reconstruct 1d or Nd hologram using single reference hologram
* Reconstruct Nd hologram using Nd reference hologram (applies each
  reference to each hologram in Nd stack)

The reconstruction parameters (sb_position, sb_size, sb_smoothness)
have to be 1d or to have same dimensionality as the hologram.

* **Parameters:**
  **reference**
  ```rst
  ndarray, hyperspy.api.signals.Signal2D, python:None
  ```

  : Vacuum reference hologram.

  **sb_size**
  ```rst
  python:float, ndarray, hyperspy.api.signals.BaseSignal, python:None
  ```

  : Sideband radius of the aperture in corresponding unit (see
    ‘sb_unit’). If None, the radius of the aperture is set to 1/3 of
    the distance between sideband and center band.

  **sb_smoothness**
  ```rst
  python:float, ndarray, hyperspy.api.signals.BaseSignal, python:None
  ```

  : Smoothness of the aperture in the same unit as sb_size.

  **sb_unit**
  ```rst
  python:str, python:None
  ```

  : Unit of the two sideband parameters ‘sb_size’ and ‘sb_smoothness’.
    Default: None - Sideband size given in pixels
    ‘nm’: Size and smoothness of the aperture are given in 1/nm.
    ‘mrad’: Size and smoothness of the aperture are given in mrad.

  **sb**
  ```rst
  python:str, python:None
  ```

  : Select which sideband is selected. ‘upper’ or ‘lower’.

  **sb_position**
  ```rst
  python:tuple, hyperspy.api.signals.Signal1D, python:None
  ```

  : The sideband position (y, x), referred to the non-shifted FFT. If
    None, sideband is determined automatically from FFT.

  **high_cf**
  ```rst
  bool, optional
  ```

  : If False, the highest carrier frequency allowed for the sideband
    location is equal to half of the Nyquist frequency (Default: True).

  **output_shape: tuple, None**
  : Choose a new output shape. Default is the shape of the input
    hologram. The output shape should not be larger than the input
    shape.

  **plotting**
  ```rst
  bool
  ```

  : Shows details of the reconstruction (i.e. SB selection).

  **store_parameters**
  ```rst
  bool
  ```

  : Store reconstruction parameters in metadata

  **show_progressbar**
  ```rst
  python:None or bool
  ```

  : If `True`, display a progress bar. If `None`, the default from
    the preferences settings is used.

  **num_workers**
  ```rst
  python:None or python:int
  ```

  : Number of worker used by dask. If None, default
    to dask default value.
* **Returns:**
  [`hyperspy.api.signals.ComplexSignal2D`](https://hyperspy.org/hyperspy-doc/current/reference/api.signals/ComplexSignal2D.html#hyperspy.api.signals.ComplexSignal2D)
  : Reconstructed electron wave. By default object wave is divided by
    reference wave.
* **Raises:**
  [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError)
  : If the signal axes are non-uniform axes.

### Examples

```pycon
>>> import holospy as holo
>>> s = holo.data.Fe_needle_hologram()
>>> sb_position = s.estimate_sideband_position()
>>> sb_size = s.estimate_sideband_size(sb_position)
>>> wave = s.reconstruct_phase(sb_position=sb_position, sb_size=sb_size)
```

<!-- !! processed by numpydoc !! -->

#### set_microscope_parameters(beam_energy=None, biprism_voltage=None, tilt_stage=None)

Set the microscope parameters.

If no arguments are given, raises an interactive mode to fill
the values.

* **Parameters:**
  **beam_energy**
  ```rst
  python:float
  ```

  : The energy of the electron beam in keV

  **biprism_voltage**
  ```rst
  python:float
  ```

  : In volts

  **tilt_stage**
  ```rst
  python:float
  ```

  : In degrees

### Examples

```pycon
>>> s.set_microscope_parameters(beam_energy=300.)
>>> print('Now set to %s keV' %
>>>       s.metadata.Acquisition_instrument.
>>>       TEM.beam_energy)
```

Now set to 300.0 keV

<!-- !! processed by numpydoc !! -->

#### statistics(sb_position=None, sb='lower', high_cf=False, fringe_contrast_algorithm='statistical', apodization='hanning', single_values=True, show_progressbar=False, num_workers=None)

Calculates following statistics for off-axis electron holograms:

1. Fringe contrast using either statistical definition or
Fourier space approach (see description of fringe_contrast_algorithm parameter)
2. Fringe sampling (in pixels)
3. Fringe spacing (in calibrated units)
4. Carrier frequency (in calibrated units, radians and 1/px)

* **Parameters:**
  **sb_position**
  ```rst
  python:tuple, hyperspy.api.signals.Signal1D, python:None
  ```

  : The sideband position (y, x), referred to the non-shifted FFT.
    It has to be tuple or to have the same dimensionality as the hologram.
    If None, sideband is determined automatically from FFT.

  **sb**
  ```rst
  python:str, python:None
  ```

  : Select which sideband is selected. ‘upper’, ‘lower’, ‘left’ or ‘right’.

  **high_cf**
  ```rst
  bool, optional
  ```

  : If False, the highest carrier frequency allowed for the sideband location is equal to
    half of the Nyquist frequency (Default: False).

  **fringe_contrast_algorithm**
  ```rst
  python:str
  ```

  : Select fringe contrast algorithm between:
    * `'fourier'`: fringe contrast is estimated as 2 \* <I(k_0)> / <I(0)>,
      where I(k_0) is intensity of sideband and I(0) is the intensity of central band (FFT origin).
      This method delivers also reasonable estimation if the
      interference pattern do not cover full field of view.
    * `'statistical'`: fringe contrast is estimated by dividing the
      standard deviation by the mean of the hologram intensity in real
      space. This algorithm relies on regularly spaced fringes and
      covering the entire field of view.
    <br/>
    (Default: ‘statistical’)

  **apodization**
  ```rst
  python:str or python:None, optional
  ```

  : Used with `fringe_contrast_algorithm='fourier'`. If `'hanning'` or `'hamming'` apodization window
    will be applied in real space before FFT for estimation of fringe contrast.
    Apodization is typically needed to suppress striking  due to sharp edges of the image,
    which often results in underestimation of the fringe contrast. (Default: ‘hanning’)

  **single_values**
  ```rst
  bool, optional
  ```

  : If True calculates statistics only for the first navigation pixels and
    returns the values as single floats (Default: True)

  **show_progressbar**
  ```rst
  python:None or bool
  ```

  : If `True`, display a progress bar. If `None`, the default from
    the preferences settings is used.

  **num_workers**
  ```rst
  python:None or python:int
  ```

  : Number of worker used by dask. If None, default
    to dask default value.
* **Returns:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)
  : Dictionary with the statistics
* **Raises:**
  [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError)
  : If the signal axes are non-uniform axes.

### Examples

```pycon
>>> import holospy as holo
>>> s = holo.data.Fe_needle_reference_hologram()
>>> sb_position = s.estimate_sideband_position(high_cf=True)
>>> s.statistics(sb_position=sb_position)
{'Fringe spacing (nm)': 3.4860442674236256,
'Carrier frequency (1/px)': 0.26383819985575441,
'Carrier frequency (mrad)': 0.56475154609203482,
'Fringe contrast': 0.071298357213623778,
'Fringe sampling (px)': 3.7902017241882331,
'Carrier frequency (1 / nm)': 0.28685808994016415}
```

<!-- !! processed by numpydoc !! -->

### *class* holospy.signals.LazyHologramImage(\*args, \*\*kwargs)

Bases: [`LazySignal`](https://hyperspy.org/hyperspy-doc/current/reference/api.signals/LazySignal.html#hyperspy.api.signals.LazySignal), [`HologramImage`](#holospy.signals.HologramImage)

Lazy signal class for holograms acquired via off-axis electron
holography.

The computation is delayed until explicitly requested.

This class is not expected to be instantiated directly, instead use:

```pycon
>>> data = da.ones((10, 10))
>>> s = holospy.signals.HologramImage(data).as_lazy()
```

<!-- !! processed by numpydoc !! -->

Create a signal instance.

* **Parameters:**
  **data**
  ```rst
  numpy.ndarray
  ```

  : The signal data. It can be an array of any dimensions.

  **axes**
  ```rst
  [dict/axes], optional
  ```

  : List of either dictionaries or axes objects to define the axes (see
    the documentation of the [`AxesManager`](https://hyperspy.org/hyperspy-doc/current/reference/base_classes/axes.html#hyperspy.axes.AxesManager)
    class for more details).

  **attributes**
  ```rst
  python:dict, optional
  ```

  : A dictionary whose items are stored as attributes.

  **metadata**
  ```rst
  python:dict, optional
  ```

  : A dictionary containing a set of parameters
    that will to stores in the `metadata` attribute.
    Some parameters might be mandatory in some cases.

  **original_metadata**
  ```rst
  python:dict, optional
  ```

  : A dictionary containing a set of parameters
    that will to stores in the `original_metadata` attribute. It
    typically contains all the parameters that has been
    imported from the original data file.

  **ragged**
  ```rst
  bool or python:None, optional
  ```

  : Define whether the signal is ragged or not. Overwrite the
    `ragged` value in the `attributes` dictionary. If None, it does
    nothing. Default is None.

<!-- !! processed by numpydoc !! -->
