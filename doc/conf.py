# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import hyperspy.api as hs
from datetime import datetime

# Set logging level to `ERROR` to avoid exspy warning in documentation
hs.set_log_level("ERROR")


# -- Project information -----------------------------------------------------

project = "HoloSpy"
copyright = f"2023-{datetime.today().year}, HyperSpy Developers"
author = "HyperSpy Developers"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # numpydoc is necessary to parse the docstring using sphinx
    # otherwise the nitpicky option will raise many warnings
    "numpydoc",
    "sphinx_design",
    "sphinx_favicon",
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib.towncrier",
]

linkcheck_ignore = [
    "https://onlinelibrary.wiley.com",  # 403 Client Error: Forbidden for url
]

intersphinx_mapping = {
    "dask": ("https://docs.dask.org/en/latest", None),
    "exspy": ("https://hyperspy.org/exspy", None),
    "hyperspy": ("https://hyperspy.org/hyperspy-doc/current/", None),
    "kikuchipy": ("https://kikuchipy.org/en/latest/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "python": ("https://docs.python.org/3", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "github_url": "https://github.com/hyperspy/holospy",
    "icon_links": [
        {
            "name": "Gitter",
            "url": "https://gitter.im/hyperspy/hyperspy",
            "icon": "fab fa-gitter",
        },
    ],
    "logo": {
        "image_light": "_static/holospy-banner-light.svg",
        "image_dark": "_static/holospy-banner-dark.svg",
    },
    "header_links_before_dropdown": 6,
}

# -- Options for sphinx_favicon extension -----------------------------------

favicons = [
    "holospy.ico",
]

# Check links to API when building documentation
nitpicky = True

# -- Options for numpydoc extension -----------------------------------

numpydoc_show_class_members = False
numpydoc_xref_param_type = True
numpydoc_xref_ignore = {"type", "optional", "default", "of"}

autoclass_content = "both"

autodoc_default_options = {
    "show-inheritance": True,
}
toc_object_entries_show_parents = "hide"

# -- Options for towncrier_draft extension -----------------------------------

# Options: draft/sphinx-version/sphinx-release
towncrier_draft_autoversion_mode = "draft"
towncrier_draft_include_empty = False
towncrier_draft_working_directory = ".."


# def setup(app):
#     app.add_css_file("custom-styles.css")
