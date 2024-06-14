# daten/daten_abruf.py

import requests
from config import BASE_URL, API_KEY

class DatenAbruf:
    def __init__(self):
        self.api_url = BASE_URL

    def abrufen(self, symbol="BTCUSDT", interval="1m"):
        endpoint = "/api/v3/klines"
        url = f"{self.api_url}{endpoint}"
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": 100
        }
        headers = {
            "X-MBX-APIKEY": API_KEY
        }
        response = requests.get(url, headers=headers, params=params)
        daten = response.json()
        return daten
