If you decide to implement databases when using the `microfading` package, you will first need to [create empty databases](https://g-patin.github.io/microfading/create-databases/).


Setting up databases is an operation that only need to be performed one time. Inside a choosen folder on your local computer, it will create a few empty files (csv and txt) in which information about microfading projects and objects can be recorded. 

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
