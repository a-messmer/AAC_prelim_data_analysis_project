# Data Project
How can the Austin Animal Center increase the number of animals who are adopted and the speed at which they are rehomed?
By Andrea Messer, Charlotte Schnoebelen, Shamim Munshi, Yana Zykova, Sumaiya Ahmed

# Required Imports
* import requests - to get data from API
* import pandas as pd
* import numpy as np
* import seaborn as sns 
* import matplotlib.pyplot as plt 

# Data Processing
* We used an API to get the data on Austin Animal shelter intakes and outcomes
* We merged the datasets using Pandas
* 
  

# Columns in Dataset
* Animal ID - this is the ID which is used to identify the animals
* Animal - this is the type of the animal
* Intake Date - the date at which the animal is taken in by the shelter
* Outcome Date - the date at which the animal leaves the shelter
* Time in shelter - The length of time animal has spent in the shelter
* Age at Intake - Age of animal when they were taken in by the shelter
* Age range at intake - The intake age category for the animal
* Age at Outcome - Age of animal when they leave the shelter
* Age range at outcome - the outcome age category for the animal
* Intake condition - the condition of the animal when they were taken in by the shelter
* Intake Type - The type of intake (stray, public assist etc)
* Outcome Type - What the outcome was the animal (Adopted, Returned to owner etc)
* Sex - Sex of the animal - Male or female
* Neuter status at outcome - what was the neuter status when animal left the shelter
* Breed - the breed of the animal
* Mixed Breed - this contains a boolean value, True if animal is a mixed breed and False if it isn't
* Colour - Colour of the animal
* Total touchpoints - The total amount of times the same animal has been returned to the shelter - this was used for dataframe merging
* Touchpoint count - The number of the return to the shelter - 1 = first time at shelter, 2 = second time in shelter etc. 





