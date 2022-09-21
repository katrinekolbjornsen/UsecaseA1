# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 10:42:58 2022

@author: Nora
"""

# Import the libraries
import ifcopenshell
import bpy
from blenderbim.bim.ifc import IfcStore
 
# Define the file to search through
file = IfcStore.get_file()


## BEAMS ##
# Find all the beams in the model
# Define beams and loop through the model
beams = file.by_type("IfcBeam")
for beam in beams:
    beam.Name
    # Get the properties for the beams
    for definition in beam.IsDefinedBy:
        
        # Filter the results in order for the script to support IFC2X3
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition

# Find the material of the beams            
for beam in beams:
    for relAssociatesMaterial in beam.HasAssociations:
        print(relAssociatesMaterial.RelatingMaterial.Name)
        
        

## COLUMNS ##
# Find all the columns in the model
# Define columns and loop through the model
columns = file.by_type("IfcColumn")
for column in columns:
    column.Name
    # Get the properties for the columns
    for definition in column.IsDefinedBy:
        
        # Filter the results in order for the script to support IFC2X3
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition

# Find the material of the columns            
for column in columns:
    for relAssociatesMaterial in column.HasAssociations:
        print(relAssociatesMaterial.RelatingMaterial.Name)



## SLABS ##
slabs = file.by_type("IfcSlab")
for slab in slabs:
    slab.Name
    # Get the properties for the slabs
    for definition in slab.IsDefinedBy:
        
        # Filter the results in order for the script to support IFC2X3
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition

# Find the material of the slabs            
for slab in slabs:
    for relAssociatesMaterial in slab.HasAssociations:
        print(relAssociatesMaterial.RelatingMaterial.Name)        
        


# What needs to be done:
    # Fix the script for columns and slabs
    # For beams, columns, and slabs:
        # use only the concrete elements
        # find/calulate their volumes
    # Summarize the volumes

        