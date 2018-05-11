import pandas as pd
import numpy as np
from sklearn.preporcessing import MinMaxScaler
from crwaler import load_data

def build_data(minites,coinName,date):
    time="00:00:00" # UTC
    data = crawler.load_data(minutes, 200, coinName, 10, date, time)
    data = data.sort_values(['Time'], axis=0)
    data = data.set_index('Time')
    data = data.drop(['Coin'], axis=1)
    data = data.values[1:].astype(np.float)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler_Y= MinMaxScaler(feature_range=(0, 1))

    x = scaler.fit_transform(data)
    y = scaler_Y.fit_transform(data[:, [-1]])

    dataX = []
    dataY = []
    for i in range(0, len(y) - seq_length):
        _x = x[i:i + seq_length]
        _y = y[i + seq_length]
        #     print(_x , _y)
        dataX.append(_x)
        dataY.append(_y)

    return dataX , dataY