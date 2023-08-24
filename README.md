# **A PRELIMINARY ANALYSIS: INCREASING ADOPTION RATES AT THE AUSTIN ANIMAL CENTER**
### By Andrea Messmer, Charlotte Schnoebelen, Shamim Munshi, Yana Zykova, Sumaiya Ahmed

# *Project Intro*
With animal shelters in the US collectively taking in millions of companion animals each year and being stretched to capacity, there is interest in maximising the number of animals with positive outcomes - that is, adoption into loving forever homes as quickly as possible. Using data from the Austin Animal Center (AAC), this project set out to investigate how the shelter can increase the number of animals who are adopted and the speed at which they are rehomed. Specific questions that guided the analysis are:
* What are the characteristics of animals who are adopted?
* For animals who are adopted, how long do they stay in the shelter before being rehomed?
* Are there particular times during the year that most adoptions happen?
* How have adoption trends changed over time?
  
# *Installations Required*
* `Pip install pandas`
* `Pip install numpy`
* `pip install matplotlib `
* IDE - VScode or Jupyter Notebook
  
# *Required Imports*
* `import requests` - to get data from API
* `import pandas as pd` - to use pandas library for data anlysis and manipulation
* `import numpy as np` - to perform mathematical operations on arrays
* `import seaborn as sns` - for visualisation
* `import matplotlib.pyplot as plt` - for visualisation
* `import matplotlib.patches as mpatches`
* `import calendar`
  
# *Methods Used*
* Data collecting
* Data cleaning
* Data processing
* Data analysis
* Data visualisation
  
# *Columns in Cleaned Dataset*
* Animal ID - this is a unique ID which is used to identify each animal
* Animal - this is the type of the animal
* Intake Date - the date at which the animal is taken in by the shelter
* Outcome Date - the date at which the animal leaves the shelter
* Time in shelter - The length of time animal has spent in the shelter
* Age at Intake - Age of animal when they were taken in by the shelter
* Age range at intake - The intake age category for the animal
* Age at Outcome - Age of animal when they leave the shelter
* Age range at outcome - the age category for the animal at the time of outcome
* Intake condition - the condition of the animal when they were taken in by the shelter
* Intake Type - The type of intake (stray, public assist etc)
* Outcome Type - What the outcome was the animal (Adopted, Returned to owner etc)
* Sex - Sex of the animal - Male or female
* Neuter status at outcome - neuter status (neutered/intact) when animal left the shelter
* Breed - the breed of the animal
* Mixed Breed - a boolean value; True if animal is a mixed breed and False if it is purebred
* Colour - Colour of the animal
* Total touchpoints - The total number of times a given animal was taken in by the shelter - this was used for dataframe merging
* Touchpoint count - A number representing the count of the times that an animal was taken in by the shelter: 1 = first time at shelter, 2 = second time in shelter etc.

<img src="Dataframe.png" width="2000" height="200" />

# *Code Structure*
#### *Sections 1 - 9 - Data collecting and Data cleaning*
#### *Section 10 - Descriptive analysis*
#### *Section 11 - Time series analysis*

# *Key Results*
* Adoption rates are affected by the season / month, animal type and characteritstics of the animals.
* Dogs are adopted all year round at the same rate but cats have a decrease in adoptions during the spring.
* Stray or owner surrendered animals are more likely to get adopted than animals of other intake types.
* Neutered or spayed animals have higher adoption rates to animals who are intact.
* Adopted animals tend to be younger than animals with other outcomes; dogs who were 1-3 years old and cats up to one year old had higher adoption rates than other age groups.

# *Sources*
Austin Animal Centre Intakes https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Intakes/wter-evkm
Austin Animal Centre Outcomes https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238




