import matplotlib.pyplot as plt
import pandas as pd


def categorize(x):
    if x[0] == 'E':
        return 'Espoir'
    if x[0] == 'S':
        return 'Senior'
    if x[0] == 'V':
        return 'Veteran'

        
df = pd.read_csv("marathon_2016_results.csv", delimiter=";")
category_col = df['category'].map(categorize)

df_with_global_categories = df.join(category_col, rsuffix='_global')

print(df_with_global_categories.groupby(['category_global'])).count()
