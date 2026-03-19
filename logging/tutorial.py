import logging

# 1. KONFIGURATION
# Wir legen fest: WAS wir loggen (ab DEBUG), WIE es aussieht und WO es landet.
# Wir fügen 'filename' hinzu, um die Logs dauerhaft zu speichern.
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    filename='game.log',  # Speichert in dieser Datei
    filemode='a'          # 'a' für append (anhängen), 'w' für overwrite (überschreiben)
)

# 2. LOGGER ERSTELLEN
# Es ist Best Practice, einen Logger mit dem Modulnamen zu erstellen.
logger = logging.getLogger(__name__)

# --- DAS SPIEL BEGINNT ---

def spiel_starten(name):
    logger.info(f"--- Spiel gestartet für {name} ---")
    
    posX = 0
    posY = 0
    
    # DEBUG-Meldungen helfen uns, den internen Zustand zu sehen
    logger.debug(f"Startposition: ({posX}, {posY})")
    
    # Eine kleine Logik mit Warnung
    gefahr_nahe = True
    if gefahr_nahe:
        logger.warning("Gefahr in Verzug! Ein Koopa nähert sich.")

    # ERROR-Logging bei Fehlern (z.B. Division durch Null)
    try:
        punkte = 100 / 0 # Provozieren eines Fehlers
    except ZeroDivisionError:
        logger.error("Fehler bei der Punkteberechnung: Division durch Null!")

if __name__ == "__main__":
    spiel_starten("Luigi")
    print("Das Programm läuft. Schau in die Datei 'game.log' für die Ergebnisse!")
