In this section, we will show you how to process raw microfading files into our standard *interim* files, that is required to use the `microfading` package.

The current version of the `microfading` package can only process raw files obtained with the Fotonowy microfading device. Don't hesitate to contact us to discuss the possibility to process raw files obtained with other microfading systems.

## Fotonowy raw files

Although by most devices, the  data can be exported to an open file format (txt, csv, etc.), the microfading raw files produced by each microfading devices are often difficult read. These files often prioritize efficiency or size at the expense of readability. Which is why, it was decided to create a specific file structure where information and data could easily be found. 


```python
import microfading as mf
```


```python
# Here we use the raw files fom the microfading package, but ideally you should use your own raw files.
rawfiles = mf.get_datasets(MFT='fotonowy', rawfiles=True)
mf.process_rawdata
