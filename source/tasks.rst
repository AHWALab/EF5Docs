Task block
-----
Tasks define which model to run, the simulation period, timestep, and related settings.

.. code-block:: ini

   [Task RunFF]
   STYLE=SIMU
   MODEL=CREST
   BASIN=FF
   PRECIP=Q2_PRECIP
   PET=PET
   OUTPUT=/EF5Demo/FF/output/
   PARAM_SET=FF
   TIMESTEP=5u
   TIME_BEGIN=201006010000
   TIME_END=201006010030


Parameters
-----

.. confval:: STYLE
      
      Task style. The available styles are:

      ``SIMU``: Simulation
      
      ``SIMU_RP``: Simulation with return period
      
      ``CALI_DREAM``: Calibration using DREAM algorithm
      
      ``CALI_SCE``: Calibration using SCE algorithm

.. confval:: MODEL

      Water balance model. The available models are:

      ``CREST``: CREST model

      ``SAC``: SAC model

      ``HyMOD``: HyMOD model

.. confval:: BASIN

      Basin block name. This is the name of the basin block defined in the configuration file.

.. confval:: PRECIP

      Forcing file block name for precipitation. This is the name of the precipitation forcing block defined in the configuration file.

.. confval:: PET

      Forcing file block name for potential evapotranspiration. This is the name of the PET forcing block defined in the configuration file.

.. confval:: PARAM_SET

      Parameter set block name. This is the name of the parameter set block defined in the configuration file.

.. _time taxonomy:

.. confval:: TIMESTEP, TIME_BEGIN, TIME_END

      Simulation timing parameters. The timestep is the time interval for the simulation, and the begin and end times define the simulation period.
      
      The time format is YYYYMMDDHHUU, where ``YYYY`` is the year, ``MM`` is the month, ``DD`` is the day, ``HH`` is the hour, and ``UU`` is the minute.
      
      For time step, where ``d`` is for day step, ``h`` is for hour step, and ``u`` is for minute step.

.. confval:: OUTPUT_GRIDS

      Output grids to be generated, separated by "|". The available grids are:

      ``MAXUNITSTREAMFLOW``: tif output of maximum unit streamflow, for each time step in the simulation period.  

      ``MAXSTREAMFLOW``: tif output of maximum streamflow, one summary file for the entire simulation period.      

      ``PRECIPACCUM``: tif output of accumulated precipitation, for each time step in the simulation period.     

      ``INUNDATION``: tif output of inundation area, for each time step in the simulation period.

      ``MAXINUNDATION``: tif output of maximum inundation area, one summary file for the entire simulation period.