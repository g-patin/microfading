In this section, you will learn how to generate report about microfading measurements. A report consists of an A4-format document in which the main results are displayed. There are three types of report:

1. **single** report. Display the results of a single interim analysis.

2. **object** report. [NOT AVAILABLE FOR NOW] Display the results for a group of interim analyses that were performed on the same object.

3. **project** report. [NOT AVAILABLE FOR NOW] Display an overview of the results for a whole project which show the results for all the objects analyzed during the project.


As you usually, the first step is to select the microfading files and to create an instance of the MFT class. Afterwards you can create the report by using the function called `make_report`.

```python
import microfading as mf
```

```python
# Here we are using the test data, but you should use your own data files
files = mf.get_datasets()

# We create the MFT class instance
m = mf.MFT(files=files)

# We create the report
folder_figures = "/home/username/Documents/MFT/figures"  # to be replaced with your actual path for the folder figures of your MFT data
m.make_report(folder_figures=folder_figures) 
```

## 1. **Function make_report()**

The function `make_report` has 4 parameters. The first parameter (*folder_figures*) is compulsory while the remaining ones are optional:

- *folder_figures*: it refers to the path of the folder on your local computer where the algorithm will look for the figures that will be displayed in the report.
- *folder_report*: it refers to the absolute filename of the report. It allows you to choose the name of the report and in which folder it should be saved. By default, the algorithm saves the report in the current working directory.
- *type*: The type of report to be created ('single', 'object', or 'project').
- *authors*: Person(s) that created the report. If you registered the initials of persons in the databases, you can use these initials otherwise you can enter the name(s) inside a string.

## 2. **Single report**

The single report contains four figures that we will need to be created and saved in the *folder_figures* that you will pass in as argument in the `make_report` function. When creating the figures, set the *report* parameter to True. It will add the word 'report' to the filename, which is how the `make_report` function is able to retrieve the appropriate figures in the *folder_figures*.

1. CIELAB plot

2. SP plot

3. Delta plot

4. Colour swatches circle plot




