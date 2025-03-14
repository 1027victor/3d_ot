# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '3d_OT'
copyright = '2025, hpw'
author = 'hpw'
release = '0.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration




templates_path = ['_templates']


# Sphinx 扩展
extensions = ['nbsphinx']

# 确保 Sphinx 忽略 .ipynb 生成的输出缓存
nbsphinx_allow_errors = True  # 允许 Notebook 代码执行时出错（可选）
# exclude_patterns = ['build', '**.ipynb_checkpoints']  # 忽略 Jupyter Notebook 的缓存文件
exclude_patterns = ['**.ipynb_checkpoints']
nbsphinx_execute = 'never'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
