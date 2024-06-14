# ausfuehrung/handels_ausfuehrer.py

import requests
import hashlib
import hmac
import time
from urllib.parse import urlencode
from config import BASE_URL, API_KEY, API_SECRET

class HandelsAusfuehrer:
    def __init__(self):
        self.api_url = BASE_URL

    def _sign_payload(self, params):
        query_string = urlencode(params)
        signature = hmac.new(
            API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256
        ).hexdigest()
        return query_string + "&signature=" + signature

    def trades_ausfuehren(self, signale):
        for signal in signale:
            seite = signal["seite"]
            symbol = signal["symbol"]
            menge = 0.001  # Beispielmenge

            endpoint = "/api/v3/order"
            url = f"{self.api_url}{endpoint}"

            params = {
                "symbol": symbol,
                "side": seite.upper(),
                "type": "MARKET",
                "quantity": menge,
                "timestamp": int(time.time() * 1000)
            }

            headers = {
                "X-MBX-APIKEY": API_KEY
            }

            signed_params = self._sign_payload(params)
            response = requests.post(url, headers=headers, params=signed_params)
            print(response.json())
          
