*********************
Software installation
*********************

EF5 is open-source and can be run in Windows, MacOS and Linux. Get Started by downloading the source code (MacOS/Linux) or pre-compiled executable (Windows).

.. admonition:: ready-to-run EF5.
   
   The Windows pre-compiled executable is a ready-to-run version of EF5. It can be downloaded `via the provided link <https://github.com/AHWALab/EF5/releases/download/v1.2.6/ef5_win64.zip>`_.


`Go to EF5 GitHub repository <https://github.com/AHWALab/EF5>`_

Compiling EF5
==============
EF5 uses the TIFF and GEOTIFF libraries for raster formats. Compilation can be performed in three steps:

1. **(Developer Only)** – If you are modifying the Makefile.am, run:

   .. code-block:: bash

      autoreconf --force --install

2. **Configure** – If you wish to install EF5 to a custom path, run:

   .. code-block:: bash

      ./configure --prefix=/path/to/installation

3. **Compile** – Build EF5 with:

   .. code-block:: bash

      make CXXFLAGS="-O3 -fopenmp"

Upon successful compilation, a binary named ``ef5`` will be created in the ``bin`` directory.

.. _how to cite ef5:

How to cite EF5
=========================

Flamig, Z. L., Vergara, H., and Gourley, J. J.: The Ensemble Framework For Flash Flood Forecasting (EF5) v1.2: description and case study, Geosci. Model Dev., 13, 4943–4958, https://doi.org/10.5194/gmd-13-4943-2020, 2020.


Changelog
=========

* v 1.2.6.                    **Status**: Released

      **Added**
      
        * New parameter th_fim to set a threshold for Simple Inundation simulations      
        * New output grid for simple inundation: HAND catchments      
        * Resource utilization summary printed after any task completes
      
      **Fixed**
      
        * Incorrect precipitation values when switching from Normal to Long Range simulations
      
      **Optimized**
      
        * Reduced duplicate warning prints, especially for "Node Soil Moisture" messages
    

* v 1.2.5.                    **Status**: Under development

    * [To be updated with changes once released]


* v 1.2.4.                    **Status**: Released

    * Merged average Grids branch with master, allowing users to run both simulation and averaging on the same EF5 so there is no need to use different versions of EF5 to do averaging.


* v 1.0.                      **Status**: Released

    * Initial release of EF5.