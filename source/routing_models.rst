.. _routing models:

Routing Models
--------------
Linear Reservoir
~~~~~~~~~~~~~~~~
Adapted from the CREST implementation, the linear reservoir routing model uses two reservoirs—one for overland (surface) runoff and one for subsurface runoff.

Linear Reservoir Parameter Set
^^^^^^^^^^^^^^^^^^^^^^^
Defines the parameters for the linear reservoir model.

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

Kinematic Wave
~~~~~~~~~~~~~~
Kinematic wave routing is a simplified approximation of the Barré de Saint-Venant equations. It assumes that gravitational and friction forces cancel and neglects acceleration terms.

Kinematic Wave Parameter Set
^^^^^^^^^^^^^^^^^^^^^^^

Defines the parameters for the kinematic wave model.

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