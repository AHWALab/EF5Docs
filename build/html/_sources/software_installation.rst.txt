*********************
Software installation
*********************

Compiling EF5
==============
EF5 uses the TIFF and GEOTIFF libraries for raster formats. Compilation can be performed in three steps:

1. **(Developer Only)** – If you are modifying the Makefile.am, run:

   .. code-block:: bash

      autoreconf --force --install

2. **Configure** – If you wish to install EF5 to a custom path, run:

   .. code-block:: bash

      ./configure --prefix=/path/to/installation

3. **Compile** – Build EF5 with:

   .. code-block:: bash

      make CXXFLAGS="-O3 -fopenmp"

Upon successful compilation, a binary named ``ef5`` will be created in the ``bin`` directory.


Changelog
=========


v 1.2.5
--------

**Status**: Under development

* [To be updated with changes once released]


v 1.2.4
--------

**Status**: Released

* Merged average Grids branch with master, allowing users to run both simulation and averaging on the same EF5 so there is no need to use different versions of EF5 to do averaging.


v 1.0
------

**Status**: Released

* Initial release of EF5.