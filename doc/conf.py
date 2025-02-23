# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'BayesML'
copyright = '2022, BayesML Developers'
author = 'BayesML Developers'

# The full version, including alpha/beta/rc tags
release = '0.2.5'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx.ext.mathjax',
	'myst_parser',
	'sphinx.ext.autodoc',
	'numpydoc',
	'sphinx.ext.autosummary',
	'sphinx.ext.intersphinx'
	#'sphinx.ext.napoleon'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','devdoc']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = 'BayesML'

html_logo = 'logos/BayesML_logo.png'

myst_enable_extensions = ["dollarmath", "amsmath","html_image"]

html_theme_options = {
  "logo_only": True,
  "repository_url": "https://github.com/yuta-nakahara/BayesML/",
  "use_repository_button": True,
}

napoleon_use_rtype = False

autodoc_default_options = {
    'member-order': 'bysource',
}

#numpydoc_show_class_members = False

# html_style = 'css/customize.css'

autosummary_generate = True

#numpydoc_xref_param_type = True
intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                       'numpy': ('https://numpy.org/doc/stable/', None),
                       'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
                       'graphviz': ('https://graphviz.readthedocs.io/en/stable/', None)
}

html_favicon = 'logos/BayesML_favicon.ico'
