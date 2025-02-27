Calibrating the Models
----------------------
Parameters' influence in the simulated time series

.. dropdown:: Parameters influence in the simulated time series

   .. image:: _static/Parameters_Sensitivity.png
      :width: 400

Complete Sample Configuration File for Calibrating
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: ini

   /*
    * This is an example configuration file for EF5
    */

   [Basic]
   DEM=/EF5Demo/FF/basic/DEM.asc
   DDM=/EF5Demo/FF/basic/DDM.asc
   FAM=/EF5Demo/FF/basic/FAM.asc
   PROJ=laea
   ESRIDDM=true

   [PrecipForcing Q2Precip]
   TYPE=BIF
   UNIT=mm/h
   FREQ=5u
   LOC=/EF5Demo/FF/precip
   NAME=Q2_YYYYMMDDHHUU.bif

   [PETForcing PET]
   TYPE=BIF
   UNIT=mm/h
   FREQ=m
   LOC=/EF5Demo/FF/pet
   NAME=PET_MM.bif

   [Gauge OKC]
   LON=-97.01
   LAT=35.68
   OBS=/EF5Demo/obs/okc.csv

   [Gauge AR]
   LON=-93.62
   LAT=34.37

   [Basin FF]
   GAUGE=OKC
   GAUGE=AR

   [CrestParamSet FF]
   GAUGE=AR
   COEM=24.230076 EXPM=0.502391 RIVER=1.73056
   UNDER=0.291339 LEAKO=0.56668 LEAKI=0.251648
   TH=63.20205 GM=1.364364 PWM=71.96465
   PB=0.964355 PIM=6.508687 PKE=0.19952
   PFC=2.578529 IWU=53.52593 ISO=5.899539
   ISU=17.31128
   GAUGE=OKC
   COEM=24.230076 EXPM=0.502391 RIVER=1.73056
   UNDER=0.291339 LEAKO=0.56668 LEAKI=0.251648
   TH=63.20205 GM=1.364364 PWM=71.96465
   PB=0.964355 PIM=6.508687 PKE=0.19952
   PFC=2.578529 IWU=53.52593 ISO=5.899539
   ISU=17.31128

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

   [Execute]
   TASK=RunFF