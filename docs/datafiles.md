
## Files types

The `microfading` package aims to facilitate the manipulation of microfading data. Consequently, data files play a central role in the package, for which we applied the following typology for our files (we simply re-used the structure from [Cookiecutter data science](https://cookiecutter-data-science.drivendata.org/)):

1. **Raw files**: the files that are produced by the software of microfading devices when performing analyses. 

2. **Interim files**: standardized Excel or OpenDocument files created by the `microfading` package from the raw files previously mentioned.

3. **Processed files**: modified interim files tailored according to specific research needs. Currently, the package only proposed the average of several interim files as processed files. But you can definitely modified yourself the interim files, by adding new columns or modifying the existing data.

Our conception of the structure related to scientific data and files can be viewed as a tree or an hourglass shape. At the bottom, there are multiple roots. Each root can be viewed as a device that produces its own raw files with a specific structure inside the files. It is very common in laboratory, to have different devices that are doing similar analyses. For example, several microfading devices were developed over the past decaded. Each device creates its own specfic rawfiles that are usually very different from one device to another. Comparing the data from these various raw files can be quite tidious. One solution is to convert each raw file into a unique file format, which is the method that has been chosen in this package. This unique file format corresponds to the above-mentioned *interim* file. Therefore, first step of our package is to convert raw files into *interim* files, so that whatever the microfading device you used to perform your analyses, the *interim* file will always have a similar structure. This is what makes the `microfading` functional because it expects a given structure that makes it easy to retrieve data or perform further computational processes. Above the *interim* files are the *processed* files. Their structure can be different and be specific according to the projects, the research questions, etc. This is where data and files gain in flexibility so that it can adequately fullfill the needs and objectives of each project.


## Interim files

An *interim* file is simply an Excel or an OpenDocument file with a specific inner structure to organize the data. Each *interim* file is composed of three sheets:

1. **info** : it contains the metadata related to the measurements, the object, and the project
2. **CIELAB** : it contains the colorimetric values
3. **spectra** : it contains the spectral values

An example of an *interim* file can be found in the microfading package [(section Retrieve test datasets)](https://g-patin.github.io/microfading/retrieve-test-datasets/). As an illustration of the content of *interim* files, the picture below shows the CIELAB sheet of an *interim* file. The first three rows on the left are related to the light dose energy, while the other columns show various colorimetric units. The value *nominal*, that you can see inside *interim* file, corresponds to the data types, for which more information is provided below.

![Alt text](images/mf_interim-file_CIELAB-sheet.png){: .img-large align=left }
/// caption
CIELAB sheet of a microfading interim file.
///

If you prefer to use the functionalities provided by Excel or OpenDocument, you can always create a new sheet inside an *interim* file to perform more calculations or create figures. I would not recommend to delete the existing columns or rows inside the first three sheets (info, CIELAB, spectra), or to create figures inside them. This might lead to some issues with the functions of the `microfading` package, and thus preventing its use.

## Data types

We defined three types of numerical data in the package:

1. **nominal**: a single value directly obtained a single measurement.

2. **mean**: a value obtained by averaging several nominal values.

3. **std**: a value corresponding to the standard deviation value of several nominal values.

**Mean** and **std** values will be encountered when asking the package to compute the average of several *interim* files (see section [Compute average values](https://g-patin.github.io/microfading/compute-average/)).

---

© 2026 Gauthier Patin. All rights reserved. | Last updated: 2026-01-18

