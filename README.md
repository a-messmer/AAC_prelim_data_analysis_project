# Data-Project
CFG group project by Andrea Messer, Charlotte Schnoebelen, Shamim Munshi, Yana Zykova, Sumaiya Ahmed

# Data Collecting
Two API's used to fetch data using the requests function. This retrieved data is then stored in a JSON format.
Used pandas Dataframe to covert both JSON data to a dataframe.
Creating csv files for both the dataframes. 

# Data Cleaning
We start by cleaning the intakes dataset. 
Removing duplicate rows to prevent data from being skewed. 
As there are multiple entries under animal id for some animals (this is due to animals bein returned to the shelter) we use a touchpoint method to ensure that when we merge both dataframes, the merge is done correctly.
Removing duplicate columns (datetime and datetime2) are both the same columns so we removed one
We did the exact same with the outake dataset. 

Merging the dataframes using an inner join. Therefore, if there are any rows where there is no matching income / outcome data, those rows will not be included in the merge. This is because we want to look at the entire process (intake to outcome) for every animal.

After merging we further clean the data.
First we convert the animal id to an integer using regular expressions and then converting the datatype to an integer.
We removed duplicate and unncessary columns.
As we want to focus on animals that can be adopted we removed wildlife and livestock records.

As the sex and neuter status where both in the same cell, we extracted this so we had new columns for the sex and neuter status.
We calculated and created a new column for the length an animal stays in the shelter using intake and outcome date. 
We also checked if there were any incorrects dates that may have been added (intake date is after the outcome date) and removed these rows as they are inaccurate and will skew the results. 

Converted the datetime values to only contain the date and not the time. 
We used bins to create the age range and added a new column to the dataframe for this. 
We then addressed null values and saw there was 1 column which had a large amount of null values. The column that contained majority null values was later removed.

To end the data cleaning we renamed our columns and reindexed them.
Finally we created a new csv file for the clean data which was ready to use for analysis. 

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




