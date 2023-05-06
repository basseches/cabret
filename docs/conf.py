import os
import sys

sys.path.insert(0, os.path.abspath('..'))

project = 'texonomy'
copyright = '2023, Ivy Basseches'
author = 'Ivy Basseches'
release = '0.2.0'

# -- General configuration ---------------------------------------------------

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon']
source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

napoleon_include_special_with_doc = True

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_static_path = ['_static']
