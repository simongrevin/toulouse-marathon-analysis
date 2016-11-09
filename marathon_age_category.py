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


# read csv
df = pd.read_csv("marathon_2016_results.csv", delimiter=";")

# create new dataframe for age category and join
age_category_dataframe = df['category'].map(get_age_category)
final_df = df.join(age_category_dataframe, rsuffix='_age')

# print final dataframe grouped by age category then by gender
df_group = final_df.groupby(['category_age']).count()['name']
print(df_group)

#sets the labels, values and colors
labels = 'Espoir (20 to 22 yo)', 'Senior (23 to 39 yo)', 'Veteran (40+)'
sizes = [df_group['Espoir'], df_group['Senior'], df_group['Veteran']]
colors = ['yellowgreen', 'gold', 'lightskyblue']

# explode second slice
explode = (0, 0.1, 0)

# configure pie
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')

# show pie
plt.show()
