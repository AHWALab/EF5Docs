# EF5 Documentation

This repository contains the official documentation for EF5. The documentation is built using Sphinx and is located in the `source/` folder.

## Getting Started

Follow these steps to set up and build the EF5 documentation locally.

---

### 1. Clone the Repository
Clone this repository to your local machine using Git:

```bash
git clone https://github.com/AHWALab/EF5Docs.git
cd EF5Docs
```

---

### 2. Explore the Documentation Files
All source files for the documentation are located in the source/ folder:

- **source/index.rst:** The main entry point with the table of contents.
- **Other .rst files:** Individual sections of the EF5 User Manual (e.g., source/about.rst, source/water_balance_models.rst).
- **source/conf.py:** Sphinx configuration file.

---

### 3. After Committing
After committing your changes, they should be visible online in a few minutes at:

**https://ef5docs.readthedocs.io/en/latest/index.html**

---

### 4. Install Python and Dependencies (**The below steps are only necessary if you want to build locally and test your changes before committing**)
```bash
pip install sphinx sphinx_rtd_theme sphinx-togglebutton
```
- **sphinx:** Core package for generating the documentation.
- **sphinx_rtd_theme:** The Read the Docs theme for a clean, hierarchical navigation layout.
- **sphinx-togglebutton:** Enables dropdown functionality used in some sections (e.g., "Calibrating the Models").

---

### 5. Test Changes Locally (**optional**)
If you modify the **.rst** files in **source/** and want to preview your changes before committing:

- Edit the files in source/.
- Run the build command (make.bat html).

**This will build the documentation and place the output in the build/html/ folder. Open build/html/index.html in a web browser to view it.**

---
