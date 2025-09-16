Inundation Models
=================

Simple Inundation (HAND method)
-------------------------------

Height Above Nearest Drainage (HAND) method proposed by Rennó et al. (2008), considers relative flow depth to fill a hydro-conditioned DEM. The methodology could be used to obtain quick results, but has some limitations as the listed ones (Aristizabal et al., 2023):

•	Doesn’t consider pluvial, coastal, ground water, and dam break components among other possible.
•	Inundation proxy or no physics model.
•	Requires all areas eligible for inundation to drain to the designated drainage network (Hydro-conditioning).
•	Higher resolutions can lack sufficient representation of fine grain features such as embankments, flood walls, and closure structures.

The following figure illustrates the implementation of the HAND methodology using EF5.

.. figure:: _static/outputs_examples/ex_simple_inundation.png
   :width: 400
   :align: center
   
   Water depth (.tif) output using EF5. The arbitrary color ramp represents the water depth for the simulated event.

The following figure briefly illustrates the implementation concept of HAND.

.. figure:: _static/HAND.png
   :width: 800
   :align: center
   
   HAND methodology implementation, from `(Rebolho et al., 2018) <https://hess.copernicus.org/articles/22/5967/2018/>`_

Simple Inundation Parameter Set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Defines the parameters for the simple inundation model. The parameters `alpha` and `beta` are used to define the coefficients for the rating curve power function, which is used to calculate the flow depth from the simulated flow rate.

.. confval:: PARAMETERS FOR INUNDATION

 
   ``gauge``: Gauge ID as defined in the BASIN block.
   
   ``alpha``: Lumped parameter for the rating curve alpha*(discharge)^beta.
   
   ``beta``: Lumped parameter for the rating curve alpha*(discharge)^beta.

   **Optional parameters:**

   ``alpha_grid``: Path for the grid of alpha parameter (.tif) for the rating curve alpha*(discharge)^beta. It must be accompanied by the ``alpha`` parameter, which will work as a multiplier factor for the grid values.

   ``beta_grid``: Path for the grid of beta parameter (.tif) for the rating curve alpha*(discharge)^beta. It must be accompanied by the ``beta`` parameter, which will work as a multiplier factor for the grid values.

Example of Simple Inundation Parameter Set block

.. code-block:: ini

   [simpleinundationparamset rundu]
   gauge=rundu
   alpha=2.991570
   beta=0.932080