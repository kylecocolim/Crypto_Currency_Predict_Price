import json
import requests
import pandas as pd
import datetime

def timeseries_changer(timeseries):
    date = timeseries[:10]
    time = timeseries[11:]
    date += ' ' + time
    series = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    series = series - datetime.timedelta(hours=9)
    series = series.strftime('%Y-%m-%d %H:%M:%S')
    series = series[:10] + "T" + series[11:]
    return series

def load_data(minutes, count, coinName, worktime, date):
    minutes = minutes
    coinName = coinName
    count = count
    worktime = worktime
    date = date
    time = "00:00:00"
    timeseries = date + 'T' + time
    print(timeseries)

    dataset = []

    for index in range(worktime):
        url = "https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/{minutes}?code=CRIX.UPBIT.KRW-{coinName}&count={count}&to={timeseries}.000Z".format(
            minutes=minutes, coinName=coinName, count=count, timeseries=timeseries)
        print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get(url, headers=headers).json()
        for i in response:
            coin = i['code']
            coinname = coin.replace("CRIX.UPBIT.KRW-", "")
            open = i['openingPrice']
            high = i['highPrice']
            low = i['lowPrice']
            trade = i['tradePrice']
            Time = i['candleDateTimeKst']
            dataset.append([coinname, open, high, low, trade, Time])

        print("Step {} , Success! , {} times left".format(index, worktime - index))
        timeseries = dataset[-1][-1]
        timeseries = timeseries[0:19]
        timeseries = timeseries_changer(timeseries)
        print(timeseries)

    dataset = pd.DataFrame(dataset)
    dataset.columns = ['Coin', 'Open', 'High', 'Low', 'Trade', 'Time']
    dataset.to_csv('Upbit.csv', encoding='utf-8')

    return dataset
