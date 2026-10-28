# PROJECT KNOWLEDGE BASE

**Generated:** 2026-10-24
**Commit:** 83c847f
**Branch:** deep_init

## OVERVIEW
HoloSpy: a HyperSpy extension for off-axis electron holography (hologram signal class plus phase reconstruction). Pure Python >=3.10, depends on hyperspy[image]>=2.4, numpy, scipy, pint, scikit-image, lazy_loader, GPLv3.

## STRUCTURE
```
holospy/
├── holospy/
│   ├── __init__.py / __init__.pyi    # lazy_loader stub: the .pyi IS the public API list
│   ├── hyperspy_extension.yaml       # registers signal_type "hologram" with HyperSpy
│   ├── reconstruct.py                # numpy-level FFT reconstruction primitives
│   ├── tools.py                      # carrier frequency, Fourier fringe contrast
│   ├── _version.py                   # importlib.metadata + setuptools_scm for editable git installs
│   ├── signals/
│   │   ├── _hologram_image.py        # HologramImage (945 lines, the core of the package)
│   │   ├── _lazy_hologram_image.py   # LazyHologramImage = LazySignal + HologramImage
│   │   └── hologram_image.py         # DEPRECATED shim, warns, scheduled for removal in 1.0
│   ├── data/                         # Fe needle object/reference .hdf5 samples (~1.3 MB each)
│   └── tests/                        # pytest, shipped inside the package (--pyargs holospy)
├── doc/                              # Sphinx + pydata theme, numpydoc, nitpicky
├── upcoming_changes/                 # towncrier news fragments
└── prepare_release.py                # towncrier build + bump fallback_version
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Signal behaviour (reconstruct, statistics, sideband) | `holospy/signals/_hologram_image.py` | Methods wrap `reconstruct.py`/`tools.py` through `self.map(...)` |
| Low-level math | `holospy/reconstruct.py`, `holospy/tools.py` | Plain numpy arrays, no signals |
| Add or rename a public symbol | the matching `__init__.pyi` | `lazy_loader.attach_stub` reads the stub; `__init__.py` stays untouched |
| Register a new signal type | `holospy/hyperspy_extension.yaml` | Entry point `hyperspy.extensions = holospy` in pyproject |
| Sample data loaders | `holospy/data/__init__.py` | `hs.load(..., mode="r", reader="hspy")`, UserWarnings suppressed |
| API docs | `doc/api/*.rst` | One rst per submodule; add new modules to `doc/api/index.rst` |
| Changelog entry | `upcoming_changes/<issue>.<type>.rst` | Types: new, enhancements, bugfix, api, deprecation, doc, maintenance |
| CI + AI policy | `.github/` | `compliance.yml` calls the org reusable workflow; `check-ai-co-author` hook locally, policy block verified in CI |
| Release | `releasing_guide.md`, `prepare_release.py` | Version comes from the git tag via setuptools_scm |

## CODE MAP
Refs are `git grep -w` hits across `holospy/` and `doc/`.

| Symbol | Type | Location | Refs | Role |
|--------|------|----------|------|------|
| `HologramImage` | class (`Signal2D`) | signals/_hologram_image.py | 45 | `_signal_type = "hologram"`; the entire user-facing API |
| `HologramImage.reconstruct_phase` | method | signals/_hologram_image.py | 26 | Object/reference reconstruction into a complex wave |
| `HologramImage.statistics` | method | signals/_hologram_image.py | 21 | Fringe contrast, sampling, carrier frequency (uses pint) |
| `HologramImage.estimate_sideband_position` | method | signals/_hologram_image.py | 20 | Maps `reconstruct.estimate_sideband_position` |
| `HologramImage.estimate_sideband_size` | method | signals/_hologram_image.py | 15 | Maps `reconstruct.estimate_sideband_size` |
| `reconstruct` | function | reconstruct.py | 13 | FFT, sideband aperture, inverse FFT |
| `LazyHologramImage` | class | signals/_lazy_hologram_image.py | 12 | Dask-backed variant |
| `calculate_carrier_frequency` | function | tools.py | 6 | Used by `statistics` |

## CONVENTIONS
- Lint and format with **ruff** (pre-commit: `ruff-check --fix`, `ruff-format`; rules F, E, W, I; E501 ignored). CONTRIBUTING.rst still says Black; ruff is what actually runs.
- Every source file starts with the GPLv3 license header block; copy it from a neighbouring file.
- Imports go in three blocks: stdlib, third party, then `holospy`.
- Docstrings follow numpydoc. Docs build with `nitpicky = True`, so every type cross-reference in a docstring must resolve through intersphinx.
- Modules are private (`_name.py`) and re-exported through `.pyi` stubs. A renamed public module keeps a `__getattr__` shim that emits `hyperspy.exceptions.VisibleDeprecationWarning` (see `signals/hologram_image.py`).
- Signal methods must work for both eager and lazy data: tests parametrize `lazy` over `[True, False]` and call `.as_lazy()`. Branch on `_is_dask_array` rather than assuming numpy.
- Methods that need uniform axes raise `NotImplementedError` for non-uniform axes (checked in `tests/test_non-uniform_not-implemented.py`).
- Units go through HyperSpy's registry (`hs._ureg`); never create a separate pint `UnitRegistry` (`test_pint_unit_registry`).
- Every user-visible PR adds a towncrier fragment written for users, not developers.

## ANTI-PATTERNS (THIS PROJECT)
- NEVER import from `holospy.signals.hologram_image` in new code; it is a deprecated shim. Use `holospy.signals`.
- Do not catch a specific pint exception class when parsing units: pint >= 0.26.2 changed `UndefinedUnitError` to `DefinitionSyntaxError` for HyperSpy's `"<undefined>"` sentinel. Catch `pint.PintError` (see `statistics`).
- Do not edit `__version__` or hardcode versions. Only `prepare_release.py` touches `fallback_version` in pyproject.
- Do not add a module to the package without adding it to the `.pyi` stub, or it will not be importable via `holospy.<name>`.

## COMMANDS
```bash
pip install -e .[dev]                 # tests + doc + black extras
pytest --pyargs holospy               # CI form; plain `pytest` also works (testpaths=holospy/tests)
pytest --pyargs holospy --cov=. --cov-report=xml
pre-commit run --all-files            # ruff lint + format
make -C doc html                      # Sphinx docs into doc/_build
towncrier build --draft               # preview the changelog
python prepare_release.py 0.5         # release prep (inside a PR)
```

## NOTES
- `conftest.py` forces matplotlib `agg`; CI also sets `MPLBACKEND=agg`.
- Two `test_reconstruct_phase_*` lazy cases skip with "Dask array flags not supported". Expected baseline: 23 passed, 2 skipped.
- The `.hdf5` sample files and `hyperspy_extension.yaml` ship as package data (`[tool.setuptools.package-data]`). Keep new data files matching those globs.
- On forks, CI fetches upstream tags so setuptools_scm can compute the version. Shallow clones fall back to `fallback_version`.
- The package_and_test and doc workflows are reusable workflows from `hyperspy/.github`; local edits cannot change their steps.
- No nested AGENTS.md: the repo has 63 tracked files and every subdirectory scores below 8, so this root file covers them.

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
<!-- hyperspy-ai-policy:begin -->
## HyperSpy AI policy (ecosystem contract)

Canonical source: https://github.com/hyperspy/.github/blob/main/AI-POLICY.md - do not reword
this block; the `check-agents-policy` pre-commit hook keeps it synchronized.

- Non-trivial AI-assisted changes need an accepted proposal in
  https://github.com/hyperspy/hyperspy-proposals BEFORE the implementation PR is reviewed.
  Trivial changes: PR review suffices.
- Every AI-assisted commit carries the trailer `Assisted-by: <tool>:<model>`
  (example: `Assisted-by: OpenCode:deepseek-4.0-pro`). Attribute the tool you interact with,
  not a wrapper.
- NEVER add `Co-authored-by:` trailers for AI tools; they are reserved for human co-authors.
  The `check-ai-co-author` commit-msg hook and the `compliance / ai-trailers` CI check reject
  them.
- Disable your tool's automatic co-author injection before committing: Claude Code
  `"includeCoAuthoredBy": false`; GitHub Copilot `github.copilot.chat.commitMessageGeneration`
  off; Cursor commit attribution off; OpenCode / oh-my-openagent: check skill and plugin configs.
- Run `pre-commit install` (installs the commit-msg stage) before your first commit; CI
  re-checks every PR commit regardless.
- Declare AI assistance in the pull-request template and link the accepted proposal when one
  is required.
<!-- hyperspy-ai-policy:end -->

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
