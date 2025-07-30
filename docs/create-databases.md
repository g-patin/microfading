
In this section, you will learn how to create the databases files. 

Creating databases is an operation that only needs to be performed one time using the `create_DB()` function (see below). Inside a desired folder on your local computer, it will create a few empty files (csv and txt) in which information about microfading projects and objects can be recorded. 

```python
import microfading as mf
```


```python
folder = "Enter a desired folder path as a string"
# e.g: "home/john/Documents/MFT/databases"

mf.create_DB(folder=folder)
```

&nbsp;

## **Databases created ?**

If you want to know whether databases were created, use the `is_DB()` function.

```python
import microfading as mf

# Return True if databases files were created otherwise False
mf.is_DB()

```
<div class="output-area">
<pre>
True
All the databases were created and can be found in the following directory: /home/john/Documents/MFT/databases
</pre>
</div>

&nbsp;

## **Databases location ?**

If you want to know where are the databases files located, use the  `get_config()` function. It will return the information related to databases.

```python
import microfading as mf

# Return the all the information related to databases included the path_folder
mf.get_config(key='databases')
```


<div class="output-area">
<pre>
{'db_name': 'MFT',
 'path_folder': '/home/john/Documents/RCE/databases',
 'usage': True}
</pre>
</div>

