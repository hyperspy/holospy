.. _metadata_structure:

HoloSpy metadata structure
**************************

HoloSpy extends the :external+hyperspy:ref:`HyperSpy metadata structure
<metadata_structure>`
with conventions for metadata specific to its signal types. Refer to the
:external+hyperspy:ref:`HyperSpy metadata documentation <metadata_structure>`
for general metadata fields.

The metadata of any **signal objects** is stored in the `metadata` attribute,
which has a tree structure. By convention, the node labels are capitalized and
the ones for leaves are not capitalized. When a leaf contains a quantity that
is not dimensionless, the units can be given in an extra leaf with the same
label followed by the ``_units`` suffix.

Besides directly accessing the metadata tree structure, e.g.
``s.metadata.Signal.signal_type``, the HyperSpy methods
:external:py:meth:`set_item() <hyperspy.misc.utils.DictionaryTreeBrowser.set_item>`,
:external:py:meth:`has_item() <hyperspy.misc.utils.DictionaryTreeBrowser.has_item>` and
:external:py:meth:`get_item() <hyperspy.misc.utils.DictionaryTreeBrowser.get_item>`
can be used to add to, search for and read from items in the metadata tree,
respectively.

The holography-specific metadata structure is represented in the following
tree diagram. The default units are given in parentheses. Details about the
leaves can be found in the following sections of this chapter. Note that not
all types of leaves will apply to every type of measurement.

::

    metadata
    ├── General
    │   └── # see HyperSpy
    ├── Sample
    │   └── # see HyperSpy
    ├── Signal
    │   ├── signal_type
    │   └── # otherwise see HyperSpy
    └── Acquisition_instrument
        └── TEM
            └── Biprism
                ├── azimuth_angle (º)
                ├── position
                └── voltage (V)


General
=======

See :external+hyperspy:ref:`HyperSpy-Metadata-General
<general-metadata>`.

Sample
======

See :external+hyperspy:ref:`HyperSpy-Metadata-Sample
<sample-metadata>`.

Signal
======

signal_type
    type: string

    String that describes the type of signal. Currently, the only HoloSpy
    specific signal class is ``hologram``.

See :external+hyperspy:ref:`HyperSpy-Metadata-Signal <signal-metadata>` for
additional fields.

Acquisition Instrument
======================

TEM
===

Biprism
-------

This node stores parameters of biprism used in off-axis electron holography

azimuth_angle (º)
    type: Float

    Rotation angle of the biprism in degree

position
    type: Str

    Position of the biprism in microscope column, e.g. Selected area aperture
    plane

voltage
    type: Float

    Voltage of electrostatic biprism in volts

See :external+exspy:ref:`eXSpy TEM metadata <source-metadata>` for additional fields.
