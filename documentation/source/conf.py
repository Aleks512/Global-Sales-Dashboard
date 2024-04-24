# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
# Ensure the path includes the directory where the 'src' directory is located.
#sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../../src'))
#sys.path.insert(0, os.path.abspath('../../'))
print("Current sys.path:", sys.path)  # This will help you see what's in the path



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
extensions.append('sphinx.ext.intersphinx')


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


try:
    from components import table_manager
    print("Imported table_manager successfully.")
except ImportError as e:
    print("Failed to import table_manager:", e)




