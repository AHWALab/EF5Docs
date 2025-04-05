About EF5
---------
A modeling tool for large scale hydrologic forecasting
======

The Ensemble Framework For Flash Flood Forecasting (EF5) is a hydrologic modeling 
platform, originally developed with the goal of simulating surface water
flows at continental and global scales for early warning
applications. 

EF5 is the primary modeling core in the Flooded Locations And Simulated Hydrographs 
(`FLASH <https://inside.nssl.noaa.gov/flash/>`_) system, an operational system for flash flood warning operations in the United States 
the National Weather Service (NWS) of the National Oceanic and Atmospheric Administration (NOAA). The main target of EF5 in FLASH has been the 
representation of physical processes describing rapid terrain responses to
rainfall, typical of flash floods.

.. figure:: _static/FLASH.png

    Schematic of the Continental United States FLASH system developed at The University of Oklahoma and NOAA's National Severe Storms Laboratory.

Flexible architecture for multiple physics representations
======
EF5 features multiple representations of the macro-physical processes of the water 
cycle. In its current version, it includes physics from the following three surface 
water balance modules handling the vertical fluxes of water in the soils and surface 
runoff generation: Coupled Routing and Excess Storage (CREST), 
Sacramento Soil Moisture Accounting (SAC-SMA), and
Hydrophobic (HP). It also includes two options for flow routing of water across 
the landscape and into the drainages following flow paths defined by a digital 
elevation model: linear reservoirs, and the kinematic wave approximation of the 
1-D Saint-Venant Equations of open channel flow.

.. figure:: _static/ef5_gmd_flamig2020_schematic.png
    
    Flowchart of EF5 main modules as presented in `Flamig et al. (2020) <https://gmd.copernicus.org/articles/13/4943/2020/>`_

Additionally, EF5 features a snowmelt module based on the SNOW-17 model and 
a heuristic algorithm for inundation mapping are included. EF5 has been designed 
as a modular architecture, which facilitates the addition of new physical 
representations as well as pre- and post-processing routines.

Acknowledgements
======
Initial support for the
development of EF5 was provided by NOAA and the National
Aeronautics and Space Administration (NASA)
to researchers at The University of Oklahoma and National Severe Storms Laboratory.

**Original Developers**

Zac Flamig [`Scholar <https://scholar.google.com/citations?user=AYUjs0YAAAAJ&hl=en&oi=ao>`_ | `GitHub <https://github.com/zflamig>`_]

Humberto Vergara [`Scholar <https://scholar.google.com/citations?user=v-irprAAAAAJ&hl=en&oi=ao>`_ | `GitHub <https://github.com/humberva>`_]

Jonathan Gourley [`Scholar <https://scholar.google.com/citations?user=ez7FKEsAAAAJ&hl=en>`_]

*Other contributors*

Jorge Duarte [`Scholar <https://scholar.google.com/citations?hl=en&user=8GC5yRgAAAAJ>`_ | `GitHub <https://github.com/babetoduarte>`_]