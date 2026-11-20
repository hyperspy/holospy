<!-- This is a stub, see the top level CHANGES.rst file for the changelog. -->

# Release Notes

Changelog entries for the development version are available at
[https://holospy.readthedocs.io/en/latest/changes.html](https://holospy.readthedocs.io/en/latest/changes.html)

## [UNRELEASED] (2026-11-20)

### Bug Fixes

- Fix incompatibility with `pint >= 0.26.2`, which raises
  `DefinitionSyntaxError` instead of `UndefinedUnitError` when parsing
  HyperSpy’s `"<undefined>"` sentinel for unset units, causing
  `HologramImage.statistics` to raise an unclear error instead of the
  intended `ValueError("Signal axes units should be defined.")`. ([#72](https://github.com/hyperspy/holospy/issues/72))

### Improved Documentation

- Add LLM-friendly Markdown rendering of the documentation using the [sphinx-llm](https://github.com/NVIDIA/sphinx-llm) extension: each documentation page is now also rendered as a Markdown file (`<page>.md`) alongside the HTML output, an `llms.txt` index of the Markdown files is generated for LLMs and agents, and all pages are concatenated into a single `llms-full.txt` file. ([#73](https://github.com/hyperspy/holospy/issues/73))

### Maintenance

- Adopt the HyperSpy AI policy: shared pre-commit hooks, compliance CI workflow and an AGENTS.md knowledge base. ([#74](https://github.com/hyperspy/holospy/issues/74))

<!-- towncrier release notes start -->

## 0.4.0 (2026-10-17)

### Enhancements

- Add lazy import to reduce import time and reduce memory usage. ([#65](https://github.com/hyperspy/holospy/issues/65))

### Maintenance

- Update supported Python versions to 3.10, 3.11, 3.12, 3.13, 3.14; drop 3.8, 3.9. ([#65](https://github.com/hyperspy/holospy/issues/65))
- Update release workflow to upload release notes and artifacts to GitHub releases. ([#66](https://github.com/hyperspy/holospy/issues/66))
- Add a `.mailmap` file to consolidate duplicate author identities in
  the git history, fixing contributor attribution for tools that respect
  mailmap. ([#69](https://github.com/hyperspy/holospy/issues/69))

## 0.3 (2024-05-02)

### Improved Documentation

- Fix DOI and add more badges to readme file. ([#34](https://github.com/hyperspy/holospy/issues/34))

### Maintenance

- Use `pint.get_application_registry` instead of HyperSpy private API to get the handle of the `pint.UnitRegistry`. ([#35](https://github.com/hyperspy/holospy/issues/35))
- Add/enable more ruff rules: isort, pyflakes, pycodestyle. ([#37](https://github.com/hyperspy/holospy/issues/37))

## 0.2 (2024-04-04)

### Deprecations

- The positional arguments `holo_data` and `holo_sampling` of [`reconstruct()`](api/reconstruct.md#holospy.reconstruct.reconstruct) have been renamed to `data` and `sampling`, respectively. ([#26](https://github.com/hyperspy/holospy/issues/26))

### Improved Documentation

- Add holoSpy logo ([#26](https://github.com/hyperspy/holospy/issues/26))

### Maintenance

- Use ruff for linting and formatting; check NPY2011. ([#28](https://github.com/hyperspy/holospy/issues/28))
- Fix numpy 1.25 deprecation. ([#29](https://github.com/hyperspy/holospy/issues/29))
- Enable numpydoc and nitpicky; fix docstrings. ([#30](https://github.com/hyperspy/holospy/issues/30))

## 0.1.1 (2023-12-02)

### Bug Fixes

- Fix getting version from metadata ([#16](https://github.com/hyperspy/holospy/issues/16))

### Maintenance

- Use towncrier to manage release notes and improve setting dev version ([#17](https://github.com/hyperspy/holospy/issues/17))

<a id="changes-0-1"></a>

## 0.1 (2023-11-15)

- Add pre-commit configuration file ([#4](https://github.com/hyperspy/holospy/pull/4))
- Format code using `black` and add workflow to check formatting ([#3](https://github.com/hyperspy/holospy/pull/3)).
- Add GitHub workflows to tests and build packages ([#2](https://github.com/hyperspy/holospy/pull/2)).
- Rename the `max_workers` argument to `num_workers` ([#9](https://github.com/hyperspy/holospy/pull/9))
- Setup codecov to measure coverage ([#10](https://github.com/hyperspy/holospy/pull/10))
- Add badges for tests, codecov and docs ([#11](https://github.com/hyperspy/holospy/pull/11))
- Add workflow to build and push documentation ([#13](https://github.com/hyperspy/holospy/pull/13))
- Consolidate package metadata in `pyproject.toml` ([#14](https://github.com/hyperspy/holospy/pull/14))
- Use `setuptools_scm` to set holospy version at build time ([#14](https://github.com/hyperspy/holospy/pull/14))
- Add package and test workflow ([#14](https://github.com/hyperspy/holospy/pull/14))
- Add python 3.12 ([#14](https://github.com/hyperspy/holospy/pull/14))
- Add release workflow ([#14](https://github.com/hyperspy/holospy/pull/14))

## Initiation (2023-07-23)

- HoloSpy was split out of the [HyperSpy repository](https://github.com/hyperspy/hyperspy) on July 23, 2023. The electron
  holography functionalities so far developed in HyperSpy were moved to the
  [HoloSpy repository](https://github.com/hyperspy/holospy).
