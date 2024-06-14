# strategie/strategie.py

import numpy as np

class Strategie:
    def __init__(self):
        pass

    def signale_generieren(self, marktdaten):
        schlusskurse = [float(d[4]) for d in marktdaten]  # Schlusskurse aus den Kerzendaten
        kurz_sma = np.mean(schlusskurse[-7:])  # 7-Perioden gleitender Durchschnitt
        lang_sma = np.mean(schlusskurse[-25:])  # 25-Perioden gleitender Durchschnitt

        signale = []
        if kurz_sma > lang_sma:
            signale.append({"symbol": "BTCUSDT", "seite": "kaufen"})
        elif kurz_sma < lang_sma:
            signale.append({"symbol": "BTCUSDT", "seite": "verkaufen"})
        return signale
