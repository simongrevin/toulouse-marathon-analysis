import pandas as pd

df_2016 = pd.read_csv("marathon_2016_results.csv", delimiter=";")
df_2015 = pd.read_csv("marathon_2015_results.csv", delimiter=";")
df_2014 = pd.read_csv("marathon_2014_results.csv", delimiter=";")
df_2013 = pd.read_csv("marathon_2013_results.csv", delimiter=";")

# only get runners who've ran all 4 years
df_regulars = df_2016.merge(
        df_2015, on='name', how='inner', suffixes=('_2016', '_2015')
    ).merge(df_2014, on='name', how='inner', suffixes=('_2015', '_2014')
    ).merge(df_2013, on='name', how='inner', suffixes=('_2014', '_2013'))

# write to csv
df_regulars.to_csv('regular_runners.csv', sep=';', encoding='utf-8')
