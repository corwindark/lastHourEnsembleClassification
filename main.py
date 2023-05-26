# This is a sample Python script.

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import darts


from darts import TimeSeries
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv('C:/users/corwi/downloads/daily_traffic.csv')


#index = df['holiday'] == 'None'
#print(index)
#df['holiday'] = index
print(df.shape[0])
print(df.duplicated().astype(int).sum())
#df = df[~df.duplicated(), :]
df = df.drop_duplicates()
print(df.shape[0])
series = TimeSeries.from_dataframe(df, time_col='date_time', fill_missing_dates=True, freq='H')
series = series.drop_before(pd.Timestamp('1/1/2016 0:00'))


series.plot()
plt.show()



