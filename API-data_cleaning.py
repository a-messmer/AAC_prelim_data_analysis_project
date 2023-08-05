import requests
import pandas as pd

""" Data Collection """

"""
Requesting data from the Austin Animal shelter API using requests.get

Both datasets contain around 160,000 rows of data. To retrieve all the data, using ?$limit=160000 
at the end of both API Endpoints 
"""

# Requesting data from the intake API and storing as a JSON
response = requests.get('https://data.austintexas.gov/resource/wter-evkm.json?$limit=160000')
data_set1 = response.json()
print(data_set1)

# Requesting data from the outcome API and storing as a JSON
response2 = requests.get('https://data.austintexas.gov/resource/9t4d-g238.json?$limit=160000')
data_set2 = response2.json()
print(data_set2)

""" Converting JSON data to a dataframe using PANDAS """

# dataframe(df) for intake data
animal_intake_df = pd.DataFrame(data_set1)
# only showing the first 5 rows - can remove .head() to see more rows
print(animal_intake_df.head(5))

# dataframe 2 for output
animal_outcome_df = pd.DataFrame(data_set2)
print(animal_outcome_df.head(5))

""" Cleaning Data
As both datasets contains 2 columns that store the datatime, we can remove both columns and only store the date
"""

# checking the datatypes of the columns
animal_intake_df.info()


""" Removing the time from the datetime column, so we are just left with the date 

As the datetime column is a object, we are using the pandas to_datetime function, 
to convert the column into a datetime object

Then using the dt (datetime) date PANDAS function to convert our datetime object to just the date
"""
intake_date = pd.to_datetime(animal_intake_df['datetime']).dt.date

# print(intake_date) - this will show the output which is just the date

# using the PANDAS drop function to drop the 'datetime' and 'datetime2' columns from the intake dataset
intake_df = animal_intake_df.drop(['datetime', 'datetime2'], axis='columns')

# inserting the new column which we created before - (intake_date) and placing this at index 2 in the dateset
intake_df.insert(2, 'intake_date', intake_date)

# returning first 5 rows, just to show how the dataframe now looks
print(intake_df.head(5))


""" Cleaning outcome Data """

outcome_date = pd.to_datetime(animal_outcome_df['datetime']).dt.date

# this dataset contains the 'datetime' and 'monthyear' column which both can be removed
outcome_df = animal_outcome_df.drop(['datetime', 'monthyear'], axis='columns')

outcome_df.insert(2, 'outcome_date', outcome_date)

print(outcome_df.head(5))


""" Merging both datasets to retrieve the rows that contain both intake and output information """

merged_df = pd.merge(intake_df, outcome_df, on='animal_id', how='inner')

print(merged_df.head(2))

# removing the A from animal id to allow sorting of animal id later on
merged_df['animal_id'] = merged_df['animal_id'].str[1:]
print(merged_df)

# sorting rows based on animal_id - this way we can check for any duplicates
merged_df = merged_df.sort_values('animal_id')
print(merged_df)

# removing duplicates based on the animal_id
merged_df = merged_df.drop_duplicates(subset='animal_id')  # .reset_index() - can reset the index 
print(merged_df)

