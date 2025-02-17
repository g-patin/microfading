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
        try:      
            self.folder_db = Path(self.get_db_path())
        except TypeError:                       
            self.folder_db = 'path_folder'
               

    def add_new_creator(self):
        """Record a new object creator in the object_creators.txt file
        """

        # Function to update the text file if the initials are unique
        def update_text_file(file_path, name, surname):            
            
            
            df_creators = self.get_creators()
            df_creators = pd.concat([df_creators, pd.DataFrame(data=[name,surname], index=['name','surname']).T])
            df_creators = df_creators.sort_values(by='surname')
            df_creators.to_csv(self.folder_db/'object_creators.txt',index=False)
               
            print(f"Added: {surname}, {name}")

        # Define ipython widgets
        name_widget = ipw.Text(        
            value='',
            placeholder='Enter a name (optional)',
            description='Name',               
        )

        surname_widget = ipw.Text(        
            value='',
            placeholder='Enter a surname',
            description='Surname',             
        )

        recording = ipw.Button(
            description='Create record',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click me',            
        )        
        

        button_record_output = ipw.Output()

        def button_record_pressed(b):
            """
            Save the creator info in the objet_creators.txt file.
            """

            button_record_output.clear_output(wait=True)

            name = name_widget.value.strip()
            surname = surname_widget.value.strip()

            with button_record_output:

                if surname: # ensure the surname field is complete
                    update_text_file(self.folder_db / 'object_creators.txt', name, surname)
                else:
                    
                    print("Please enter at least a surname.")


        recording.on_click(button_record_pressed)

        display(surname_widget,name_widget)
        display(ipw.HBox([recording, button_record_output]))


    def add_new_institution(self):        
        """Record a new institution in the insitutions.txt file
        """

        # Function to get the existing initials from the file
        def get_existing_acronyms(file_path):
            try:
                df_institutions = self.get_institutions()
                existing_acronyms = df_institutions['acronym']                
                return existing_acronyms
            except FileNotFoundError:
                # If the file does not exist, return an empty set
                return set()
            
        # Function to update the text file if the initials are unique
        def update_text_file(file_path, name, acronym):
            # Check if the acronym already exists
            existing_acronyms = get_existing_acronyms(file_path)
            
            if acronym in existing_acronyms:
                print(f"Acronym '{acronym}' already exists. Please use a different acronym.")
            else:
                df_institutions = self.get_institutions()
                df_institutions = pd.concat([df_institutions, pd.DataFrame(data=[name,acronym], index=['name','acronym']).T])
                df_institutions = df_institutions.sort_values(by='name')
                df_institutions.to_csv(self.folder_db/'institutions.txt',index=False)
               
                print(f"Added: {name} : {acronym}")

        # Define ipython widgets
        name_widget = ipw.Text(        
            value='',
            placeholder='Enter a name',
            description='Name',               
        )

        acronym_widget = ipw.Text(        
            value='',
            placeholder='Enter an acronym',
            description='Acronym',             
        )

        recording = ipw.Button(
            description='Create record',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click me',            
        )

        button_record_output = ipw.Output()

        def button_record_pressed(b):
            """
            Save the person info in the persons.txt file.
            """

            button_record_output.clear_output(wait=True)

            name = name_widget.value.strip()            
            acronym = acronym_widget.value.strip()

            with button_record_output:

                if name and acronym: # ensure all fields are filled
                    update_text_file(self.folder_db / 'institutions.txt', name, acronym)
                else:
                    
                    print("Please enter all fields (Name, Acronym)")

        recording.on_click(button_record_pressed)

        display(name_widget,acronym_widget)
        display(ipw.HBox([recording, button_record_output]))       
    
    
    def add_new_object(self):
        """Add a new object in the DB_objects.csv file"""

        db_projects = self.get_db(db='projects')
        projects_list = ['noProject'] + list(db_projects['project_id'].values)

        db_objects = self.get_db(db='objects')
        existing_columns = list(db_objects.columns)

        creators_file = pd.read_csv(self.folder_db / 'object_creators.txt')
        creators = [f'{x[0]}, {x[1]}' if isinstance(x[1],str) else x[0] for x in creators_file.values]
        
        types_file = open(self.folder_db / r'object_types.txt', 'r').read()
        types = types_file.split("\n")        

        techniques_file = open(self.folder_db / r'object_techniques.txt', 'r').read()
        techniques = techniques_file.split("\n")        

        supports_file = open(self.folder_db  / r'object_supports.txt', 'r').read()
        supports = supports_file.split("\n")        

        owners_file = pd.read_csv(self.folder_db / 'institutions.txt')
        owners = tuple(owners_file['name'].values)
               

        # Define ipython widgets

        project_id = ipw.Combobox(
            #value = ' ',
            placeholder='Project',
            options = projects_list,
            description = 'Project id',
            ensure_option=False,
            disabled=False,
            layout=Layout(width="99%", height="30px"),
            style=style,
        )

        object_id = ipw.Text(        
            value='',
            placeholder='Inv. N°',
            description='Id',
            disabled=False,
            layout=Layout(width="99%", height="30px"),
            style=style,   
        )

        object_category = ipw.Dropdown(
            options=['heritage','model','reference','sample'],
            value='heritage',
            description='Category',
            disabled=False,
            layout=Layout(width="99%", height="30px"),
            style=style,
        )    

        object_creator = ipw.Combobox(
            placeholder = 'Surname, Name',
            options = creators,
            description = 'Creator',
            ensure_option=False,
            disabled=False,
            layout=Layout(width="99%", height="30px"),
            style=style,
        ) 

        object_date = ipw.Text(
            value='',
            placeholder='Enter a date',
            description='Date',
            disabled=False,
            layout=Layout(width="99%", height="30px"),
            style=style,         
        )  

        object_owner = ipw.Combobox(
            placeholder = 'Enter an institution/owner',
            options = owners,
            description = 'Object owner',
            ensure_option = False,
            disabled = False,
            layout=Layout(width='99%',height="30px"),
            style = style

        )

        object_title = ipw.Textarea(        
            value='',
            placeholder='Enter the title',
            description='Title',
            disabled=False,
            layout=Layout(width='99%',height="100%"),
            style=style,   
        )  

        object_name = ipw.Text(        
            value='',
            placeholder='Enter a short object name without space',
            description='Name',
            disabled=False,
            layout=Layout(width='99%',height="30px"),
            style=style,   
        )

        object_type = ipw.Combobox(
            placeholder = 'General classification',
            options = types,
            description = 'Type',
            ensure_option=False,
            disabled=False,
            layout=Layout(width="99%", height="30px"),
            style=style,
        )

        object_technique = ipw.SelectMultiple(
            placeholder = 'Enter techniques/materials',
            options = techniques,
            description = 'Technique',
            ensure_option=False,
            disabled=False,
            layout=Layout(width="99%", height="160px"),
            style=style,
        )   

        object_support = ipw.Combobox(
            placeholder = 'Enter a material',
            options = supports,
            description = 'Support',
            ensure_option=False,
            disabled=False,
            layout=Layout(width="99%", height="30px"),
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
        

        button_record_output = ipw.Output()       
    

        object_color = ipw.Combobox(
            description = 'Color',
            placeholder = 'Optional',
            ensure_option=False,
            disabled=False,
            layout=Layout(width="99%", height="30px"),
            style=style,
        )        
                
        # Combobox for additional parameters (if any)
        additional_params = [col for col in existing_columns if col not in [
            'project_id',
            'object_id',
            'object_category',
            'object_type',
            'object_technique',
            'object_title',
            'object_name',
            'object_creator',
            'object_date',
            'object_owner',
            'object_support']]

        additional_param_widgets = {}
        for param in additional_params:
            additional_param_widgets[param] = ipw.Combobox(
                description=param,
                options=[],  # You can populate this with options if needed
                placeholder=f"Enter {param} value"
            )        


        def button_record_pressed(b):
            """
            Save the object info in the object database file (DB_objects.csv).
            """

            with button_record_output:
                button_record_output.clear_output(wait=True)

                db_objects_file = self.folder_db / 'DB_objects.csv'
                db_objects = pd.read_csv(db_objects_file)            
                                
                creators = [f'{x[0]}, {x[1]}' if isinstance(x[1],str) else x[0] for x in self.get_creators().values]

                owners_file = open(self.folder_db  / r'institutions.txt', 'r').read().splitlines()
                owners = owners_file             

                types_file = open(self.folder_db / r'object_types.txt', 'r').read().splitlines()
                types = types_file       

                techniques_file = open(self.folder_db / r'object_techniques.txt', 'r').read().splitlines()
                techniques = techniques_file        

                supports_file = open(self.folder_db  / r'object_supports.txt', 'r').read().splitlines()
                supports = supports_file                        

                new_row = pd.DataFrame({                    
                    'project_id': project_id.value,
                    'object_id' : object_id.value,                   
                    'object_category': object_category.value, 
                    'object_type': object_type.value, 
                    "object_technique": "_".join(object_technique.value),
                    "object_title": object_title.value,
                    'object_name': object_name.value,
                    'object_creator': object_creator.value,                        
                    'object_date': object_date.value,
                    'object_owner': object_owner.value,
                    'object_support': object_support.value},                       
                    index=[0] 
                    ) 


                if object_creator.value not in creators:                    

                    creator_surname = object_creator.value.split(',')[0].strip()
                    try:
                        creator_name = object_creator.value.split(',')[1].strip()
                    except IndexError:
                        creator_name = ''
                    
                    df_creators = pd.read_csv(self.folder_db / 'object_creators.txt')
                    df_creators = pd.concat([df_creators, pd.DataFrame(data=[creator_surname,creator_name], index=['surname','name']).T])
                    df_creators.to_csv(self.folder_db / 'object_creators.txt', index=False)
                

                
                if object_support.value not in supports:
                    supports.append(str(object_support.value))
                    supports = sorted(supports, key=str.casefold)                    

                    with open(self.folder_db / 'object_supports.txt', 'w') as f:
                        f.write('\n'.join(supports).strip()) 
                    f.close()

                if object_type.value not in types:
                    types.append(str(object_type.value))
                    types = sorted(types, key=str.casefold)

                    with open(self.folder_db / 'object_types.txt', 'w') as f:
                        f.write('\n'.join(types).strip())
                    f.close()                                 
                

                # Add additional parameters to the new record
                for param, widget in additional_param_widgets.items():
                    new_row[param] = widget.value

                db_objects_new = pd.concat([db_objects, new_row],)
                db_objects_new.to_csv(db_objects_file, index= False)
                print(f'Object {object_id.value} added to database.')

        recording.on_click(button_record_pressed)

        display(ipw.HBox([ipw.VBox([object_id,project_id,object_creator,object_date,object_owner,object_title, object_name],layout=Layout(width="40%", height="300px"), style=style,),
                        ipw.VBox([object_category,object_type,object_technique,object_support,object_color],layout=Layout(width="40%", height="300px"), style=style),
                        ]))  

        display(*[widget for widget in additional_param_widgets.values()])
        display(ipw.HBox([recording, button_record_output]))
        

    def add_new_person(self):
        """Record a new person in the persons.txt file
        """

        # Function to get the existing initials from the file
        def get_existing_initials(file_path):
            try:
                df_persons = self.get_persons()
                existing_initials = df_persons['initials']                
                return existing_initials
            except FileNotFoundError:
                # If the file does not exist, return an empty set
                return set()
            
        # Function to update the text file if the initials are unique
        def update_text_file(file_path, name, surname, initials):
            # Check if the initials already exist
            existing_initials = get_existing_initials(file_path)
            
            if initials in existing_initials:
                print(f"Initials '{initials}' already exist. Please use different initials.")
            else:
                df_persons = self.get_persons()
                df_persons = pd.concat([df_persons, pd.DataFrame(data=[name,surname,initials], index=['name','surname','initials']).T])
                df_persons = df_persons.sort_values(by='name')
                df_persons.to_csv(self.folder_db/'persons.txt',index=False)
               
                print(f"Added: {name}, {surname} : {initials}")


        # Define ipython widgets
        name_widget = ipw.Text(        
            value='',
            placeholder='Enter a name',
            description='Name',               
        )

        surname_widget = ipw.Text(        
            value='',
            placeholder='Enter a surname',
            description='Surname',             
        )
        
        initials_widget = ipw.Text(        
            value='',
            placeholder='Enter initials in capital letters',
            description='Initials',             
        )

        recording = ipw.Button(
            description='Create record',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click me',            
        )        
        

        button_record_output = ipw.Output()

        def button_record_pressed(b):
            """
            Save the person info in the persons.txt file.
            """

            button_record_output.clear_output(wait=True)

            name = name_widget.value.strip()
            surname = surname_widget.value.strip()
            initials = initials_widget.value.strip()

            with button_record_output:

                if name and surname and initials: # ensure all fields are filled
                    update_text_file(self.folder_db / 'persons.txt', name, surname, initials)
                else:
                    
                    print("Please enter all fields (Name, Surname, Initials)")

            

        recording.on_click(button_record_pressed)

        display(name_widget,surname_widget,initials_widget)
        display(ipw.HBox([recording, button_record_output]))


    def add_new_project(self):
        """Add a new project in the DB_projects.csv file"""

        db_projects = self.get_db(db='projects')
        existing_columns = list(db_projects.columns)
        institutions = tuple(self.get_institutions()['name'].values)    
        persons = tuple([f'{x[0]}, {x[1]}' for x in self.get_persons()[['name','surname']].values])    

        # Define ipython widgets
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
            options = institutions,              
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

        project_leader = ipw.Combobox(
            placeholder = 'Enter a name or a surname',
            options=persons,            
            description='Project leader',
            disabled=False,
            layout=Layout(width="90%", height="30px"),
            style=style,
        )

        coresearchers = ipw.SelectMultiple(
            value=['none'],
            options=['none'] + list(persons), 
            description='Co-researchers',
            rows=5,
            disabled=False,
            layout=Layout(width="90%", height="95px"),
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
        additional_params = [col for col in existing_columns if col not in ['project_id', 'institution', 'start_date', 'end_date', 'project_leader', 'co-researchers', 'keywords']]
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
                persons = self.get_persons()

                institutions = pd.read_csv(self.folder_db / 'institutions.txt')['name'].values

                
                project_leader_name = project_leader.value.split(',')[0].strip()
                project_leader_surname = project_leader.value.split(',')[1].strip()
                project_leader_initials = persons.query(f'name == "{project_leader_name}" and surname == "{project_leader_surname}"')['initials'].values[0]

                if coresearchers.value[0] == 'none':
                    coresearchers_initials = 'none'

                else:
                    coresearchers_initials = []
                    for coresearcher in [x for x in coresearchers.value]:
                        coresearcher_name = coresearcher.split(',')[0].strip()
                        coresearcher_surname = coresearcher.split(',')[1].strip()
                        coresearcher_initials = persons.query(f'name == "{coresearcher_name}" and surname == "{coresearcher_surname}"')['initials'].values[0]
                        coresearchers_initials.append(coresearcher_initials)

                
                    coresearchers_initials = '-'.join(coresearchers_initials)
                
             
                new_row = pd.DataFrame({'project_id':project_Id.value,
                        'institution':institution.value, 
                        'start_date':startDate.value, 
                        'end_date':endDate.value,
                        'project_leader':project_leader_initials,  
                        'co-researchers':coresearchers_initials,                       
                        'keywords':project_keyword.value},                       
                        index=[0] 
                        )  
                
                if institution.value not in institutions:                       
                    institutions.append(str(institution.value))         
                    institutions = sorted(institutions)   

                    with open(self.folder_db / 'institutions.txt', 'w') as f:
                        f.write('\n'.join(institutions).strip())  
                    f.close()                
                

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
                    ipw.VBox([startDate,endDate, project_leader],layout=Layout(width="60%", height="95%")),
                    ipw.VBox([coresearchers],layout=Layout(width="60%", height="95%"))
                    ]),                
                ], layout=Layout(width="70%", height="100%")),                        
            ], layout=Layout(width="100%", height="110%"))
        ) 

        display(*[widget for widget in additional_param_widgets.values()])
        display(ipw.HBox([recording, button_record_output]))


    def create_db(self, folder_path):   
        
        ##### ENTER THE FOLDER_PATH IN CONFIG FILE #####

        with open(self.config_file, "r", encoding="utf-8") as f:
            config = json.load(f)

        # Ensure the databases section exists
        if 'databases' not in config:
            config["databases"] = {}

        # Update the databases dictionary with the new key-value pair
        config["databases"]["path_folder"] = folder_path

        
        # Save the updated config back to the JSON file
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)

        
        ##### CREATE THE DATABASE FILES #####

        # create the project database
        db_project = pd.DataFrame(columns=['project_id','institution','start_date','end_date','project_leader','co-researchers','keywords'])
        db_project.to_csv(Path(folder_path) / 'DB_projects.csv', index=False)


        # create the object database
        db_object = pd.DataFrame(columns=['object_id','object_category','object_type','object_technique','object_title','object_name','object_creator','object_date','object_owner','object_support','colorants','colorants_name','binding','ratio','thickness_um','color','status','project_id'])
        db_object.to_csv(Path(folder_path) / 'DB_objects.csv', index=False)

        
        # create several text files

        with open(Path(folder_path) / 'MFT_devices.txt', 'w') as f:
            f.write('Id,name,description,process_function\n')
            
        with open(Path(folder_path) / 'white_standards.txt', 'w') as f:
            f.write('Id,description\n')
            f.write('WR1,Fotonowy-fotolon-PTFE\n')

        with open(Path(folder_path) / 'object_creators.txt', 'w') as f:
            f.write('surname,name')

        with open(Path(folder_path) / 'object_techniques.txt', 'w') as f:
            f.write("China ink\n")
            f.write("acrylinc\n")
            f.write("aquatinte\n")
            f.write("black ink\n")
            f.write("black pencil\n")
            f.write("chalk\n")
            f.write("charcoal\n")
            f.write("monotypie\n")
            f.write("dye\n")
            f.write("felt-tip ink\n")
            f.write("frescoe\n")
            f.write("gouache\n")
            f.write("ink\n")
            f.write("linoleum print\n")
            f.write("lithograh\n")
            f.write("mezzotinte\n")
            f.write("oil paint\n")
            f.write("pastel\n")
            f.write("tin-glazed\n")
            f.write("watercolor\n")
            f.write("wood block print\n")        

        with open(Path(folder_path) / 'object_types.txt', 'w') as f:            
            f.write("banknote\n")
            f.write("book\n")
            f.write("BWS\n")       
            f.write("ceramic\n")
            f.write("colorchart\n")
            f.write("drawing\n")
            f.write("notebook\n")
            f.write("paint-out\n")
            f.write("painting\n")
            f.write("photograph\n")
            f.write("print\n")
            f.write("sculpture\n")
            f.write("seals\n")
            f.write("spectralon\n")
            f.write("tapistry\n")
            f.write("textile\n")
            f.write("wallpainting\n")

        with open(Path(folder_path) / 'object_supports.txt', 'w') as f:
            f.write("blue paper\n")
            f.write("canvas\n")
            f.write("cardboard\n")
            f.write("ceramic\n")
            f.write("coloured paper\n")
            f.write("cotton\n")
            f.write("Japanese paper\n")
            f.write("none\n")
            f.write("opacity chart\n")
            f.write("paper\n")
            f.write("parchment\n")
            f.write("rag paper\n")
            f.write("stone\n")
            f.write("transparent paper\n")
            f.write("wax\n")
            f.write("wood\n")
            f.write("woodpulp paper\n")
            f.write("wool\n")            

        with open(Path(folder_path) / 'institutions.txt', 'w') as f:
            f.write('name,acronym')

        with open(Path(folder_path) / 'persons.txt', 'w') as f:
            f.write('name,surname,initials')

        print(f'The database files have been created in the following folder: {folder_path}')
           
    
    def get_creators(self):
        if (Path(self.folder_db) / 'object_creators.txt').exists():
            df_creators = pd.read_csv(Path(self.folder_db) / 'object_creators.txt')
            return df_creators
        
        else:
            print(f'The file {Path(self.folder_db) / "object_creators.txt"} is not existing. Make sure to create one by running the function "create_DB" from the microfading package.')
            return


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


    def get_db_config(self):
        # Load folder path from JSON file if it exists
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                config = json.load(file)
                return config
        
        else:
            print('The db_config.json has been deleted ! Please re-install the microfading package.')
            return None      
    
        
    def get_db_use(self):

        if not self.config_file.exists():
            print("The configuration file does not exist. Please ensure 'db_config.json' is created.")
            return None
        

        with open(self.config_file, "r") as f:
            config = json.load(f)
    
        # Check if the 'databases' key exists in the config
        if "databases" in config:
            db_use_info = config["databases"]

            # Convert user info to a DataFrame
            df = pd.DataFrame.from_dict(db_use_info, orient="index", columns=["value"])
            return df
        else:
            print("The db_use info have not been registered. Please register using the 'set_DB()' function.")
            return None


    def get_db_path(self):
        
        db_config = self.get_db_config()
        config_databases = db_config['databases']

        if len(config_databases) == 0:            
            return None
        
        elif 'path_folder' not in config_databases.keys():
            print('There is no path configured for the databases. Please enter databases configuration info by using the function set_DB().')
            return None

        else:
            db_path = config_databases['path_folder']
            return db_path      
    
    
    def get_persons(self):
        
        if (Path(self.folder_db) / 'persons.txt').exists():
            df_persons = pd.read_csv(Path(self.folder_db) / 'persons.txt')
            return df_persons
        
        else:
            print(f'The file {Path(self.folder_db) / "persons.txt"} is not existing. Make sure to create one by running the function "create_DB" from the microfading package.')
            return
        

    def get_institutions(self):

        if (Path(self.folder_db) / 'institutions.txt').exists():
            df_institutions = pd.read_csv(Path(self.folder_db) / 'institutions.txt')
            return df_institutions
        
        else:
            print(f'The file {Path(self.folder_db) / "institutions.txt"} is not existing. Make sure to create one by running the function "create_DB" from the microfading package.')
            return


    def get_devices(self):

        if (Path(self.folder_db) / 'MFT_devices.txt').exists():
            df_devices = pd.read_csv(Path(self.folder_db) / 'MFT_devices.txt')
            return df_devices
        
        else:
            print(f'The file {Path(self.folder_db) / "MFT_devices.txt"} is not existing. Make sure to create one by running the function "create_DB" from the microfading package.')
            return


    def get_colorimetry_info(self):

        if not self.config_file.exists():
            print("The configuration file does not exist. Please ensure 'db_config.json' is created.")
            return None

        with open(self.config_file, "r") as f:
            config = json.load(f)
    
        # Check if the 'lighting' key exists in the config
        if "colorimetry" in config:
            colorimetry_info = config["colorimetry"]
            
            # Convert user info to a DataFrame
            df = pd.DataFrame.from_dict(colorimetry_info, orient="index", columns=["value"])
            return df
        else:
            print("The colorimetric conditions have not been registered. Please register using the 'set_colorimetry_info' function.")
            return None
    

    def get_exposure_conditions(self):

        if not self.config_file.exists():
            print("The configuration file does not exist. Please ensure 'db_config.json' is created.")
            return None
        

        with open(self.config_file, "r") as f:
            config = json.load(f)
    
        # Check if the 'exposure' key exists in the config
        if "exposure" in config:
            exposure_info = config["exposure"]

            hours_per_years = int(exposure_info['hours_per_day'] * exposure_info['days_per_year'])
            yearly_Hv = hours_per_years * exposure_info['illuminance_lux']

            exposure_info['hours_per_year'] = hours_per_years
            exposure_info['yearly_Hv_klxh'] = int(yearly_Hv / 1e3)
            
            # Convert user info to a DataFrame
            df = pd.DataFrame.from_dict(exposure_info, orient="index", columns=["value"])
            return df
        else:
            print("The exposure conditions info has not been registered. Please register using the 'set_exposure_conditions' function.")
            return None
        
    
    def get_light_dose_info(self):

        if not self.config_file.exists():
            print("The configuration file does not exist. Please ensure 'db_config.json' is created.")
            return None
        

        with open(self.config_file, "r") as f:
            config = json.load(f)
    
        # Check if the 'light_dose' key exists in the config
        if "light_dose" in config:
            light_dose_info = config["light_dose"]

            # Convert user info to a DataFrame
            df = pd.DataFrame.from_dict(light_dose_info, orient="index", columns=["value"])
            return df
        else:
            print("The light dose info have not been registered. Please register using the 'set_light_dose' function.")
            return None
      

    def get_white_standards(self):

        if (Path(self.folder_db) / 'white_standards.txt').exists():
            df_references = pd.read_csv(Path(self.folder_db) / 'white_standards.txt')
            return df_references
        
        else:
            print(f'The file {Path(self.folder_db) / "white_standards.txt"} is not existing. Make sure to create one by running the function "create_DB" from the microfading package.')
            return

    
    def update_db_projects(self, new: str, old:Optional[str] = None):

        if (Path(self.folder_db) / 'DB_projects.csv').exists():
            
            db_projects = self.get_db(db='projects')
            db_projects[new] = ''
            
            if old != None:
                if old in db_projects.columns:
                    db_projects.drop(old, axis=1, inplace=True)
                else:
                    print(f'The column {old} cannot be removed because it does not exist.')

            db_projects.to_csv(Path(self.folder_db) / 'DB_projects.csv',index=False)
            print('DB_projects successfully updated.')

        else:
            print('No databases have been created yet.')
        

    def update_db_objects(self, new: str, old:Optional[str] = None):

        if (Path(self.folder_db) / 'DB_objects.csv').exists():
            
            db_objects = self.get_db(db='objects')
            db_objects[new] = ''
            
            if old != None:
                if old in db_objects.columns:
                    db_objects.drop(old, axis=1, inplace=True)
                else:
                    print(f'The column {old} cannot be removed because it does not exist.')

            db_objects.to_csv(Path(self.folder_db) / 'DB_objects.csv',index=False)
            print('DB_projects successfully updated.')

        else:
            print('No databases have been created yet.')


    def set_colorimetry_info(self):


        wg_observer = ipw.Dropdown(
            description = 'Observer (deg)',
            value = '10',
            options = ['2', '10'],
            style = style
        )

        wg_illuminant = ipw.Dropdown(
            description = 'Illuminant',
            value = 'D65',
            options = ['A', 'B', 'C', 'D50', 'D55', 'D60', 'D65', 'D75', 'E', 'FL1', 'FL2', 'FL3', 'FL4', 'FL5', 'FL6', 'FL7', 'FL8', 'FL9', 'FL10', 'FL11', 'FL12', 'FL3.1', 'FL3.2', 'FL3.3', 'FL3.4', 'FL3.5', 'FL3.6', 'FL3.7', 'FL3.8', 'FL3.9', 'FL3.10', 'FL3.11', 'FL3.12', 'FL3.13', 'FL3.14', 'FL3.15', 'HP1', 'HP2', 'HP3', 'HP4', 'HP5', 'LED-B1', 'LED-B2', 'LED-B3', 'LED-B4', 'LED-B5', 'LED-BH1', 'LED-RGB1', 'LED-V1', 'LED-V2', 'ID65', 'ID50'],
            style = style
        )

        wg_white_standard = ipw.Dropdown(
            description = 'White standard',            
            options = self.get_white_standards()['Id'].values,
            style = style
        )

        recording = ipw.Button(
            description='Save',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click me',            
        )

        button_record_output = ipw.Output()

        

        def button_record_pressed(b):
            """
            Save the person info in the persons.txt file.
            """

            button_record_output.clear_output(wait=True)

            with open(self.config_file, "r") as f:
                config = json.load(f)

            # Update config with user data
            config["colorimetry"] = {
                "observer": f'{wg_observer.value}deg',
                "illuminant": wg_illuminant.value, 
                "white_standard": wg_white_standard.value,                               
            }
            # Save the updated config back to the JSON file
            with open(self.config_file, "w") as f:
                json.dump(config, f, indent=4)

            
            with button_record_output:
                print('Colorimetric conditions info recorded in the db_config.json file.')

        
        recording.on_click(button_record_pressed)

        display(ipw.VBox([wg_observer, wg_illuminant, wg_white_standard]))
        display(ipw.HBox([recording, button_record_output]))
   
    
    def set_db(self, folder_path:Optional[str] = '', use:Optional[bool] = True):
        
        wg_folder = ipw.Text(
            description = 'Path folder',
            placeholder = 'Location of the databases folder on your computer',
            value = folder_path,
            style = style, 
            layout=Layout(width="50%", height="30px"),
        )

        wg_use = ipw.Dropdown(
            description = 'Use',
            value = use,
            options = [True, False],
            style = style,
            layout=Layout(width="10%", height="30px"),
        )        

        recording = ipw.Button(
            description='Save',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click me',            
        )

        button_record_output = ipw.Output()


        def button_record_pressed(b):
            """
            Save the databases info in the db_config.json file.
            """

            button_record_output.clear_output(wait=True)

            with open(self.config_file, "r") as f:
                config = json.load(f)

            # Update config with user data
            config["databases"] = {
                "path_folder": wg_folder.value,
                "usage": wg_use.value,
                              
            }
            # Save the updated config back to the JSON file
            with open(self.config_file, "w") as f:
                json.dump(config, f, indent=4)

            
            with button_record_output:
                print('Database info recorded in the db_config.json file.')

        
        recording.on_click(button_record_pressed)

        display(ipw.VBox([wg_folder, wg_use]))
        display(ipw.HBox([recording, button_record_output]))

    
    def set_exposure_conditions(self):

        wg_illuminance = ipw.IntText(
            description = 'Illuminance (lux)',
            value = 100,
            style = style, 
        )

        wg_hours_per_day = ipw.IntText(
            description = 'Exposure hours per day',
            value = 10,
            style = style, 
        )

        wg_days_per_year = ipw.IntText(
            description = 'Exposure days per year',
            value = 365,
            style = style, 
        )

        recording = ipw.Button(
            description='Save',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click me',            
        )

        button_record_output = ipw.Output()


        def button_record_pressed(b):
            """
            Save the exposure conditions info in the db_config.json file.
            """

            button_record_output.clear_output(wait=True)

            with open(self.config_file, "r") as f:
                config = json.load(f)

            # Update config with user data
            config["exposure"] = {
                "illuminance_lux": wg_illuminance.value,
                "hours_per_day": wg_hours_per_day.value,
                "days_per_year": wg_days_per_year.value,                
            }
            # Save the updated config back to the JSON file
            with open(self.config_file, "w") as f:
                json.dump(config, f, indent=4)

            
            with button_record_output:
                print('Exposure conditions info recorded in the db_config.json file.')

        
        recording.on_click(button_record_pressed)

        display(ipw.VBox([wg_illuminance, wg_hours_per_day,wg_days_per_year]))
        display(ipw.HBox([recording, button_record_output]))

    
    def set_light_dose(self):

        wg_dose_unit = ipw.Dropdown(
            description = 'Dose unit',
            placeholder = 'Select a unit',
            options = ['He_MJ/m2', 'Hv_Mlxh', 't_sec'],
            style = style
        )

        recording = ipw.Button(
            description='Save',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click me',            
        )

        button_record_output = ipw.Output()

        def button_record_pressed(b):
            """
            Save the light dose unit in the db_config.json file.
            """

            button_record_output.clear_output(wait=True)

            with open(self.config_file, "r") as f:
                config = json.load(f)

            # Update config with user data
            config["light_dose"] = {
                "unit": wg_dose_unit.value,                                
            }
            # Save the updated config back to the JSON file
            with open(self.config_file, "w") as f:
                json.dump(config, f, indent=4)

            
            with button_record_output:
                print('The unit of the light dose has been recorded in the db_config.json file.')


        recording.on_click(button_record_pressed)

        display(ipw.VBox([wg_dose_unit]))
        display(ipw.HBox([recording, button_record_output]))
