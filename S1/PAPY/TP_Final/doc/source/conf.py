# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('/mnt/e/Centrale Nantes/AI/A2/PAPY/TP_Final/Mandelbrot_Julia_Plot'))

project = 'Mandelbrot_Julia_Plot'
copyright = '2023, Zhenyu PU'
author = 'Zhenyu PU'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon', # interprete les formats de docstring de google et numpy (en plus de .rst)
              'sphinx.ext.viewcode', # Donne accés au code source depuis la doc
              'myst_parser',
              'sphinx.ext.imgmath'
              ]

imgmath_image_format = 'svg'  # 指定数学公式的图像格式
imgmath_font_size = 14  # 指定数学公式的字体大小

imgmath_use_preview = False
latex_engine = 'xelatex'  # 使用xelatex引擎
imgmath_latex = 'xelatex'  # 使用xelatex引擎


source_suffix = [".rst", ".md"]

templates_path = ['_templates']
exclude_patterns = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', 'DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_css_files = ['pandoc.css']

html_theme = 'bizstyle'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
