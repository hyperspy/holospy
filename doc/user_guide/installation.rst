.. _installation:

Installation
************

To install HoloSpy, you have the following options (independent of the operating system you use):

1. HoloSpy is included in the `HyperSpy Bundle <https://hyperspy.org/hyperspy-bundle/>`_,
   a standalone program that includes a python distribution and all relevant libraries
   (recommended if you do not use *python* for anything else).
2. :ref:`conda` (recommended if you are also working with other *python* packages).
3. :ref:`pip`.
4. Installing the development version from `GitHub <https://github.com/hyperspy/holospy/>`_.
   Refer to the appropriate section in the :external+hyperspy:ref:`HyperSpy user guide
   <install-dev>` (replacing ``hyperspy`` by ``holospy``).


.. _conda:

Installation using conda
========================

Follow these 3 steps to install HoloSpy using **conda** and start using it.

1. Creating a conda environment
-------------------------------

HoloSpy requires Python 3 and ``conda`` -- we suggest using the Python 3 version
of `Miniforge <https://conda-forge.org/miniforge/>`_.

We recommend creating a new environment for the HoloSpy package (or installing
it in the :external+hyperspy:ref:`HyperSpy <anaconda-install>`
environment, if you have one already). To create a new environment:

1. Load the miniforge prompt.
2. Run the following command:

.. code-block:: bash

    (base) conda create -n holospy -y


2. Installing the package in the new environment
------------------------------------------------

Now activate the holospy environment and install the package from ``conda-forge``:

.. code-block:: bash

    (base) conda activate holospy
    (holospy) conda install -c conda-forge holospy -y

Required dependencies will be installed automatically.

Installation is completed! To start using it, check the next section.

.. Note::

   If you run into trouble, check the more detailed documentation in the
   :external+hyperspy:ref:`HyperSpy user guide <anaconda-install>`.


3. Getting Started
------------------

To get started using HoloSpy, especially if you are unfamiliar with Python, we
recommend using `Jupyter notebooks <https://jupyter.org/>`_. Having installed
HoloSpy as above, a Jupyter notebook can be installed and opened using the following commands
entered into an anaconda prompt (from scratch):

.. code-block:: bash

    (base) conda activate holospy
    (holospy) conda install -c conda-forge jupyterlab -y
    (holospy) jupyter lab


.. _pip:

Installation using pip
========================

Alternatively, you can also find HoloSpy in the `Python Package Index (PyPI) <https://pypi.org>`_
and install it using (requires ``pip``):

.. code-block:: bash

    pip install holospy

Required dependencies will be installed automatically.


Updating the package
====================

Using **conda**:

.. code-block:: bash

    conda update holospy -c conda-forge

Using **pip**:

.. code-block:: bash

    pip install holospy --upgrade

.. Note::

    If you want to be notified about new releases, please *Watch (Releases only)* the `HoloSpy repository
    on GitHub <https://github.com/hyperspy/holospy/>`_ (requires a GitHub account).
