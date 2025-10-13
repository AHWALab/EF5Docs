.. _task styles:

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
      
      Defines the type of task EF5 will execute. See :ref:`style section <style>` 
      for the full list of supported style types. The available styles are:

      ``SIMU``: Runs a standard simulation using the defined model, forcings, and parameters.
      
      ``SIMU_RP``: Similar to ``SIMU``, but also generates grids for standard deviation, mean, and skewness to support return period estimation using the Log-Pearson Type III distribution.

      ``CLIP_BASIN``: Clips model inputs to the domain defined in the BASIN block.
 
      ``CALI_DREAM``: Performs model calibration using the DREAM algorithm. Requires additional parameter blocks specific to calibration.

.. confval:: MODEL

      Specifies the water balance model to be used. Options include:

      ``CREST``: The Coupled Routing and Excess STorage distributed hydrological model.

      ``SAC``: The SAC-SMA model.

      ``HyMOD``: HyMOD model.

      Visit section 4. Models for extended description of these options.

.. confval:: ROUTING

      Indicates the routing method to apply. Options include:

      ``KW``: Kinematic Wave Routing.

      ``LR``: Linear Reservoir Routing.

      Visit section 4. Models for extended description of these options.

.. confval:: BASIN

      The name of the Basin block, which defines the spatial extent over which the model will run.

.. confval:: PRECIP

      The name of the Precipitation block, which defines the precipitation input data.

.. confval:: PET

      Forcing file block name for potential evapotranspiration input data.

.. confval:: PARAM_SET

      The name of the Parameter Set block that contains water balance model parameters. Visit section 5. Parameters for extended description of these options.

.. confval:: ROUTING_PARAM_SET

      The Parameter Set block that contains parameters for the routing model. Visit section 5. Parameters for extended description of these options.


**Simulation timing parameters:**

.. confval:: TIMESTEP, TIME_BEGIN, TIME_END

      Sets the model time step. Supported units are ``d`` is for day step, ``h`` is for hour step, and ``u`` is for minute step. 

.. confval:: TIME_BEGIN

       Start time for the simulation, in YYYYMMDDHHMMUU format. Where ``YYYY`` is the year, ``MM`` is the month, ``DD`` is the day, ``HH`` is the hour, and ``UU`` is the minute.

.. confval:: TIME_END

      End time for the simulation, in YYYYMMDDHHMMUU format. Where ``YYYY`` is the year, ``MM`` is the month, ``DD`` is the day, ``HH`` is the hour, and ``UU`` is the minute.

.. confval:: TIME_WARMEND 

      (Optional) Marks the end of the model’s warm-up period, in YYYYMMDDHHMMUU format. Where ``YYYY`` is the year, ``MM`` is the month, ``DD`` is the day, ``HH`` is the hour, and ``UU`` is the minute.

.. confval:: TIME_STATE 

      (Optional) After warming up the model, users might save the states for future simulations. `TIME_STATE` specifies the time at which to output the model state, in YYYYMMDDHHMMUU format. Where ``YYYY`` is the year, ``MM`` is the month, ``DD`` is the day, ``HH`` is the hour, and ``UU`` is the minute.


**Simulation outputs:**

.. confval:: STATES 

      Path where state variable output files should be saved. If `TIME_STATE` is used, the model will use `STATES` path to look for the last states files, if available will use them in the simulation.

.. confval:: OUTPUT 

      Directory path where model output files will be written.

.. confval:: OUTPUT_GRIDS

      (Optional) Output grids to be generated, separated by "|". The available grids are:

      ``NONE``: No gridded output will be produced.

      ``STREAMFLOW``: Streamflow at each grid cell, in cubic meters per second (m³/s)

      ``UNITSTREAMFLOW``: Unit discharge, calculated as streamflow per contributing area (e.g., m³/s per km²).

      ``MAXSTREAMFLOW``: Maximum streamflow value at each grid cell during the simulation period (m³/s).

      ``MAXUNITSTREAMFLOW``: Maximum unit discharge (streamflow per unit area) observed during the simulation (m³/s per km²).

      ``PRECIP``: Precipitation (mm)

      ``PRECIPACCUM``: Accumulated precipitation (mm)  

      ``INUNDATION``: Simulated water depth for inundated areas, in meters (m).

      ``MAXINUNDATION``: Simulated maximum water depth for inundated areas during the simulation period (m)

      ``SOILMOISTURE``: Volumetric soil moisture content, expressed as a percentage (%).

      ``MAXSOILMOISTURE``: Maximum soil moisture value reached during the simulation, as a percentage (%).

      ``PET``: Potential evapotranspiration, in millimeters (mm). 

      ``TEMPERATURE``: Air temperature, in degrees Celsius (°C). 

      ``RETURNPERIOD``: Estimated return period of streamflow at each grid cell, in years.

      ``MAXRETURNPERIOD``: Maximum return period value during the simulation, in years.  

      ``SNOWWATER``: Snow Water Equivalent (SWE) from the snow model, in millimeters (mm). 

      ``MAXSNOWWATER``: Maximum snow water equivalent during the simulation, in millimeters (mm).  

      ``RUNOFF``: Surface runoff generated from rainfall, in millimeters per hour (mm/hr).  

      ``GROUNDWATER``: Conceptual representation of the groundwater table height, in millimeters (mm). 

      ``SUBRUNOFF``: Subsurface runoff (interflow or baseflow), in millimeters per hour (mm/hr).  


**Optional Files for Specialized Use:**

.. confval:: DA_FILE 

      (Optional): File containing streamflow observations for use with data assimilation.

.. confval:: CO_FILE 

      (Optional): Path to a combined output file, if desired.

.. confval:: RP_STDGRID 

      (Optional): GeoTIFF file with standard deviation values for the Log-Pearson Type III return period distribution.

.. confval:: RP_AVGGRID 

      (Optional): GeoTIFF file with average values for the return period distribution.

.. confval:: RP_CSGRID 

      (Optional): GeoTIFF file with skew coefficient values for the return period distribution.


**Required Parameters for Specific Model Components:**

.. confval:: SNOW_PARAM_SET 

      (Required if using SNOW) Parameter block for snow modeling.

.. confval:: INUNDATION_PARAM_SET

      (Required if using INUNDATION): Parameter block for inundation modeling.

.. confval:: CALI_PARAM 

      (Required if using CALI_DREAM): Water balance parameter set used during calibration.

.. confval:: ROUTING_CALI_PARAM 

      (Required if using CALI_DREAM): Routing parameter set used during calibration.

.. confval:: SNOW_CALI_PARAM 

      (Required if using SNOW with CALI_DREAM): Snow parameter set for calibration.

.. confval:: INUNDATION_CALI_PARAM 

      (Required if using INUNDATION with CALI_DREAM): Inundation parameter set for calibration.


**Forecast and Preload Options:**

.. confval:: PRELOAD_FILE 

      (Optional): Path to a preload file containing all forcings (precipitation, PET, temperature) for the current time range and basin. EF5 will generate this file if it does not already exist. Useful for speeding up runs when forcings do not change (e.g., during manual calibration).

.. confval:: PRECIPFORECAST 

      (Optional): Forecast precipitation block used if the primary precipitation block is unavailable.

.. confval:: TEMP 

      (Required if using SNOW): Temperature block for snow processes.

.. confval:: TEMPFORECAST 

      (Optional if using SNOW): Forecast temperature block, used as fallback if TEMP data is missing.
