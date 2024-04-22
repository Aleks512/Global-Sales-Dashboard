# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Global Sales Dashboard'
copyright = '2024, Aleksandra Cichocka'
author = 'Aleksandra Cichocka'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = []
extensions = [
    'sphinx.ext.autodoc',  # Génère la doc à partir des docstrings
    'sphinx.ext.napoleon',  # Supporte les docstrings au format Google et Numpy
    'sphinx.ext.viewcode',  # Ajoute des liens vers le code source
]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']



import os
import sys
sys.path.insert(0, os.path.abspath('../../src/components'))  # Ajustez le chemin selon l'emplacement de vos modules

