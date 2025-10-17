============
Installation
============

Using pip (recommended)
-----------------------

To install the package with pip, run the following command:

.. code-block:: shell

    pip install pymfoil

This should install all package dependencies automatically.

Alternatively if you want to upgrade an existing installation:

.. code-block:: shell

    pip install --upgrade pymfoil

Verify installation
-------------------

To check if the installation is ok use

.. code-block:: python

    import pymfoil as pymf 
    pymf .__version__

Creating a new environment (recommended)
----------------------------------------

This is the recommended method:

.. code-block::shell

    conda create -n pymfoil python=3
    conda activate pymfoil     

.. note::

    Alternatively *if you are running low on space on an SSD* drive you can use the prefix option (**IMPORTANT:** read through the following `StackOverflow Question: how to specify new environment location for conda create <https://stackoverflow.com/questions/37926940/how-to-specify-new-environment-location-for-conda-create>`__)


Install dependencies
~~~~~~~~~~~~~~~~~~~~~~

If the pip method is used the dependencies should be installed automatically.

Activate the new conda environment and install the following:

.. code-block::shell

    conda install numpy pandas scipy
    conda install matplotlib  seaborn
    conda install ipython jupyter
    conda install openpyxl 
    conda install tqdm
    

From source
-----------
The pymfoil uses a ``pyproject.toml`` file for (hopefully) compliance with PEP 517 and PEP 518.
To install the package from source, clone the repository and run the following command: 

.. code-block:: shell

    pip install . 

    

