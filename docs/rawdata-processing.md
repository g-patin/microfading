In this section, we will show you how to process raw microfading files into our standard *interim* files, that are required to use the `microfading` package. 

A summary of this page has been compiled inside a Jupyter notebook and is available for download: [Download notebook](notebooks/Process_rawfiles.zip)

The current version of the `microfading` package can only process raw files obtained with the Fotonowy microfading device. Don't hesitate to contact us to discuss the possibility to process raw files obtained with other microfading systems.

Processing the rawdata files consists of two main steps:

1. Get a list of your raw files
2. Run the `process_rawdata()` function

## Get raw files

There are many ways in python to retrieve a list of files. I will only show two ways of doing it.

**Option 1** - Retrieve the files manually

In this option you create a list by typing the names of the raw files. To ease the process, you can start writing the first letter and then press the `Tab` button to autocomplete the rest of the filename. This only works if the notebooks is in the same folder as the data files or if you modified the current working directory of the notebook. 

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

**Option 2** - Retrieve with `glob`

```python
from glob import glob

# Ask glob to retrieve all the files containing the expression *MF* and *rawdata* in their filenames
# I also asked to sort the files
files = sorted(glob('*MF*rawdata*'))
files
```

<div class="output-area">
<pre>['/home/john/Documents/data/Project01_MF.plume01.01_G01_blue_rawdata.txt',
'/home/john/Documents/data/Project12_MF.S01.01_G01_paperBlock_rawdata.txt']
</pre>
</div>

Although option 1 is the easiest one, it can be quite time-consuming. For instance, the Fotonowy device currently produces 4 raw files per analysis, which can quickly become a lot of files to individually write. If you are saving all your microfading raw files inside the same folder, you might want to consider creating a sub-folder called "To_process" and copy-paste any analyses that you want to process. To select all the files in this sub-folder you can use the `glob` method as showed below.

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

For the argument 'device' of the `process_rawdata()` function, you can start by entering 'fotonowy' as value (see code below).

```python
#### BASIC RAWDATA PROCESSING STEPS ####

# retrieve raw files
rawfiles = .... [see above]

# run the function to process the rawfiles
mf.process_rawdata(files=rawfiles, device='fotonowy')
```

The method showed in the above cell corresponds to the most basic way of processing your raw files. It can be viewed as a 'quick and dirty way' ! This is not the recommended method, but we understand that at first, you might prefer to use such a method. 
 
For a better way to process your raw files, you will need to use the other arguments of the `process_rawdata()` function for which more information is provided in the following sub-section.


## Function arguments

The `process_rawdata()` function contains several arguments that enable you to process your data in a more rigorous way. I will let you read the docstrings for detailed information. But I will just focus on two parameters that you might find important to be aware of. 




