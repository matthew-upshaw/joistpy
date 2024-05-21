# Import dependencies
import os
import pandas as pd

# Define classes
class Joist:
    def __init__(self, name):
        self.name = name
        self.joist_type = {}

    def add_joist_type(self, name, value):
        self.joist_type[name] = value

    def __getattr__(self, name):
        if name in self.joist_type:
            return self.joist_type[name]
        raise AttributeError(f"'Joist' object has no attribute '{name}'")

class JoistType:
    def __init__(self, name):
        self.name = name
        self.designations = {}

    def add_designation(self, name, value):
        self.designations[name] = value

    def __getattr__(self, name):
        if name in self.designations:
            return self.designations[name]
        raise AttributeError(f"'Joist_Type' object has no attribute '{name}'")

class Designation:
    def __init__(self, name):
        self.name = name
        self.properties = {}

    def add_property(self, name, value):
        self.properties[name] = value

    def get_l360(self, span):
        pass

    def __getattr__(self, name):
        if name in self.properties:
            return self.properties[name]
        raise AttributeError(f"'Designation' object has no attribute '{name}'")

# Define property filepath dictionary
filepath = {
    'K_Series':{
        'l_360':'K_L_360.csv',
        'total':'K_Total.csv',
        'weight':'K_weight.csv',
    },
}

# Get the directory of the currently executing module
module_dir = os.path.dirname(__file__)

# Construct the relative path to property files folder
directory_path = os.path.join(module_dir, 'property files')

# Loop through files and add properties to joist_dict
joist_dict = {}
for cur_joist_type_name in filepath.keys():
    if cur_joist_type_name not in joist_dict.keys():
        joist_dict[cur_joist_type_name] = {}
    
    for cur_property_name in filepath[cur_joist_type_name].keys():
        cur_file = os.path.join(directory_path, filepath[cur_joist_type_name][cur_property_name])
        df = pd.read_csv(cur_file)

        for col in df.columns:
            cur_list = []
            for idx, item in enumerate(df[col].to_list()):
                if item == '#VALUE!' or item == '#N/A':
                    cur_list.append(None)
                else:
                    cur_list.append(float(item))
            df[col] = cur_list

        if cur_property_name == 'weight':
            joist_des = df.columns.to_list()

            for joist in joist_des:
                cur_property = df[joist].to_list()[0]
                cur_joist_name = cur_joist_type_name.split('S')[0]+joist

            if cur_joist_name not in joist_dict[cur_joist_type_name].keys():
                joist_dict[cur_joist_type_name][cur_joist_name] = {}

            joist_dict[cur_joist_type_name][cur_joist_name][cur_property] = cur_property

        else:
            joist_des = df.columns[1:].to_list()

            for joist in joist_des:
                cur_property = [df['Span'].to_list(), df[joist].to_list()]
                cur_joist_name = cur_joist_type_name.split('S')[0]+joist
    
                if cur_joist_name not in joist_dict[cur_joist_type_name].keys():
                    joist_dict[cur_joist_type_name][cur_joist_name] = {}
    
                joist_dict[cur_joist_type_name][cur_joist_name][cur_property_name] = cur_property

# Add all information in joist_dict into the classes
sji = Joist('SJI')

for cur_joist_type_name in joist_dict.keys():
    cur_joist_type = JoistType(cur_joist_type_name)

    for cur_designation_name in joist_dict[cur_joist_type_name].keys():
        cur_designation = Designation(cur_designation_name)

        for cur_property_name in joist_dict[cur_joist_type_name][cur_designation_name].keys():
            cur_property = joist_dict[cur_joist_type_name][cur_designation_name][cur_property_name]

            cur_designation.add_property(cur_property_name, cur_property)

        cur_joist_type.add_designation(cur_designation_name, cur_designation)

    sji.add_joist_type(cur_joist_type_name, cur_joist_type)
