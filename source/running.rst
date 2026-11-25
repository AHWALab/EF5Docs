Running EF5
============

.. toctree::
   :maxdepth: 1

   parameters
   style
   tasks
   controlfile

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

.. warning::
   Requirements for TIFF files:

   1. -9999 as nodata value.
   2. No TILED format.
   3. ``float32`` data type.
   4. The ESRI flow direction convention must be restricted to the following values: **1, 2, 4, 8, 16, 32, 64, and 128**.
   5. Each parameter grid must be a single-band GeoTIFF whose pixels are stored in one image plane (TIFF tag ``PlanarConfiguration = 1``, also called "contiguous", "pixel-interleaved" or "chunky"). Grids saved with separate planes (``PlanarConfiguration = 2``, "band-interleaved" or "planar") are not read.

Run EF5 in the terminal
------------------------

For the final step, to run EF5, execute the binary with the control file argument:

.. code-block:: bash

   ../bin/ef5 <your_controlfile_name.txt>