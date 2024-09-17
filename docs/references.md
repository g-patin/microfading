## Commands

### Datasets

* `get_datasets [rawfiles, BWS, stdev]` - Retrieve examples of data files.

### Databases management

* `create_DB [folder]` - Create two empty databases (projects and objects).
* `get_DB [db]` - Retrieve the databases.
* `folder_DB` - Retrieve the folder where the databases are stored.
* `add_new_project` - Add a new project to the database.
* `add_new_object` - Add a new object to the database.
* `update_DB_project [new, old]` - Modify or add a new parameter to the project database.
* `update_DB_object [new, old]` - Modify or add a new parameter to the object database.

### Data processing

* `process_rawdata [files, device]` - Process rawdata files into interim files.

### MFT class

* `data_points` - Select colourimetric values for one or multiple light dose values.

::: microfading.microfading
    rendering:
      show_root_heading: true
      show_source: true
