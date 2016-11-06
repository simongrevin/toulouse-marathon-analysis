import pandas as pd
import datetime as dt
import time
from matplotlib import pyplot as plt
from matplotlib.dates import date2num

df_runners = pd.read_csv("regular_runners.csv", delimiter=";")
df_runners = df_runners.head(10)

fig = plt.figure()
graph = fig.add_subplot(111)
x_years = ['2013', '2014', '2015', '2016']
graph.set_xticks(x_years)
graph.set_xticklabels(x_years)

for i in range(0, len(df_runners)):

    _2013 = time.strptime(df_runners['time_2013'][i], "%H:%M:%S")
    _2014 = time.strptime(df_runners['time_2014'][i], "%H:%M:%S")
    _2015 = time.strptime(df_runners['time_2015'][i], "%H:%M:%S")
    _2016 = time.strptime(df_runners['time_2016'][i], "%H:%M:%S")

    minutes_2013 = int(dt.timedelta(hours=_2013.tm_hour,minutes=_2013.tm_min,seconds=_2013.tm_sec).total_seconds() / 60)
    minutes_2014 = int(dt.timedelta(hours=_2014.tm_hour,minutes=_2014.tm_min,seconds=_2014.tm_sec).total_seconds() / 60)
    minutes_2015 = int(dt.timedelta(hours=_2015.tm_hour,minutes=_2015.tm_min,seconds=_2015.tm_sec).total_seconds() / 60)
    minutes_2016 = int(dt.timedelta(hours=_2016.tm_hour,minutes=_2016.tm_min,seconds=_2016.tm_sec).total_seconds() / 60)

    y_perfs = [minutes_2013, minutes_2014, minutes_2015, minutes_2016]
    graph.plot(x_years, y_perfs)

plt.xlabel('years')
plt.ylabel('time')
plt.show()
