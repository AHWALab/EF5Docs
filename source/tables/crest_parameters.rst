.. Reusable table: CREST water balance parameters.
.. Pulled into pages with ``.. include:: tables/crest_parameters.rst``.
.. Excluded from the build in conf.py (exclude_patterns), so it is not a page on its own.

**Table:** CREST water balance parameters definition, units and reference values.

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
   * - wm
     - Maximum soil water capacity
     - \(mm)
     - 0
     - 206
     - 2500
   * - fc
     - Soil saturated hydraulic conductivity
     - \(mm/hr)
     - 0
     - 8
     - 51
   * - b
     - Exponent of the infiltration curve
     - \(1)
     - 0
     - 5
     - 12
   * - im\ :sup:`‡`
     - Impervious area
     - \(%)
     - 0
     - 1
     - 96
   * - ke\ :sup:`§`
     - Potential evapotranspiration adjustment factor
     - \(1)
     - NA
     - NA
     - NA
   * - iwu\ :sup:`†`
     - Initial value of soil water
     - \(%)
     - 0
     - NA
     - 100

| :sup:`†` **iwu**: A state value, not a physical parameter. It sets the soil water at the first time step as a percentage of wm (initial soil water = iwu × wm / 100).
| :sup:`‡` **im**: For a lumped value, enter im as a percentage, because EF5 divides it by 100. With a gridded parameter, EF5 uses the grid value × im as it is, so that product must be a fraction between 0 and 1.
| :sup:`§` **ke**: A multiplier applied to the input PET (PET used by the model = ke × input PET). A value of 1 keeps the input PET unchanged and is a good starting point, so no reference range is given.

Adapted from `Flamig et al. (2020) <https://doi.org/10.5194/gmd-13-4943-2020>`__.