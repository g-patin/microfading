Creating databases is an operation that only needs to be performed one time using the `create_DB()` function (see below). Inside a choosen folder on your local computer, it will create a few empty files (csv and txt) in which information about microfading projects and objects can be recorded. 

```python
import microfading as mf
```


```python
folder = Enter a desired folder path as a string
# e.g: "home/john/Documents/MFT/databases"

mf.create_DB(folder=folder)
```

&nbsp;

## **Databases created ?**

If you want to know whether databases were created, use the `DB()` function.

```python
import microfading as mf

# Return True if databases files were created otherwise False
mf.DB()

```
<div class="output-area">
<pre>
True
All the databases were created and can be found in the following directory: /home/john/Documents/MFT/databases
</pre>
</div>

&nbsp;

## **Databases location ?**

If you want to know where are the databases files located, use the  `get_path_DB()` function. It will return the path of the folder where the databases are located.

```python
import microfading as mf

# Return the path were the databases files are located if any.
mf.get_path_DB()
```

```
<div class="output-area">
<pre>
The databases are located in the folder: /home/john/Documents/MFT/databases
</pre>
</div>

