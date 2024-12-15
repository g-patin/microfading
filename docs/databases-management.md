The microfading package gives you the possibility to implement databases where the information related to the objects and projects can be stored. The main advantage of having databases is to connect metadata to the analytical data when processing raw files. 

This section implies that you have created the database files. If that is not the case, look at the section on how to [create empty databases](https://g-patin.github.io/microfading/create-databases/).

The microfading packages contains several functions to manage the databases:

- Get functions: retrieve information contains in the databases
- Add functions: add a new item in the databases
- Update functions: modify the recording parameters of the databases


## Get functions

There are 5 get functions:

- **get_path_DB()** : returns the absolute path where the databases are stored on your local computer
- **get_DB()** : returns the databases as pandas dataframes
- **get creators()** : returns a list of names and surnames corresponding to the persons that created the microfaded objects.
- **get_institutions()** : returns a list of institutions that own the microfaded objects.
- **get_persons()** : returns a list of persons that performed the microfading analyses.


## Add a new project

```python
import microfading as mf
```


```python
mf.add_new_project()
```


    HBox(children=(VBox(children=(HBox(children=(VBox(children=(Text(value='', description='Project Id', layout=La…



    HBox(children=(Button(description='Create record', style=ButtonStyle(), tooltip='Click me'), Output()))


```python
mf.add_new_project()
```

## Add a new object


## Add a new person


## Update project parameters


## Update object parameters

