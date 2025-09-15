Model calibration
----------------------

To calibrate a specific model, CREST or SAC-SMA, you need to set up the calibration parameters range in the control file. The calibration process will optimize the parameters to minimize the difference between observed and simulated streamflow.
EF5 uses the DREAM method for optimization. You can specify the objective function -CC, NSCE, SSE-, which are statistic metrics to evaluate the model performance. The possible parameter ranges for calibration are also defined in the configuration file.
The following is an example of how to set up the calibration parameters in the configuration file:



.. admonition:: Lumped (aggregated) vs distributed (grided) parameters.
   
   Take a look at the :ref:`lumped and distributed description <lumped distributed>` in the Coltrolfile section for more details about the difference between lumped and distributed parameters.
   
**Table:** Kinematic wave **lumped** parameters definition and possible ranges for calibration.

+-----------+--------------------------------------------------------------------------------+-------------+--------------+
| Parameter | Definition                                                                     | Ref min val | Ref max val  |
+===========+================================================================================+=============+==============+
| alpha0    | Used for overland, not channel, routing                                        | 0.01        | 5            |
+-----------+--------------------------------------------------------------------------------+-------------+--------------+
| alpha     | Used in the equation Streamflow = alpha*(cross-sectional channel area)^beta    | 0.01        | 3            |
+-----------+--------------------------------------------------------------------------------+-------------+--------------+
| beta      | Used in the equation Streamflow = alpha*(cross-sectional channel area)^beta    | 0.0001      | 1            |
+-----------+--------------------------------------------------------------------------------+-------------+--------------+
| under     | Interflow flow speed multiplier                                                | 0.0001      | 3            |
+-----------+--------------------------------------------------------------------------------+-------------+--------------+
| leaki     | Amount of water leaked from interflow reservoir in each time step              | 0.0001      | 1            |
+-----------+--------------------------------------------------------------------------------+-------------+--------------+
| th        | Number of grid cells needed to flow into a cell for it to be part of a channel | 30          | 300          |
+-----------+--------------------------------------------------------------------------------+-------------+--------------+
| isu       | Initial value of the interflow reservoir                                       | 0           | 0.0001       |
+-----------+--------------------------------------------------------------------------------+-------------+--------------+



**Table:** CREST **lumped** parameters definition and possible ranges for calibration.

+-----------+-------------------------------------------------------+-------------+--------------+
| Parameter | Definition                                            | Ref min val | Ref max val  |
+===========+=======================================================+=============+==============+
| wm        | Maximum soil water capacity                           | 5           | 600          |
+-----------+-------------------------------------------------------+-------------+--------------+
| b         | Exponent of the variable infiltration curve (VIC)     | 0.1         | 20           |
+-----------+-------------------------------------------------------+-------------+--------------+
| im        | Impervious area ratio                                 | 0.01        | 0.5          |
+-----------+-------------------------------------------------------+-------------+--------------+
| ke        | Multiplier to convert between input PET and local PET | 0.001       | 1            |
+-----------+-------------------------------------------------------+-------------+--------------+
| fc        | Soil saturated hydraulic conductivity (Ksat) in mm/hr | 0           | 150          |
+-----------+-------------------------------------------------------+-------------+--------------+
| iwu       | Initial value of soil water                           | 2.5         | 250          |
+-----------+-------------------------------------------------------+-------------+--------------+



Control file example for Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ini

   [Basic]
   ...

   [PETForcing CLIMO]
   ...

   [PrecipForcing MRMS]
   ...

   [Gauge 03404900]
   lon=-84.093599999999995
   lat=36.951400000000000
   obs=data/observations/usgs/Q_03404900.csv

   [Basin 0]
   gauge=03404900

   # The following code is used for the simulation process.
   # It is kept here to replace the optimized parameters later and run the simulation.  
   [CrestParamSet EF5KY] 
   gauge=03404900
   wm=9.883508
   ...

   # The following code is used for the simulation process.
   # It is kept here to replace the optimized parameters later and run the simulation.  
   [KWParamSet EF5KY]
   gauge=03404900
   under=0.000100
   leaki=5.144720
   ...

   [CrestCaliParams 0CRESTCALI]
   # To set up the following ranges, please refer to the above table
   gauge=03404900
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
   gauge=03404900
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
   defaultparamsgauge=03404900
   PARAM_SET=EF5KY
   ROUTING_PARAM_Set=EF5KY
   CALI_PARAM=0CRESTCALI
   ROUTING_CALI_PARAM=0KWCALI
   TIMESTEP=2u
   TIME_BEGIN=20220727120000
   TIME_END=20220730120000

   # The following code is used for the simulation process.
   # It is kept here to replace the optimized parameters later and run the simulation.  
   [Task CREST_Simulation]
   ...

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
   
   *WARNING: Failed to load preload file outputs/califorcings.bin*
   
      This warning does not affect the process, it is related about a file created during the calibration task, which could be used in the future to re-run it.

.. admonition:: Common EF5 warning message in this step.
   
   *ERROR:src/ExecutionController.cpp(94): Unimplemented simulation run style "7"*
   
      This warning does not affect the calibration process.

.. WARNING::
   
   Common EF5 error message in this step:   
   
   | *INFO:src/BasicGrids.cpp(625): Max gauge search distance is 217*  
   | *INFO:src/BasicGrids.cpp(735): Gauge 21677 (14.856667, -2.904167; 7, 2935): FAM 1*  
   | *INFO:src/BasicGrids.cpp(954): Walked 48852383 (out of 48893469) nodes for 0!*  
   | *terminate called after throwing an instance of 'std::bad_alloc'*  
   | *what():  std::bad_alloc*  
   | *Aborted.*
   
      This error message could be related to the gauge basin area verification, but it is also caused by a memory overload. Adding more RAM to your job would solve this problem.

Parameters' sensitivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The following image shows the parameters' sensitivity in the simulated time series. Each parameter is varied while the others are kept constant. The sensitivity analysis helps to understand how each parameter influences the model output.

.. figure:: _static/Parameters_Sensitivity.png
   :width: 400
   :align: center

   Parameters sensitivity analysis. Blue line represents the observed streamflow, the read lines goes from the lowest to the highest value of each parameter, where thickness indicates the increasing value of the parameter.

.. toggle::

   Here is my toggle-able content!

.. dropdown::

    Dropdown content

.. dropdown:: Dropdown title

    Dropdown content

.. dropdown:: Open dropdown
    :open:

    Dropdown content
