# Crypto_Currency_Predict
Predict Crypto Currency Price Predict using Korea UPbit unoffical realtime data</br>

대한민국에서 가장 많이 사용하는 UPBit의 비공식 데이터를 이용해서 LSTM을 이용하여 종가를 예측하는 프로그램입니다.</br>

[UPBit Data Crawler]<br>
업비트에서 제공하는 비공식 API로써 사이트에 Ajax형태인 JSON으로 반환 할때 이용되는 URL을 통해 데이터를 수집합니다.<br>
[URL]<br>
https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/{minutes}?code=CRIX.UPBIT.KRW-{coinName}&count={count}&to={timeseries}.000Z<br>
URL에서의 Parameter<br>
minutes : 1,3,5,30,60,240 분으로 검색기간을 지정할 수 있습니다.<br>
count : 검색기간을 두고 호출할 데이터의 갯수를 설정합니다 (count<=200)<br>
coinName : UPbit에서 제공하는 KRW <-> Coin 을 설정합니다. (ex. BTC : 비트코인 , ETH : 이더리움 , XRP : 리플)<br>

Python libs:
[LSTM]
> 1. tensorflow
> 2. numby
> 3. pandas
> 4. sklearn
[UpBit Data Crawler]
> 1. requests
> 2. pandas
> 3. datetime
