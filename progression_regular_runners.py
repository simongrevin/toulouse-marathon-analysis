import pandas as pd
import datetime as dt
import time
from matplotlib import pyplot as plt

df_runners = pd.read_csv("regular_runners.csv", delimiter=";")

# only get runners who've constantly been faster year on year
df_runners = df_runners.query('(time_2016 < time_2015) & (time_2015 < time_2014) & (time_2014 < time_2013)')
df_runners = df_runners.reset_index(drop=True)

# setting the graph
fig = plt.figure()
graph = fig.add_subplot(111)

# x axis are the years
x_axis = [2013, 2014, 2015, 2016]
graph.set_xticks(x_axis)
graph.set_xticklabels(x_axis)


# for each runner
for i in range(0, len(df_runners)):

    # get time for each year
    _2013 = time.strptime(df_runners['time_2013'][i], "%H:%M:%S")
    _2014 = time.strptime(df_runners['time_2014'][i], "%H:%M:%S")
    _2015 = time.strptime(df_runners['time_2015'][i], "%H:%M:%S")
    _2016 = time.strptime(df_runners['time_2016'][i], "%H:%M:%S")

    # convert to minutes
    minutes_2013 = int(dt.timedelta(hours=_2013.tm_hour,minutes=_2013.tm_min,seconds=_2013.tm_sec).total_seconds() / 60)
    minutes_2014 = int(dt.timedelta(hours=_2014.tm_hour,minutes=_2014.tm_min,seconds=_2014.tm_sec).total_seconds() / 60)
    minutes_2015 = int(dt.timedelta(hours=_2015.tm_hour,minutes=_2015.tm_min,seconds=_2015.tm_sec).total_seconds() / 60)
    minutes_2016 = int(dt.timedelta(hours=_2016.tm_hour,minutes=_2016.tm_min,seconds=_2016.tm_sec).total_seconds() / 60)

    # print name and times
    print(df_runners['name'][i] + ' : ' + str(minutes_2013) + ' - ' + str(minutes_2014) + ' - ' + str(minutes_2015) + ' - ' + str(minutes_2016))

    # y axis are the times
    y_axis = [minutes_2013, minutes_2014, minutes_2015, minutes_2016]

    # insert into graph
    graph.plot(x_axis, y_axis)

# add axis labels
plt.xlabel('Years')
plt.ylabel('Time (in minutes)')

# show graph
plt.show()
