Running EF5
============

Setting up your own domain
---------------------------

For a detailed guide on setting up your own domain (generate files for your own study area), please refer to the `EF5-builder-toolkit <https://github.com/AHWALab/EF5-builder-toolkit>`_ GitHub repository. The toolkit provides step by step instructions for generating:

#. Basic files (DEM derived files)
#. Prepare Precipitation Forcing Data
#. Prepare Potential Evapotranspiration (PET) Data
#. Preparing Grids for a Distributed Model
      a. Prepare Soil Data
      b. Prepare impervious area
#. Automatically defining all outlets locations
#. Calculate Basin-Integrated Variables (aggregate variables pixel by pixel for the tributary area)
#. Generate CREST parameters
#. Generate the Kinematic Wave (KW) Parameters

Setting up your configuration
----------------------------

Before running EF5, ensure you have a properly configured control file. The control file specifies various parameters and paths needed for the simulation or taks. To set up your configuration, refer to the components listed below.


.. toctree::
   :maxdepth: 1
   :caption: Components:

   controlfile
   tasks
   execute_block


Final step
----------

To run EF5, execute the binary with an optional control file argument:

.. code-block:: bash

   ef5 <your_controlfile_name.txt>