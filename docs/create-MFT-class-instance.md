The functions provided by the microfading package only work on an instance of a microfading test class (MFT). The creation of an instance of a microfading class is a two-steps procedure and is described below:

1. Retrieve a list of data files on which the functions provided by the class will be applied. The data files need to be constrained to a specific file structure (For more information about it, see the [data files section](https://g-patin.github.io/microfading/datafiles)).

```python
>>> import microfading as mf
```
```python
# Here we are using the test data, but you should use your own data files
>>> files = mf.get_datasets()
```

2. Create the instance using the files as the main parameter.

```python
>>> mf_data = mf.MFT(files=files)
>>> mf_data
Microfading data class - Number of files = 5
```


