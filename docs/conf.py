import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import splitiorequests

project = 'splitio-requests'
copyright = '2020, Mikayel Aleksanyan'
author = 'Mikayel Aleksanyan'

# The full version, including alpha/beta/rc tags
version = release = splitiorequests.__version__


# -- General configuration ---------------------------------------------------

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosectionlabel']

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
