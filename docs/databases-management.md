The microfading package gives you the possibility to implement databases where the information related to the objects and projects can be stored. The main advantage of having databases is to connect metadata to the analytical data when processing raw files. 

This section implies that you have created the database files. If that is not the case, look at the section on how to [create empty databases](https://g-patin.github.io/microfading/create-databases/). If you want to know whether databases were already created, use the following function:

```python
import microfading as mf
```

```python
mf.DB()
```
<div class="output-area">
<pre>
All the databases were created and can be found in the following directory: /home/john/Documents/MFT/databases
</pre>
</div>

&nbsp;

The microfading packages contains several functions to manage the databases:

- **Get functions**: retrieve information contains in the databases
- **Add or register functions**: add a new item in the databases
- **Update functions**: modify the recorded parameters of the databases


## **Get functions**

There are eight *get* functions:

- `get_path_DB()` : returns the absolute path where the databases are stored on your local computer
- `get_DB()` : returns the databases as pandas dataframes
- `get creators()` : returns a list of names and surnames corresponding to the persons that created the microfaded objects.
- `get_institutions()` : returns a list of institutions that own the microfaded objects.
- `get_objects()` : returns a list of the microfaded objects
- `get_persons()` : returns a list of persons that performed the microfading analyses.
- `get_devices()` : returns a list of the registered microfading devices.
- `get_white_references()` : returns a list of the registered white standard references.

## **Add/Register functions**

There are seven *add/register* functions:

- `add_new_creator()` : record information about a new object creator (artist, institution, etc.).
- `add_new_institution()` : record information about a new institution.
- `add_new_object()` : record information about a new object.
- `add_new_person()` : record information about a new person performing microfading measurements.
- `add_new_project()` : record information about a new project.
- `register_devices()` : register a new microfading device.
- `register_references()` : register a new white standard reference.

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

### Add a new object




## **Update functions**

There are two *update* functions:

- `update_DB_objects()` : add new categories to the objects database.
- `update_DB_projects()` : add new categories to the projects database.

### Update project parameters


### Update object parameters

