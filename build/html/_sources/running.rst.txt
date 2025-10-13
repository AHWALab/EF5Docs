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

Control file (Configuration file)
----------------------------------

Before running EF5, ensure you have a properly configured control file. The control file specifies various parameters and paths needed for the simulation or tasks. 

The control file is structured into blocks, each containing key-value pairs. Example:

   .. code-block:: ini
      
      [Basic]                                       # Basic block

The minimum required blocks are:
      
#. Basic block: Specifies file locations for the digital elevation model (DEM), flow direction map (DDM), and flow accumulation map (FAM).
#. Precipitation forcing block: Defines the properties of the precipitation forcing files.
#. PET forcing block: Defines the PET forcing files details.
#. Gauge block(s): Specifies the locations of gauges for output and parameter assignment. At least one gauge block is required.
#. Basin block(s): Defines the basin(s) for the simulation, including associated gauges. At least one basin block is required.
#. Parameter set block(s): For the chosen models.
#. Task block(s): Defines the style to be executed, the routing model, the time period for the simulation, the time step, and the forcing data to be used. See :ref:`task styles <task styles>` for more details.
    The Style parameter within the Task block defines the type of task EF5 will execute, e.g., ``SIMU`` for a standard simulation, ``CLIP_GAUGE`` for clipping model inputs to the entire domain, ``CALI_DREAM`` for calibration using the DREAM algorithm, etc. See :ref:`task styles <task styles>` for the full list of supported Style types.
#. Execute block: Specifies which task to run, one at a time per run. At least one Execute block is required.

The following mock-up illustrates the bare minimum structure for a control file required to run any of the available styles.

.. code-block:: ini

   [Basic]                                       # Basic block
   DEM=/EF5Demo/FF/basic/DEM.asc
   ...

   [PrecipForcing Q2Precip]                      # Precipitation forcing block
   TYPE=BIF
   UNIT=mm/h
   ...

   [PETForcing PET]                              # PET forcing block
   TYPE=BIF
   UNIT=mm/h
   ...

   [Gauge 0]                                     # At least one gauge is required
   LON=-97.01
   LAT=35.68
   ...

   [Basin FF]                                    # At least one basin is required
   GAUGE=0                                       # containing at least one gauge

   [CrestParamSet FF]                            # Parameter set for routing model
   GAUGE=AR
   ...

   [Task RunFF]                                  # Task block
   STYLE=SIMU                                    # Style, refer to "4.2.3. Task block parameters"
   MODEL=CREST
   BASIN=0
   PRECIP=Q2_PRECIP
   PET=PET
   OUTPUT=/EF5Demo/FF/output/
   TIMESTEP=5u
   TIME_BEGIN=201006010000
   TIME_END=201006010030

   [Execute]                                     # Execute block
   TASK=RunFF                                    

To set up your configuration, refer to the components listed below.

.. toctree::
   :maxdepth: 1
   :caption: Components:

   controlfile
   tasks
   execute_block


Run EF5 in the terminal
------------------------

For the final step, to run EF5, execute the binary with the control file argument:

.. code-block:: bash

   ../bin/ef5 <your_controlfile_name.txt>