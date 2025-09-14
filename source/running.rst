Running EF5
-----------
To run EF5, execute the binary with an optional control file argument:

.. code-block:: bash

   ef5 <your_controlfile_name.txt>

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