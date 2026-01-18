In this section, we will show you how to process microfading raw files into our standard *interim* files, that are required to use the `microfading` package. To learn more about the types of files used in this package, see the [Datafiles](https://g-patin.github.io/microfading/datafiles/) section.

A summary of this page has been compiled inside a Jupyter notebook and is available for download: [rawdata processing notebook](notebooks/Process_rawfiles.zip).

The current version of the `microfading` package can only process raw files obtained with the Fotonowy microfading device. Please, don't hesitate to contact us to discuss the possibility to process raw files obtained with other microfading systems.

Processing the rawdata files consists of two main steps:

1. Get a list of your raw files
2. Run the `process_rawdata()` function

## Get raw files

There are many ways in python to retrieve a list of files. I will only show two ways of doing it.

**Option 1** - Retrieve files manually

In this option you create a list by typing the names of the raw files. To ease the process, you can start writing the first letter and then press the `Tab` button to autocomplete the rest of the filename. This only works if the notebook is in the same folder as the data files or if you modified the current working directory of the notebook. 

```python
# For example, I created a list of two rawdata files
files = ['Project01_MF.plume01.01_G01_blue_rawdata.txt',
	     'Project12_MF.S0001.01_G01_paperBlock_rawdata.txt']

# If the files are located in a different directory than the notebook you are using,
# then you will need to give the absolute path of the files	     
files = ['/home/john/Documents/data/Project01_MF.plume01.01_G01_blue_rawdata.txt',
	     '/home/john/Documents/data/Project12_MF.S01.01_G01_paperBlock_rawdata.txt']
```

&nbsp;

**Option 2** - Retrieve files with `glob`

The `glob` module allows users to find pathnames according to pattern matching expression that you will provide. The current working directory (cwd) of the notebook should be similar to the folder where your files are located. You can change the cwd of the notebook by using the *cd* command. Then you can invoke the `glob` module as described below, by entering the pattern matching expressions between * *. By default, the recurvise parameter is set to False, but if you set it to True, then the function will also search for files in all the sub-folders of the cwd.


```python
from glob import glob
```

```python
# change the cwd of the notebook if you need to
cd /home/john/Documents/MFT/rawfiles
```

```python
# Ask glob to retrieve all the files containing the expression *MF* and *rawdata* in their filenames
# I also asked to sort the files

files = sorted(glob('*MF*rawdata*'), recursive=False)
files
```

<div class="output-area">
<pre>['/home/john/Documents/data/Project01_MF.plume01.01_G01_blue_rawdata.txt',
'/home/john/Documents/data/Project12_MF.S01.01_G01_paperBlock_rawdata.txt']
</pre>
</div>

Although option 1 is the easiest one, it can be quite time-consuming. For instance, the Fotonowy device currently produces 4 raw files per analysis, which can quickly become a lot of files to individually write. If you are saving all your microfading raw files inside the same folder, you might want to consider creating a sub-folder called "To_process" and copy-paste any analyses that you want to process. To select all the files in this sub-folder you can use the `glob` method as showed below.

```python
# change the cwd of the notebook to the "To_process" folder
cd /home/john/Documents/MFT/rawfiles/To_process
```

```python
all_files = sorted(glob('**'))
```

## Run function

Once you have a list of rawdata files, you will use it in combination with the `process_rawdata()` function as illustrated below. This function has two compulsory arguments (*files* and *device*) for which you will need to provide values. You will use the list of rawfiles for the *files* argument and you will select the adequate microfading device you used (see sub-sections below).

```python
import microfading as mf

# get the raw files (see step above)
files = ['filename1', 'filename2', etc.]

# run the function to process the rawfiles
mf.process_rawdata(files=files, device='<MFT_device_name>')
```

### Fotonowy device

Currently, the Fotonowy device produces 4 raw files for each analysis, thus you will need to enter these 4 files in the list of required raw files.
The list of raw files can contain several analyses. The algorithm will automatically detect that there are more than one analyses, and will thus process them separately. 

For the argument 'device' of the `process_rawdata()` function, you can start by entering 'fotonowy' as a value (see code below).

```python
#### BASIC RAWDATA PROCESSING STEPS ####

# retrieve raw files
rawfiles = .... [see above]

# run the function to process the rawfiles
mf.process_rawdata(files=rawfiles, device='fotonowy')
```

The method showed in the above cell corresponds to the most basic way of processing your raw files. It can be viewed as a 'quick and dirty way' ! This is not the recommended method, but we understand that at first, you might prefer to use such a method. 
 
For a better way to process your raw files, you will need to use the other arguments of the `process_rawdata()` function, for which more information is provided in the following sub-section.


## Function arguments

The `process_rawdata()` function contains several arguments that enable you to process your data in a more rigorous way, more specifically:

- Information about objects and projects will be automatically added.
- Better control over some data processing parameters (rounding, interpolation, wavelength range and step, filenaming, etc.).
- Default behavior to fill in some values.
- Overall data processing more coherent and more repeatable.

To make use of the arguments of the `process_rawdata()` function, you will need to perform the following steps:
 
1. Register your working environment information inside database files (see section [register work-environment info](https://g-patin.github.io/microfading/register-work-environment-info/)). 
 
2. Connect the `microfading` package with the database files previously created (see section [connection with db files](https://g-patin.github.io/microfading/connection-db-files/)). 

3. Set default behavior information (see section [configuration info](https://g-patin.github.io/microfading/configuration-info/)).  


	Steps 1 to 3 only needs to be performed once at the beginning. However, each time you have a new project or a new object on which you will perform microfading analyses, then you will need to register the project or object.  



4. Register a new project (see section [register projects](https://g-patin.github.io/microfading/register-projects/)).

5. Register a new object (see section [register objects](https://g-patin.github.io/microfading/register-objects/)).

---

© 2026 Gauthier Patin. All rights reserved. | Last updated: 2026-01-18



