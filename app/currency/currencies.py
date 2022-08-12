from datetime import datetime, timedelta
import requests

class CurrenciesService:
    _currencies = {}
    LastUpdate = None
    _url = 'https://economia.awesomeapi.com.br/all'
    _timeToExpire = None

    def __init__(self, timeToExpire=10):
        self._timeToExpire = int(timeToExpire)
        self._currencies['BRL'] = { 
                "name": "Real Brasileiro",
                "high": 1, 
                "low": 1, 
                "varBid": 0, 
                "pctChange": 0, 
                "bid": 1, 
                "ask": 1,
                "createDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

        self.Load()

    def Load(self):
        r = requests.get(self._url)
        data = r.json()

        for code in data:
            value = data[code]
            self._currencies[code.upper()] = { 
                "name": value['name'],
                "high": float(value['high']), 
                "low": float(value['low']), 
                "varBid": float(value['varBid']), 
                "pctChange": float(value['pctChange']), 
                "bid": float(value['bid']), 
                "ask": float(value['ask']),
                "createDate": value['create_date']
            }

        self.LastUpdate = datetime.now()

    def Get(self):
        if self.LastUpdate is None:
            self.Load()

        if datetime.now() - self.LastUpdate > timedelta(minutes=self._timeToExpire):
            self.Load()

        return self._currencies

    def GetByCode(self, code:str):
        if self.LastUpdate is None:
            self.Load()

        if datetime.now() - self.LastUpdate > timedelta(minutes=self._timeToExpire):
            self.Load()

        if code.upper() in self._currencies:
            return self._currencies[code.upper()]

        return None