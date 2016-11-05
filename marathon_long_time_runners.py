import matplotlib.pyplot as plt
import pandas as pd



df_2016 = pd.read_csv("marathon_2016_results.csv", delimiter=";")
df_2015 = pd.read_csv("marathon_2015_results.csv", delimiter=";")
df_2014 = pd.read_csv("marathon_2014_results.csv", delimiter=";")
df_2013 = pd.read_csv("marathon_2013_results.csv", delimiter=";")

long_time_runners_df = pd.DataFrame({'place' : [], 'bib number': [], 'name': [], 'category':[], 'time':[]})
index = 0

results = []
for runner_2016 in df_2016['name']:
    for runner_2015 in df_2015['name']:
        if runner_2015 == runner_2016:
            for runner_2014 in df_2014['name']:
                if runner_2014 == runner_2016:
                    for runner_2013 in df_2013['name']:
                        if runner_2013 == runner_2016:
                            #print("Long time runner " + str(index) + " : " + runner_2016)
                            serie = pd.Series(df_2016.iloc[index])
                            results.append(serie)
                            #result.append()
    index = index + 1


print(len(results))
print(results[0])

df = pd.DataFrame(results, columns=['place', 'bib number', 'name', 'category', 'time'])
df2 = pd.concat(results, axis=1)
df.describe()
df2.describe()
