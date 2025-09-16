Hydrologic Water Balance Models
-------------------------------
CREST
~~~~~
The Coupled Routing and Excess Storage (CREST) distributed hydrological model is a hybrid strategy developed by the University of Oklahoma and the NASA SERVIR Project Team. CREST simulates the spatiotemporal variation of water and energy fluxes and storages on a user-defined grid. Its scalability is achieved through sub-grid scale representation of soil moisture storage (using a variable infiltration curve) and runoff generation (using linear reservoirs). Originally developed for global flood predictions, it is also suitable for basin-scale applications.

More detailed information about CREST can be found in the publication:  
`Flamig et al., (2020) <https://gmd.copernicus.org/articles/13/4943/2020/gmd-13-4943-2020.html>`_

CREST Parameter Set block
----------------
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