# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:25:02 2022

@author: Nora
"""

# Import the libraries
import ifcopenshell
import bpy
from blenderbim.bim.ifc import IfcStore
 
# Define the file to search through
file = IfcStore.get_file()




# Define spaces
spaces = file.by_type('IfcSpace')

# Create for loop to print name of spaces
for space in spaces:
    print(space.Name)

# Print total number of rooms
print(f'Total number of rooms: {len(spaces)}')



# Define beams
beams = file.by_type('IfcBeam')

# Create for loop to print name of beams
for beam in beams:
    print(beam.Name)

    #for definition in beam.IsDefinedBy:
        #if definition_is_a('IfcBeDefinedByProperties'):
           # property_set = definition.RelatingPropertyDefinition
            #print(property_set.get_info())
            
            # Sort by the name of the propertyset
            #if property_set.Name == 'Pset_BeamCommon':
                #for property in property_set_HasProperties:
                   # print(property)
                    
                    #if property.Name == 'IsExternal':
                      #  print(property.NominalValue.wrappedValue)
                      #  

# Print total number of beams
print(f'Total number of beams: {len(beams)}')


















