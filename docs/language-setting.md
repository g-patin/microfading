
The language setting is only relevant when processing microfading raw files using the `process_rawdata()` function. Inside the later function, there is a parameter called *language* and for which you can provide the language setting information about the computer that was used to perform the microfading analyses. Selecting the adequate language setting enables the algorithm to correctly parse the datetime information given in the microfading raw files. By default, the algorithm assumes that English was used for the language setting of the computer. If this is not the case, you will need to select another language setting, which will slightly be different according to the operating system of the computer used to perform the measurements (Windows, Linux, or Mac OS).



# Fotonowy raw files

When you open the .txt file (the one containing the CIE colorimetric values) provided by Fotonowy, the first line provides information about the date and time of the analysis (see image below). The software of Fotonowy directly retrieve this information from the computer that was used to perform the analysis. According to the language configuration of the computer, the date and time will be formated differently. Therefore, when the algorithm of the `microfading` package read this file and try to parse the date and time information, it will need to know the language settings, so that it can adequately determine the information 

![Alt text](images/mf_fotonowy_rawfiles.png){: .img-large align=left }
/// caption
Details of a microfading Fotonowy raw files
///

**Windows OS**

If you used a Windows OS computer to perform the analyses, you can use one of the following language abbreviations that corresponds to your computer language (non-exhaustive list) : 'en', 'fr', 'it', 'nl', 'de', 'es' (See code below for an example).

```python
import microfading as mf
```

```python
# a list of strings corresponding to the absolute paths of the raw files on your local computer
rawfiles = ['...'] 

# you can also enter the device ID if you registered your MFT device
device = 'Fotonowy'

language = 'it'

mf.process_rawfiles(files=rawfiles, device=device, language=language)
```

**Linux OS**

If you used a Linux OS computer to perform the analyses, you cannot simply type the abbreviations of the language, like for Windows OS. You will need to retrieve the correct language setting. For that, open a terminal, and type the command *localectl status* (see figure below). The language setting information is provided on the first line, after the expression *LANG=*. In my case, it is *en_US.UTF-8*, and this is what I will need to enter as value in `process_rawdata()` function. 

![Alt text](images/mf_language-setting_terminal.png){: .img-large align=left }
/// caption
Get the language setting information on Ubuntu.
///


For the curious people, you can open the process_rawfiles.py inside the microfading package and search for the expression "analysis datetime". It will show you where and how the language setting is used. You will see that it is used inside a function called "parse_datetime" which is written at the beginning of the process_rawfiles.py file.



