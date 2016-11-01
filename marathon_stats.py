import matplotlib.pyplot as plt
import pandas as pd

# get age category based on first letter
def get_age_category(x):
    if x[0] == 'E':
        return 'Espoir'
    if x[0] == 'S':
        return 'Senior'
    if x[0] == 'V':
        return 'Veteran'

# get sex category based on first letter
def get_gender_category(x):
    if x[-1:] == 'F':
        return 'Femme'
    if x[-1:] == 'H':
        return 'Homme'

# read csv
df = pd.read_csv("marathon_2016_results.csv", delimiter=";")

# create new dataframe for age category and join
age_category_dataframe = df['category'].map(get_age_category)
final_df = df.join(age_category_dataframe, rsuffix='_age')

# create new dataframe for gender category and join
gender_category_dataframe = df['category'].map(get_gender_category)
final_df = final_df.join(gender_category_dataframe, rsuffix='_gender')


# print final dataframe grouped by age category then by gender
print(final_df.groupby(['category_age'])).count()
print(final_df.groupby(['category_gender'])).count()
