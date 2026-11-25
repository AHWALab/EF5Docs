.. Reusable table: Kinematic wave routing parameters.
.. Pulled into pages with ``.. include:: tables/kw_parameters.rst``.
.. Excluded from the build in conf.py (exclude_patterns), so it is not a page on its own.

**Table:** Kinematic wave (KW) routing parameters definition, units and reference values.

.. list-table::
   :header-rows: 1
   :widths: 12 46 12 10 10 10
   :class: param-table

   * - Parameter
     - Definition
     - Units
     - Min
     - Mean
     - Max
   * - alpha
     - Kinematic wave coefficient
     - \(1)
     - 0.4
     - 3
     - 149
   * - beta
     - Kinematic wave exponent
     - \(1)
     - 0.4
     - 0.7
     - 1
   * - alpha0
     - Kinematic wave conveyance parameter
     - \(1)
     - 0.06
     - 0.7
     - 18
   * - under
     - Subsurface flow speed
     - \(m/s)
     - 0
     - 8
     - 51
   * - leaki
     - Reduction in interflow storage
     - \(%)
     - 0.127
     - 0.128
     - 0.129
   * - th\ :sup:`*`
     - Flow accumulation threshold in # of cells
     - \(1)
     - NA
     - NA
     - NA
   * - isu\ :sup:`†`
     - Initial water storage in channel grid cells
     - \(mm)
     - NA
     - NA
     - NA

| :sup:`*` **th**: Flow accumulation threshold, in number of upstream cells. EF5 treats a cell as a channel cell when its flow accumulation is greater than th. Multiplying th by the cell area gives the drainage area needed for a channel to form. That area varies widely between domains with climate, geology and relief, so no reference range is given.
| :sup:`†` **isu**: A state value, not a physical parameter. It sets the water stored in the interflow reservoir of each cell at the first time step of the simulation.

Adapted from `Flamig et al. (2020) <https://doi.org/10.5194/gmd-13-4943-2020>`__.