Model calibration
----------------------

To calibrate a specific model, CREST or SAC-SMA, you need to set up the calibration parameters range in the control file. The calibration process will optimize the parameters to minimize the difference between observed and simulated streamflow.
EF5 uses the DREAM method for optimization. You can specify the objective function -CC, NSCE, SSE-, which are statistic metrics to evaluate the model performance. The possible parameter ranges for calibration are also defined in the configuration file.
The following is an example of how to set up the calibration parameters in the configuration file:

.. dropdown:: Parameters influence in the simulated time series
   
   Example
   Example of dropdown





Table: Parameters definition and possible ranges for calibration.

+-----------+--------------------------------------------------------------------------------+-------------+--------------+--+--+--+--+--+--+
| Parameter | Definition                                                                     | Ref min val | Ref max val  |  |  |  |  |  |  |
+===========+================================================================================+=============+==============+==+==+==+==+==+==+
| alpha0    | The alpha value used for overland, not channel, routing                        | 0.01        | 5            |  |  |  |  |  |  |
| alpha     | Used in the equation Streamflow = alpha*(cross-sectional channel area)^beta    | 0.01        | 3            |  |  |  |  |  |  |
| beta      | Used in the equation Streamflow = alpha*(cross-sectional channel area)^beta    | 0.0001      | 1            |  |  |  |  |  |  |
| under     | The interflow flow speed multiplier                                            | 0.0001      | 3            |  |  |  |  |  |  |
| leaki     | Amount of water leaked from interflow reservoir in each time step              | 0.0001      | 1            |  |  |  |  |  |  |
| th        | Number of grid cells needed to flow into a cell for it to be part of a channel | 30          | 300          |  |  |  |  |  |  |
| isu       | Initial value of the interflow reservoir                                       | 0           | 0.0001       |  |  |  |  |  |  |
| wm        | Maximum soil water capacity                                                    | 5           | 600          |  |  |  |  |  |  |
| b         | The exponent of the VIC                                                        | 0.1         | 20           |  |  |  |  |  |  |
+-----------+--------------------------------------------------------------------------------+-------------+--------------+--+--+--+--+--+--+



+------------------------+------------+----------+
| Header row, column 1   | Header 2   | Header 3 |
+========================+============+==========+
| body row 1, column 1   | column 2   | column 3 |
+------------------------+------------+----------+
| body row 2             | Cells may span        |
+------------------------+-----------------------+


Control file example for Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ini

   [Basic]
   DEM=data/basic/dem_KY.tif
   DDM=data/basic/ddm_KY.tif
   FAM=data/basic/fam_KY.tif
   PROJ=geographic
   ESRIDDM=true
   SelfFAM=false

   [PETForcing CLIMO]
   LOC=data/pet/
   FREQ=1m
   UNIT=mm/d
   NAME=PET_MM_KY.tif
   TYPE=TIF

   [PrecipForcing MRMS]
   TYPE=TIF
   UNIT=mm/h
   FREQ=2u
   LOC=data/precip/
   NAME=PrecipRate_00.00_YYYYMMDD-HHUU00.tif

   [Gauge 0]
   lat=36.9883
   lon=-89.1326
   outputts=true
   basinarea=421966.3

   [Gauge 03404900]
   lon=-84.093599999999995
   lat=36.951400000000000
   basinarea=139.341000000000008
   obs=data/observations/usgs/Streamflow_Time_Series_CMS_UTC_USGS_03404900.csv

   [Gauge 03282040]
   lon=-83.810299999999998
   lat=37.500599999999999
   basinarea=200.205999999999989
   obs=data/observations/usgs/Streamflow_Time_Series_CMS_UTC_USGS_03282040.csv

   [Gauge 03250190]
   lon=-83.831699999999998
   lat=38.023899999999998
   basinarea=218.854000000000013
   obs=data/observations/usgs/Streamflow_Time_Series_CMS_UTC_USGS_03250190.csv

   [Gauge 03208950]
   lon=-82.438900000000004
   lat=37.123899999999999
   basinarea=172.234000000000009
   obs=data/observations/usgs/Streamflow_Time_Series_CMS_UTC_USGS_03208950.csv

   [Gauge 03208500]
   lon=-82.295800000000000
   lat=37.206899999999997
   basinarea=740.736999999999966
   obs=data/observations/usgs/Streamflow_Time_Series_CMS_UTC_USGS_03208500.csv

   [Gauge 03206600]
   lon=-82.296099999999996
   lat=38.017200000000003
   basinarea=99.714500000000001
   obs=data/observations/usgs/Streamflow_Time_Series_CMS_UTC_USGS_03206600.csv

   [Gauge 03284525]
   lon=-84.411100000000005
   lat=37.988300000000002
   basinarea=2.486400000000000
   obs=data/observations/usgs/Streamflow_Time_Series_CMS_UTC_USGS_03284525.csv

   [Gauge 03478400]
   lon=-82.133899999999997
   lat=36.631700000000002
   basinarea=69.670699999999997
   obs=data/observations/usgs/Streamflow_Time_Series_CMS_UTC_USGS_03478400.csv

   [Basin 0]
   #gauge=0
   #gauge=03404900
   gauge=03282040
   #gauge=03250190
   #gauge=03208950
   #gauge=03208500
   #gauge=03206600
   #gauge=03284525
   #gauge=03478400

   [CrestParamSet EF5KY] 
   wm_grid=data/parameters/CREST/wm_KY.tif
   im_grid=data/parameters/CREST/im_KY.tif
   fc_grid=data/parameters/CREST/ksat_KY.tif
   b_grid=data/parameters/CREST/b_KY.tif
   # The following code is used for the simulation process.
   # It is kept here to replace the optimized parameters later and run the simulation.  
   gauge=03282040
   wm=9.883508
   b=6.204447
   im=0.048939
   ke=0.832682
   fc=79.819237
   iwu=42.181957


   [KWParamSet EF5KY]
   under_grid=data/parameters/KW/ksat_KY.tif
   leaki_grid=data/parameters/KW/leaki_KY.tif
   alpha_grid=data/parameters/KW/alpha_KY.tif
   beta_grid=data/parameters/KW/beta_KY.tif
   alpha0_grid=data/parameters/KW/alpha0_KY.tif
   # The following code is used for the simulation process.
   # It is kept here to replace the optimized parameters later and run the simulation.  
   gauge=03282040
   under=0.000100
   leaki=5.144720
   th=10.00000
   isu=0.000000
   alpha=9.645860
   beta=0.361487
   alpha0=1.168505

   [CrestCaliParams 0CRESTCALI]
   # To set up the following ranges, please refer to the above table
   gauge=03282040
   objective=CC                       # Possible options: CC, NSCE, SSE
   dream_ndraw=20000 
   wm=0.05,10
   b=0.05,10
   im=0.005,1
   ke=0.001,1
   fc=0.0,150.0
   iwu=0.0,300.0

   [kwcaliparams 0KWCALI]
   # To set up the following ranges, please refer to the above table
   gauge=03282040
   under=0.0001,0.00010001
   leaki=0.02,10.0
   th=10,10.00001
   isu=0.0,0.000001
   alpha=0.05,10
   beta=0.05,10
   alpha0=0.05,10

   [Task TaskCalibration]
   STYLE=CALI_DREAM
   MODEL=crest
   ROUTING=KW
   BASIN=0
   PRECIP=MRMS
   PET=CLIMO
   OUTPUT=outputs
   STATES=data/states
   defaultparamsgauge=03282040
   PARAM_SET=EF5KY
   ROUTING_PARAM_Set=EF5KY
   CALI_PARAM=0CRESTCALI
   ROUTING_CALI_PARAM=0KWCALI
   #output_grids=MAXUNITSTREAMFLOW|MAXSTREAMFLOW
   TIMESTEP=2u
   TIME_BEGIN=20220727120000
   #TIME_WARMEND=20220727120000
   #TIME_STATE=20220730120000
   TIME_END=20220730120000

   [Task CREST_Simulation]
   STYLE=simu
   MODEL=crest
   ROUTING=KW
   BASIN=0
   PRECIP=MRMS
   PET=CLIMO
   OUTPUT=outputs
   STATES=data/states
   defaultparamsgauge=03282040
   PARAM_SET=EF5KY
   ROUTING_PARAM_Set=EF5KY
   output_grids=MAXUNITSTREAMFLOW|MAXSTREAMFLOW
   TIMESTEP=15u
   TIME_BEGIN=20220727120000
   #TIME_WARMEND=20220727120000
   #TIME_STATE=20220730120000
   TIME_END=20220730120000

   [Execute]
   task=TaskCalibration
   #task=CREST_Simulation              # Comment this line, and then, after the calibration, update the parameters
                                       # with the optimized values and un-comment it to run the simulation


Calibration output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The calibration process will generate an output file, "cali_dream.gauge_name.crest.csv", that contains the optimized parameters, at the end of the .csv file, and the objective function value. The output will be saved in the specified directory.

The optimized parameters will be saved in the following format:

.. code-block:: ini

   wm,b,im,ke,fc,iwu,under,leaki,th,isu,alpha,beta,alpha0,nsce,nsce/2
   1.243439,1.027347,0.028567,2.212074,0.690118,232.437332,0.002938,0.339752,12.009190,13.275298,1.238962,0.246814,2.164778,-8814420.000000,-4407210.000000
   ...
   ...
   ...
   [WaterBalance]
   wm=2.861236
   b=1.986400
   im=0.016121
   ke=2.344525
   fc=1.774454
   iwu=281.206879
   [Routing]
   under=0.002960
   leaki=0.707585
   th=12.006120
   isu=19.988890
   alpha=2.894948
   beta=2.375221
   alpha0=2.960580

.. admonition:: Common EF5 warning message in this step.
   
      WARNING: Failed to load preload file outputs/califorcings.bin
   
   It does not affect the process, it is related about a file created during the calibration task, which could be used in the future to re-run it.

.. admonition:: Common EF5 warning message in this step.
   
      ERROR:src/ExecutionController.cpp(94): Unimplemented simulation run style "7"
   
   It does not affect the calibration process.

.. WARNING::
   
   Common EF5 error message in this step:
      INFO:src/BasicGrids.cpp(625): Max gauge search distance is 217
      INFO:src/BasicGrids.cpp(735): Gauge 21677 (14.856667, -2.904167; 7, 2935): FAM 1
      INFO:src/BasicGrids.cpp(954): Walked 48852383 (out of 48893469) nodes for 0!
      terminate called after throwing an instance of 'std::bad_alloc'
         what():  std::bad_alloc
      Aborted.
   
   It could be related to the gage basin area verification, but it could be caused by a memory overload. Adding more RAM memory to your computer could solve this problem.

Parameters' sensitivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The following image shows the parameters' sensitivity in the simulated time series. Each parameter is varied while the others are kept constant. The sensitivity analysis helps to understand how each parameter influences the model output.

.. image:: _static/Parameters_Sensitivity.png
   :width: 400
   :align: center