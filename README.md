# Data Project
How can the Austin Animal Center increase the number of animals who are adopted and the speed at which they are rehomed?
By Andrea Messer, Charlotte Schnoebelen, Shamim Munshi, Yana Zykova, Sumaiya Ahmed

# Project Intro - same as intro in project doc??

With animal shelters in the US collectively taking in millions of companion animals each year and being stretched to capacity, there is interest in maximising the number of animals with positive outcomes - that is, adoption into loving forever homes as quickly as possible. Using data from the Austin Animal Center (AAC), this project set out to investigate how the shelter can increase the number of animals who are adopted and the speed at which they are rehomed.

This report outlines the development team’s approach to project delivery, provides insight into our analysis design and implementation strategy, and identifies some high-level findings. The next section summarises background information about animal shelters in the US - including the AAC - then section 3.0 details the project aims and objectives. The report goes on to outline the project specifications and analysis design (section 4.0), and subsequently describes our implementation process and challenges (section 5.0). Next, section 6.0 provides an overview of our data sources before concluding with high-level findings (section 7.0) and recommendations (section 8.0) for next steps. 

# Required Imports
* import requests - to get data from API
* import pandas as pd
* import numpy as np
* import seaborn as sns 
* import matplotlib.pyplot as plt
* import matplotlib.patches as mpatches
* import calendar 

# Methods used
* Data collecting
* Data cleaning
* Data analysis
* Data visulisation
  
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





