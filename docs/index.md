# Welcome !

Welcome on the documentation website of the microfading python package.

This package aims to facilitate the manipulation of microfading data. Consequently, microfading data - provided by the users - play a central role in the package. Like in most analytical techniques, several microfading devices have been developed over the years. Each device produces its own specfic rawfiles - containing the measurement data - that are usually very different from one device to another. To compare the results obtained with different devices, one solution is to convert each rawfile into a unique file format, which is the method has been chosen in this package. 

This unique file format, called interim file, is simply an excel file with a specific inner structure to organize the data. Each excel file is composed of three sheets:

1. **info** : it contains all the metadata related to the measurements, the object, and the project
2. **CIELAB** : it contains all the colorimetric values
3. **spectra** : it contains all the spectral values

An exemple of an interim file can be found in the microfading package [(get_datasets() function)](https://g-patin.github.io/microfading/how-to-guides/).

The overall landscape of the package can be viewed as a tree or an hourglass shape. 

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
