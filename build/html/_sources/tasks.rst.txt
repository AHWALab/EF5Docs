Tasks
-----
Tasks define which model to run, the simulation period, timestep, and related settings.

.. code-block:: ini

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

* **STYLE**: Task style (e.g., SIMU, SIMU_RP, CALI_DREAM, etc.)
* **MODEL**: Water balance model (e.g., CREST, SAC, HyMOD)
* **BASIN**: Basin block name
* **PRECIP/PET**: Forcing file blocks
* **PARAM_SET**: Parameter set block name
* **TIMESTEP, TIME_BEGIN, TIME_END**: Simulation timing parameters