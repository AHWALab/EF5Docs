Control file (Configuration file)
------------------
The configuration file controls all user-adjustable settings for EF5, including input forcings, output options, and run methods. It is generally case **insensitive** (except for file paths on case-sensitive systems). Three styles of comments are supported: bash (#), C (/* */), and C++ (//).



.. code-block:: ini

   # All variables (except file paths) are case insensitive
   // Multiple comment types are supported
   /*
      Including multi-line C-style comments
   */

Basic Information
~~~~~~~~~~~~~~~~~
Specifies file locations for the digital elevation model (DEM), drainage direction map (DDM), and flow accumulation map (FAM).

.. code-block:: ini

   [Basic]
   DEM=/EF5Demo/FF/basic/DEM.asc
   DDM=/EF5Demo/FF/basic/DDM.asc
   FAM=/EF5Demo/FF/basic/FAM.asc
   PROJ=laea
   ESRIDDM=true
   SELFFAM=true

Precipitation Information
~~~~~~~~~~~~~~~~~~~~~~~~~~
Defines the properties of the precipitation forcing files.

.. code-block:: ini

   [PrecipForcing Q2Precip]
   TYPE=BIF
   UNIT=mm/h
   FREQ=5u
   LOC=/EF5Demo/FF/precip
   NAME=Q2_YYYYMMDDHHUU.bif

Potential Evapotranspiration (PET) Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Defines the PET forcing file details.

.. code-block:: ini

   [PETForcing PET]
   TYPE=BIF
   UNIT=mm/h
   FREQ=m
   LOC=/EF5Demo/FF/pet
   NAME=PET_MM.bif

Gauge Locations
~~~~~~~~~~~~~~~
Specifies the locations of gauges for output and parameter assignment.

.. code-block:: ini

   [Gauge OKC]
   LON=-97.01
   LAT=35.68
   OBS=/EF5Demo/obs/okc.csv
   BASINAREA=341.88
   OUTPUTTS=TRUE

   [Gauge AR]
   LON=-93.62
   LAT=34.37

Basins
~~~~~~
Groups gauge locations into basins.

.. code-block:: ini

   [Basin FF]
   GAUGE=OKC
   GAUGE=AR

Parameter Sets
~~~~~~~~~~~~~~
Control the distributed model parameter settings. Parameters are specified per gauge.

CREST Parameter Set
~~~~~~~~~~~~~~~~~~~
.. code-block:: ini

   [CrestParamSet ABRFC]
   wm_grid=/path/to/wm.tif
   im_grid=/path/to/im.tif
   fc_grid=/path/to/ksat.tif
   b_grid=/path/to/b.tif
   gauge=03455500
   wm=1.00
   b=1.0
   im=0.01
   ke=1.0
   fc=1.00
   iwu=50.0

SAC-SMA Parameter Set
~~~~~~~~~~~~~~~~~~~~~
.. code-block:: ini

   [SacParamSet ABRFC]
   UZTWM_grid=/path/to/uztwm.tif
   UZFWM_grid=/path/to/uzfwm.tif
   UZK_grid=/path/to/uzk.tif
   ZPERC_grid=/path/to/zperc.tif
   REXP_grid=/path/to/rexp.tif
   LZTWM_grid=/path/to/lztwm.tif
   LZFSM_grid=/path/to/lzfsm.tif
   LZFPM_grid=/path/to/lzfpm.tif
   LZSK_grid=/path/to/lzsk.tif
   LZPK_grid=/path/to/lzpk.tif
   PFREE_grid=/path/to/pfree.tif
   gauge=01055000
   UZTWM=1.0
   UZFWM=1.0
   UZK=1.0
   PCTIM=0.101
   ADIMP=0.10
   RIVA=1.001
   ZPERC=1.0
   REXP=1.0
   LZTWM=1.0
   LZFSM=1.0
   LZFPM=1.0
   LZSK=1.0
   LZPK=1.0
   PFREE=1.0
   SIDE=0.0
   RSERV=0.3
   ADIMC=1.0
   UZTWC=0.55
   UZFWC=0.14
   LZTWC=0.56
   LZFSC=0.11
   LZFPC=0.46

HP Parameter Set
~~~~~~~~~~~~~~~~
*To be completed in a future revision.*

Linear Reservoir Parameter Set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: ini

   [lrparamset rundu]
   gauge=rundu
   coem=1611.115479
   river=307.980042
   under=2531.556641
   leako=0.918236
   leaki=0.017568
   th=8.140809
   iso=0.000040
   isu=0.000073

Kinematic Wave Parameter Set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: ini

   [KWParamSet rundu]
   GAUGE=rundu
   UNDER=1.673110
   LEAKI=0.043105
   TH=6.658569
   ISU=0.000000
   ALPHA=2.991570
   BETA=0.932080
   ALPHA0=4.603945

Snow-17 Parameter Set
~~~~~~~~~~~~~~~~~~~~~
.. code-block:: ini

   [snow17paramset tarbela]
   GAUGE=tarbela
   UADJ=0.184653
   MBASE=0.047224
   MFMAX=1.068658
   MFMIN=0.516059
   TIPM=0.911706
   NMF=0.077336
   PLWHC=0.093812
   SCF=2.219492

Simple Inundation Parameter Set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: ini

   [simpleinundationparamset rundu]
   gauge=rundu
   alpha=2.991570
   beta=0.932080

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
   OUTPUT_GRIDS=MAXUNITSTREAMFLOW|MAXSTREAMFLOW|PRECIPACCUM|INUNDATION|MAXINUNDATION # Refer to 
   PARAM_SET=FF
   TIMESTEP=5u
   TIME_BEGIN=201006010000
   TIME_END=201006010030

   [Execute]
   TASK=RunFF