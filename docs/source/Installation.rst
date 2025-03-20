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

Installation Guide
------------------

You can create an environment to run lib_3d_OT without any problems by following the code below:

.. code-block:: bash

   git clone https://github.com/dbjzs/3d-OT.git
   cd 3d-OT
   conda create -n 3d-OT -f environment.yaml
   conda activate 3d-OT
   pip install -r requirements.txt
   pip install git+https://github.com/dbjzs/3d-OT.git
