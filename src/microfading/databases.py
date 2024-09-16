import pandas as pd
from pathlib import Path
from typing import Optional
import json
import os
from ipywidgets import Layout
import ipywidgets as ipw
from IPython.display import display, clear_output

style = {"description_width": "initial"}


class DB:
    def __init__(self, config_file=Path(__file__).parent / 'db_config.json') -> None:
        self.config_file =  config_file
        self.folder_db = Path(self.load_folder_db())


    def add_new_project(self):

        db_projects = self.get_db(db='projects')
        existing_columns = list(db_projects.columns)

        # Define the ipython widgets
        project_Id = ipw.Text(        
            value='',
            placeholder='Type something',
            description='Project Id',
            disabled=False,
            layout=Layout(width="95%", height="30px"),
            style=style,   
        )

        institution = ipw.Combobox(
            placeholder = 'Enter an institution',
            options = [],  #institutions_list,
            description = 'Institution',
            ensure_option=False,
            disabled=False,
            layout=Layout(width="95%", height="30px"),
            style=style,
        )
        
        startDate = ipw.DatePicker(
            description='Start date',
            disabled=False,
            layout=Layout(width="90%", height="30px"),
            style=style,
        )

        endDate = ipw.DatePicker(
            description='End date',
            disabled=False,
            layout=Layout(width="90%", height="30px"),
            style=style,
        )

        PL = ipw.Dropdown(
            options=['A','B'],
            value='A',
            description='Project leader',
            disabled=False,
            layout=Layout(width="90%", height="30px"),
            style=style,
        )
        

        recording = ipw.Button(
            description='Create record',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click me',
            #layout=Layout(width="50%", height="30px"),
            #style=style,
            #icon='check' # (FontAwesome names without the `fa-` prefix)
        )
        

        project_keyword = ipw.Text(
            placeholder = 'Describe project in 1 or 2 words',
            description = 'Project keywords',
            disabled = False,
            layout=Layout(width="95%", height="40px"),
            style = style,
        )

        # Combobox for additional parameters (if any)
        additional_params = [col for col in existing_columns if col not in ['project_id', 'institution', 'start_date', 'end_date', 'project_leader', 'keywords']]
        additional_param_widgets = {}
        for param in additional_params:
            additional_param_widgets[param] = ipw.Combobox(
                description=param,
                options=[],  # You can populate this with options if needed
                placeholder=f"Enter {param} value"
            )

        button_record_output = ipw.Output()


        def button_record_pressed(b):
            """
            Save the project info in the project database file (DB_projects.csv).
            """

            with button_record_output:
                button_record_output.clear_output(wait=True)

                Projects_DB_file = self.folder_db / 'DB_projects.csv'
                Projects_DB = pd.read_csv(Projects_DB_file)        

                new_row = pd.DataFrame({'project_id':project_Id.value,
                        'institution':institution.value, 
                        'start_date':startDate.value, 
                        'end_date':endDate.value,
                        'project_leader':PL.value,                        
                        'keywords':project_keyword.value},                       
                        index=[0] 
                        )  
                '''         
                institutions_list = list(institution.options)
                
                if institution.value not in institutions_list:                       
                    institutions_list.append(str(institution.value))         
                    institutions_list = sorted(institutions_list)

                    with open(self.folder_db / r'Institutions.txt', 'w') as f:
                        f.write('\n'.join(institutions_list))

                    f.close()
                '''

                # Add additional parameters to the new record
                for param, widget in additional_param_widgets.items():
                    new_row[param] = widget.value

                Projects_DB_new = pd.concat([Projects_DB, new_row],)
                Projects_DB_new.to_csv(Projects_DB_file, index= False)
                print(f'Project {project_Id.value} added to database.')

        recording.on_click(button_record_pressed)


        # Display the widgets
        display(ipw.HBox([
            ipw.VBox([
                ipw.HBox([
                    ipw.VBox([project_Id,institution, project_keyword],layout=Layout(width="60%", height="95%")),
                    ipw.VBox([startDate,endDate, PL],layout=Layout(width="60%", height="95%")),
                    ]),                
                ], layout=Layout(width="50%", height="100%")),                        
            ], layout=Layout(width="100%", height="110%"))
        ) 

        display(*[widget for widget in additional_param_widgets.values()])
        display(ipw.HBox([recording, button_record_output]))


    def create_db(self, folder_path):

        self.folder_db = folder_path
        self.save_folder_db(folder_path)

        # create the project database
        db_project = pd.DataFrame(columns=['project_id','institution','start_date','end_date','project_leader','keywords'])
        db_project.to_csv(Path(folder_path) / 'DB_projects.csv', index=False)

        # create the object database
        db_object = pd.DataFrame(columns=['object_id','object_category','object_type','object_technique','object_title','object_name','object_creator','object_date','object_owner','object_support','colorants','colorants_name','binding','ratio','thickness_um','color','status','project_id'])
        db_object.to_csv(Path(folder_path) / 'DB_objects.csv', index=False)

        print(f'DB_projects.csv and DB_objects.csv created in the following folder: {folder_path}')


    def save_folder_db(self, folder_path):
        # Save folder path in a JSON file
        with open(self.config_file, 'w') as file:
            json.dump({"folder_db": folder_path}, file)


    def load_folder_db(self):
        # Load folder path from JSON file if it exists
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                config = json.load(file)
                return config.get("folder_db")
        return None
    

    def get_db(self, db:Optional[str] = 'all'):

        if (Path(self.folder_db) / 'DB_projects.csv').exists():
            db_projects = pd.read_csv(Path(self.folder_db) / 'DB_projects.csv')
        else:
            print(f'The DB_projects.csv file is not existing. Make sure to create one by running the function "create_DB" from the microfading package.')
            return
        
        if (Path(self.folder_db) / 'DB_objects.csv').exists():        
            db_objects = pd.read_csv(Path(self.folder_db) / 'DB_objects.csv')
        else:
            print(f'The DB_objects.csv file is not existing. Make sure to create one by running the function "create_DB" from the microfading package.')
            return

        if db == 'all':
            return db_projects, db_objects
        
        elif db == 'projects':
            return db_projects
        
        elif db == 'objects':
            return db_objects
        



    def update_db_projects(self, new: str, old:Optional[str] = None):

        if (Path(self.folder_db) / 'DB_projects.csv').exists():
            print('dddd')

        else:
            print('No databases have been created yet.')
            


    def update_db_objects(self, new: str, old:Optional[str] = None):

        if (Path(self.folder_db) / 'DB_objects.csv').exists():
            print('dddd')

        else:
            print('No databases have been created yet.')
