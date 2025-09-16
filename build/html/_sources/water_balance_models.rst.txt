.. _water balance models:

Hydrologic Water Balance Models
-------------------------------

CREST
~~~~~

The Coupled Routing and Excess Storage (CREST) distributed hydrological model is a hybrid strategy developed by the University of Oklahoma and the NASA SERVIR Project Team. CREST simulates the spatiotemporal variation of water and energy fluxes and storages on a user-defined grid. Its scalability is achieved through sub-grid scale representation of soil moisture storage (using a variable infiltration curve) and runoff generation (using linear reservoirs). Originally developed for global flood predictions, it is also suitable for basin-scale applications.

More detailed information about CREST can be found in the publication:  
`Flamig et al., (2020) <https://gmd.copernicus.org/articles/13/4943/2020/gmd-13-4943-2020.html>`_

CREST Parameter Set block
^^^^^^^^^^^^^^^^^^^^^^^^^
Defines the parameters for the CREST model.

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

SAC-SMA
~~~~~~~
The Sacramento Soil Moisture Accounting (SAC-SMA) Model was developed by the U.S. National Weather Service. Its purpose is to parameterize soil moisture characteristics so that applied moisture is logically distributed, percolation is realistically simulated, and streamflow is effectively modeled.

More detailed information about SAC-SMA is available at:  
`U.S. NWS SAC-SMA algorithm description  <http://www.nws.noaa.gov/oh/hrl/nwsrfs/users_manual/part2/_pdf/23sacsma.pdf>`_

SAC-SMA Parameter Set
^^^^^^^^^^^^^^^^^^^^^^^
Defines the parameters for the SAC-SMA model.

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

HP
~~
The Hydrophobic (HP) water balance model assumes an entirely impervious surface where all rainfall is transformed directly into surface runoff.

.. HP Parameter Set
   *To be completed in a future revision.*

