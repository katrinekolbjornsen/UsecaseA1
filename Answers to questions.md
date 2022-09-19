 # Answers to questions
## Describe the use case you have chosen
The use case chosen is structural. Structural in this case means all of the load-bearing elements located in the building, such as beams, columns, walls and slabs. The goal is to easily calculate the amount of concrete needed in a building.  


## Who is the use case for?
The use case is for the structural engineer in the project, who needs to easily access information about the amount of concrete in different buildings. This includes finding the number of different elements and their dimensions, and summing it up to find the total amount of concrete. This use case is both for the concrete manufacturer and the LCA engineers. 


## What disciplinary (non BIM) expertise did you use to solve the use case
Basic geometry and mathematics. Knowledge about structural elements in buildings was also necessary. 


## What IFC concepts did you use in your script (would you use in your script)
Object and properties in order to identify concrete elements and find their dimensions. 


## What disciplinary analysis does it require?
It requires the architect to be done with the model, as well as the structural engineer to have completed their calculations. 


## What building elements are you interested in?
We are interested in all the load-bearing elements in the building made from concrete. 


## What (use cases) need to be done before you can start your use case?
Architectural and fire needs to be done beforehand, as their work determine the structural model. 


## What is the input data for your use case?
The input data for our use case is:
- analysis of the model
- localize and extract information about the volume of every concrete object
- summarize the volumes of the objects
- get a total amount displayed 


## What other use cases are waiting for your use case to complete?
LCA, Build & Operate and Cost are waiting for our use case to be complete.  
