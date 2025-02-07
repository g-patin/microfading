In this section, you will learn how to use the databases that come along with the `microfading` package and inside which you have the possibility to store information. The main purpose of the databases is to connect the metadata with the analytical data. Additionally, the databases will allow you to conveniently reuse information and will also enable you to perform queries based on the information stored in the databases. For example, one could retrieve all the data obtained on paintings created by a given artist. 


This section implies that you have created the database files. If that is not the case, look at the section on how to [create empty databases](https://g-patin.github.io/microfading/create-databases/). If you want to know whether databases were already created, use the following function:

```python
import microfading as mf

# Check whether databases were created.
mf.DB()
```

<div class="output-area">
<pre>
True
All the databases were created and can be found in the following directory: /home/john/Documents/MFT/databases
</pre>
</div>

&nbsp;

## **Description**

The databases simply consists of csv and txt files in which you will accumulate information. The management of the databases lies around two main actions:

1. You want to learn how to **add / remove info**.
2. You want to learn how to **retrieve info** when needed. 

The first things to do is to import the microfading package as showed in the code box above. You will access the databases functions as followed:

```python
mf.<function name>

# for example, this will retrieve all the microfading devices that you registered. 
mf.get_devices()
```

Every function name start with a verb followed by an underscore and a noun or an adjective providing more information on the action that will be performed. There are only 4 verbs:

- **Get functions**: retrieve information contains in the databases
- **Add functions**: add a new item in the databases
- **Update functions**: modify the recorded parameters of the databases
- **Set functions**: set default values for some key parameters

&nbsp;

## **Get functions**

There are ten *get* functions:

- `get_path_DB()` : returns the absolute path where the databases are stored on your local computer.
- `get_DB()` : returns the databases as pandas dataframes.
- `get_colorimetric_info()` : returns the observer and illuminant default values.
- `get creators()` : returns a list of names and surnames corresponding to the persons that created the microfaded objects.
- `get_institutions()` : returns a list of institutions that own the microfaded objects.
- `get_lighting_conditions()` : returns the default light exposure conditions default values.
- `get_objects()` : returns a list of the microfaded objects.
- `get_persons()` : returns a list of persons that performed the microfading analyses.
- `get_devices()` : returns a list of the registered microfading devices.
- `get_white_references()` : returns a list of the registered white standard references.

## **Add/Register functions**

There are seven *add* functions:

- `add_new_creator()` : record information about a new object creator (artist, institution, etc.).
- `add_new_institution()` : record information about a new institution.
- `add_new_object()` : record information about a new object.
- `add_new_person()` : record information about a new person performing microfading measurements.
- `add_new_project()` : record information about a new project.
- `add_devices()` : register a new microfading device.
- `add_references()` : register a new white standard reference.


## **Add/Register functions**

There are two *set* functions:

- `set_colorimetric_info()` : set the observer and illuminant default values
- `set_lighting_conditions()` : set the light exposure conditions default values


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

