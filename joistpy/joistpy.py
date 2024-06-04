import numpy as np
import os
import pandas as pd

class Joist:
    """
    A class to represent a collection of joist types and designations.

    Attributes
    ----------
    joist_type : dict
        a dictionary containing all joist types in the collection
    name : str
        the name of the joist collection

    Methods
    -------
    None
    """
    def __getattr__(self, name):
        """
        Returns the attribute indicated by ```name```.

        Parameters
        ----------
        name : str
            the name of the attribute being accessed
        
        Returns
        -------
        joist_type : joisttype object
            the joisttype object referenced by ```name```
        """
        if name in self.joist_type:
            return self.joist_type[name]
        raise AttributeError(f"'Joist' object has no attribute '{name}'")
    
    def __init__(self, name):
        """
        Constructs the necessary attributes for the joist object.

        Parameters
        ----------
        name : str
            the name of the joist collection

        Returns
        -------
        None
        """
        self.name = name
        self.joist_type = {}

    def _add_joist_type(self, name, value):
        """
        Adds a joist type to the joist collection.

        Parameters
        name : str
            the name of the joist type to add to the joist collection
        value : joisttype object
            the joisttype object being added to the joist collection
        """
        self.joist_type[name] = value

class JoistType:
    """
    A class to represent a group of joist designations in a single type.

    Attributes
    ----------
    designations : dict
        a dictionary containing all joist designations within the group
    name : str
        the name of the group of joists

    Methods
    -------
    None
    """
    def __getattr__(self, name):
        """
        Returns the attribute indicated by ```name```.

        Parameters
        ----------
        name : str
            the name of the attribute being accessed
        
        Returns
        -------
        designation : designation object
            the designation object referenced by ```name```
        """
        if name in self.designations:
            return self.designations[name]
        raise AttributeError(f"'Joist_Type' object has no attribute '{name}'")
    
    def __init__(self, name):
        """
        Constructs the necessary attributes for the joisttype object.

        Parameters
        ----------
        name : str
            the name of the joisttype 

        Returns
        -------
        None
        """
        self.name = name
        self.designations = {}

    def _add_designation(self, name, value):
        """
        Adds a designation to the joist type group.

        Parameters
        name : str
            the name of the designation to add to the group
        value : designation object
            the designation object being added to the joist collection
        """
        self.designations[name] = value

class Designation:
    """
    A class to represent a single joist designation

    Attributes
    ----------
    name : str
        the name of the joist designation
    properties : dict
        a dictionary containing all the available properties of the joist
        designation

    Methods
    -------
    get_eq_area()
        Calculates the equivalent cross-sectional area of the designation
        according to the approx. weight of the designation in plf and the
        unit weight of steel.
    get_mom_inertia(span)
        Calculates the moment of inertia for the designation and the input span.
    get_wl360(span)
        Calculates the load in plf that would produce a deflection of L/360
        for the designation and input span.
    """

    def __getattr__(self, name):
        """
        Returns the attribute indicated by ```name```.

        Parameters
        ----------
        name : str
            the name of the attribute being accessed
        
        Returns
        -------
        property : varies
            the property referenced by ```name```
        """
        if name in self.properties:
            return self.properties[name]
        raise AttributeError(f"'Designation' object has no attribute '{name}'")
    
    def __init__(self, name):
        """
        Constructs the necessary attributes for the designation object.

        Parameters
        ----------
        name : str
            the name of the designation

        Returns
        -------
        None
        """
        self.name = name
        self.properties = {}

    def _add_property(self, name, value):
        """
        Adds a property to the designation.

        Parameters
        name : str
            the name of the designation to add to the group
        value : varies
            the property being added to the collection
        """
        self.properties[name] = value
    
    def get_eq_area(self):
        """
        Calculates the equivalent cross-sectional area of the designation
        according to the approx. weight of the designation in plf and the
        unit weight of steel.

        Parameters
        ----------
        None

        Returns
        -------
        eq_area : float
            the equivalent cross-sectional area of the designation
        """
        # Use the approx. weight per foot of the joist divided by the unit weight of steel to get an equivalent x-sectional area
        eq_area = (self.weight/490)*144

        return eq_area
    
    def get_mom_inertia(self, span):
        """
        Calculates the moment of inertia for the designation and the input span.

        Parameters
        ----------
        span : float or int
            the span of the joist in ft

        Returns
        -------
        mom_inertia : float
            the moment of inertia for the designation and the input span
        """
        # Calculate the load that produces L/360 deflection
        wl360 = self.get_wl360(span=span)
        # Calculate the moment of inertia per SJI formula
        mom_inertia = 26.767*(wl360)*(span-0.33)**3*(10**(-6))

        return mom_inertia

    def get_wl360(self, span):
        """
        Calculates the load in plf that would produce a deflection of L/360
        for the designation and input span.

        Parameters
        ----------
        span : float or int
            the span of the joist in ft

        Returns
        -------
        wl360 : float
            the load in plf that produces a deflection of L/360 for the
            designation and input span
        """
        if not isinstance(span, (int, float)):
            raise TypeError('span must be a positive int or float')

        # Ensure only non-zero integers get passed to the function
        if span <= 0:
            span = 1

        # Get l_360 property for current shape
        l360 = self.l_360

        defined_spans = [i for i in l360[1] if not np.isnan(i)]
        min_span = l360[0][l360[1].index(defined_spans[0])]
        max_span = l360[0][l360[1].index(defined_spans[-1])]

        # Interpolate between spans to get the load that produces L/360 deflection
        try:
            span_i = [i for i in l360[0] if span > i][-1]
            span_j = [i for i in l360[0] if span <= i][0]
        except IndexError:
            if len([i for i in l360[0] if span > i]) == 0:
                span_i = 0
            elif len([i for i in l360[0] if span <= i]) == 0:
                span_j = 60

        try:
            idx_i = l360[0].index(span_i)
            idx_j = l360[0].index(span_j)
        except ValueError:
            idx_i = l360[0][-1]
            idx_j = l360[0][-1]

        if span < min_span:
            wl360 = 550.0
        elif span > max_span:
            wl360 = 0.0
        elif min_span <= span and span <= max_span:
            w_i = l360[1][idx_i]
            w_j = l360[1][idx_j]

            wl360 = ((span-span_i)/(span_j-span_i))*(w_j-w_i)+w_i

        return wl360

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
    
                joist_dict[cur_joist_type_name][cur_joist_name][cur_property_name] = cur_property

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

            cur_designation._add_property(cur_property_name, cur_property)

        cur_joist_type._add_designation(cur_designation_name, cur_designation)

    sji._add_joist_type(cur_joist_type_name, cur_joist_type)
