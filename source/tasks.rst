Task block
-----
The Task block specifies key information needed for running EF5. It defines the type of modeling task to be executed, the time period for the simulation, the time step, and the forcing data to be used.

A simple example of a Task block might look like this:

.. code-block:: ini

   [Task RunFF]
   STYLE=SIMU
   MODEL=CREST
   ROUTING=KW
   BASIN=FF
   PRECIP=Q2_PRECIP
   PET=PET
   OUTPUT=/EF5Demo/FF/output/
   PARAM_SET=MyCrest_params
   ROUTING_PARAM=MyKW_params
   TIMESTEP=5u
   TIME_BEGIN=201006010000
   TIME_END=201006010030


Task Block Parameters
-----

.. confval:: STYLE
      
      Defines the type of task EF5 will execute. See Section 4.1 for the full list of supported task types. The available styles are:

      ``SIMU``: Runs a standard simulation using the defined model, forcings, and parameters.
      
      ``SIMU_RP``: Similar to SIMU, but also generates grids for standard deviation, mean, and skewness to support return period estimation using the Log-Pearson Type III distribution.

      ``CLIP_GAUGE``: Automatically identifies all outlets and creates necessary configuration files for distributed modeling. Useful when setting up models with many gauges.

      ``BASIN_AVG``: Calculates basin-wide averages from gridded data (e.g., average precipitation). Usefull in parameter estimation, such as for kinematic wave routing.
      
      ``CALI_DREAM``: Performs model calibration using the DREAM algorithm. Requires additional parameter blocks specific to calibration.
      
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
