Creating databases is an operation that only needs to be performed one time using the `create_DB()` function (see below). Inside a choosen folder on your local computer, it will create a few empty files (csv and txt) in which information about microfading projects and objects can be recorded. 

```python
import microfading as mf
```


```python
folder = Enter a desired folder path # e.g: "home/john/Documents/MFT/databases"
mf.create_DB(folder=folder)
```

If you want to know whether databases were created or you want to know where are the databases located, use the `folder_DB()` function. It will return the path of the folder where the databases are located.

```python
import microfading as mf
```


```python
mf.folder_DB()
```
