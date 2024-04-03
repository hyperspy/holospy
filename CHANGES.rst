Release Notes
*************

Changelog entries for the development version are available at
https://holospy.readthedocs.io/en/latest/changes.html

.. towncrier-draft-entries:: |release| [UNRELEASED]

.. towncrier release notes start

0.2 (2024-04-04)
================

Deprecations
------------

- The positional arguments ``holo_data`` and ``holo_sampling`` of :func:`~.reconstruct.reconstruct` have been renamed to ``data`` and ``sampling``, respectively. (`#26 <https://github.com/hyperspy/holospy/issues/26>`_)


Improved Documentation
----------------------

- Add holoSpy logo (`#26 <https://github.com/hyperspy/holospy/issues/26>`_)


Maintenance
-----------

- Use ruff for linting and formatting; check NPY2011. (`#28 <https://github.com/hyperspy/holospy/issues/28>`_)
- Fix numpy 1.25 deprecation. (`#29 <https://github.com/hyperspy/holospy/issues/29>`_)
- Enable numpydoc and nitpicky; fix docstrings. (`#30 <https://github.com/hyperspy/holospy/issues/30>`_)


0.1.1 (2023-12-02)
==================

Bug Fixes
---------

- Fix getting version from metadata (`#16 <https://github.com/hyperspy/holospy/issues/16>`_)


Maintenance
-----------

- Use towncrier to manage release notes and improve setting dev version (`#17 <https://github.com/hyperspy/holospy/issues/17>`_)


.. _changes_0.1:

0.1 (2023-11-15)
================

- Add pre-commit configuration file (`#4 <https://github.com/hyperspy/holospy/pull/4>`_)
- Format code using ``black`` and add workflow to check formatting (`#3 <https://github.com/hyperspy/holospy/pull/3>`_).
- Add GitHub workflows to tests and build packages (`#2 <https://github.com/hyperspy/holospy/pull/2>`_).
- Rename the ``max_workers`` argument to ``num_workers`` (`#9 <https://github.com/hyperspy/holospy/pull/9>`_)
- Setup codecov to measure coverage (`#10 <https://github.com/hyperspy/holospy/pull/10>`_)
- Add badges for tests, codecov and docs (`#11 <https://github.com/hyperspy/holospy/pull/11>`_)
- Add workflow to build and push documentation (`#13 <https://github.com/hyperspy/holospy/pull/13>`_)
- Consolidate package metadata in ``pyproject.toml`` (`#14 <https://github.com/hyperspy/holospy/pull/14>`_)
- Use ``setuptools_scm`` to set holospy version at build time (`#14 <https://github.com/hyperspy/holospy/pull/14>`_)
- Add package and test workflow (`#14 <https://github.com/hyperspy/holospy/pull/14>`_)
- Add python 3.12 (`#14 <https://github.com/hyperspy/holospy/pull/14>`_)
- Add release workflow (`#14 <https://github.com/hyperspy/holospy/pull/14>`_)

Initiation (2023-07-23)
=======================

- HoloSpy was split out of the `HyperSpy repository
  <https://github.com/hyperspy/hyperspy>`_ on July 23, 2023. The electron
  holography functionalities so far developed in HyperSpy were moved to the
  `HoloSpy repository <https://github.com/hyperspy/holospy>`_.
