# haupt.py

from daten.daten_abruf import DatenAbruf
from strategie.strategie import Strategie
from ausfuehrung.handels_ausfuehrer import HandelsAusfuehrer
from risikomanagement.risiko_manager import RisikoManager
from protokollierung.protokollierer import Protokollierer
import time

def main():
    # Komponenten initialisieren
    daten_abruf = DatenAbruf()
    strategie = Strategie()
    handels_ausfuehrer = HandelsAusfuehrer()
    risiko_manager = RisikoManager()
    protokollierer = Protokollierer()

    # Haupt-Handelsschleife
    while True:
        # Marktdaten abrufen
        marktdaten = daten_abruf.abrufen()

        # Handelssignale generieren
        signale = strategie.signale_generieren(marktdaten)

        # Risiko managen und Signale anpassen
        signale = risiko_manager.signale_anpassen(signale)

        # Trades ausführen
        handels_ausfuehrer.trades_ausfuehren(signale)

        # Aktionen protokollieren
        protokollierer.protokollieren(signale)

        # Schlafen oder bis zur nächsten Iteration warten
        time.sleep(60)  # Platzhalter für Timing-Logik

if __name__ == "__main__":
    main()
