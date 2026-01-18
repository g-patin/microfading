In this section, you will learn how to register a new project. When it comes to microfading analyses, we are assuming that most of the time, the analyses are performed within a specific context, i.e. a project. It could be a temporary exhibition, a research project, a student internship, etc. 

The information about the new project will be registered in the database files that you created earlier. If you haven't created any database files, please first consult the section on how to [create database files](https://g-patin.github.io/microfading/create-databases/).

You will need to know the name that you chose for your database files. If you forgot it, you can ask for all the database names that you created (see code below).

```python
# material science database package
import msdb

# return all the names of created databases
msdb.get_names()
```

&nbsp;

Afterwards, follow the code displayed below to add a new project. 

```python
# material science database package
import msdb
```

```python
# create a DB class instance
db_name = 'write the name you chose you for your database files'
db = msdb.DB(db_name=db_name)
```

```python
# add a new project
db.add_projects()
```

The last line of code above will return several ipywidgets, inside which you will be able to insert the required information about the project. The values for the institutions, project leader, co-researchers, and methods will appear automatically if you first had registered them (see code below). 

```python
import msdb
```

```python
# create a DB class instance
db_name = 'write the name you chose you for your database files'
db = msdb.DB(db_name=db_name)
```

```python
# add a new institution
db.add_institutions()
```
```python
# add a new user (project leader, co-researchers)
db.add_users()
```
```python
# add a new analytical method
db.add_methods()
```

