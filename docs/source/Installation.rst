Installation
============

System Requirements
-------------------

Hardware requirements
~~~~~~~~~~~~~~~~~~~~~

``lib_3d_OT`` package requires only a standard computer with enough RAM to support the in-memory operations.

Software requirements
~~~~~~~~~~~~~~~~~~~~~

OS Requirements
^^^^^^^^^^^^^^^

This package is supported for *Linux*. The package has been tested on the following systems:

- Linux: Ubuntu 22.04

Python Dependencies
^^^^^^^^^^^^^^^^^^^

``lib_3d_OT`` mainly depends on the Python(>=3.10.13) scientific stack.

For specific setting, please see `requirements.txt <https://github.com/dbjzs/3d-OT/blob/main/requirements.txt>`_.

R Dependencies
^^^^^^^^^^^^^^

We need your environment to have R(>=4.3.1) and ``mclust(6.1.1)`` package installed.

Installation via Github
=======================

Download
--------

.. code-block:: bash

   git clone https://github.com/dbjzs/3d-OT.git
   cd 3d-OT

Environment
-----------

3d-OT is available for Python 3.10. We recommend training 3d-OT models on a device with GPU support.

Using the conda install environment:

.. code-block:: bash

   conda create -n 3d-OT -c conda-forge python==3.10.13 libopenblas=0.3.25 r-base=4.3.1 r-mclust -y
   conda activate 3d-OT

Package
-------

Then install 3d-OT using pip:

.. code-block:: bash

   pip install -r requirements.txt
   pip install .

Jupyter Tutorial
================

.. code-block:: bash

   pip install ipykernel
   python -m ipykernel install --user --name=3d-OT --display-name="Python (3d-OT)"

Please use the kernel name as follows: ``Python [conda env:3d-OT]``
