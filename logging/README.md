# Python Logging für Anfänger 🪵

In dieser Lektion lernst du, wie du das `logging`-Modul in Python nutzt, um den Ablauf deiner Programme professionell zu überwachen.

## 1. Warum nicht einfach `print()`?
`print()` ist super für schnelles Debugging, hat aber Nachteile:
- **Keine Prioritäten:** Alles landet im selben Stream.
- **Schwer zu filtern:** Du musst `print`-Befehle manuell löschen, bevor das Programm "fertig" ist.
- **Keine Metadaten:** Du siehst nicht automatisch, *wann* oder *wo* (in welcher Zeile/Datei) die Ausgabe geschah.

## 2. Die 5 Log-Level
Logging kategorisiert Nachrichten nach Wichtigkeit:
1. `DEBUG`: Sehr detaillierte Infos für die Fehlersuche (z.B. Variablenwerte).
2. `INFO`: Bestätigung, dass alles nach Plan läuft (z.B. "Server gestartet").
3. `WARNING`: Etwas Unerwartetes ist passiert, aber das Programm läuft noch.
4. `ERROR`: Ein schwereres Problem, eine Funktion ist fehlgeschlagen.
5. `CRITICAL`: Ein fataler Fehler, das Programm muss wahrscheinlich beendet werden.

## 3. Die Basiskonfiguration
Mit `logging.basicConfig()` legst du fest, wie geloggt wird:
- `level`: Ab welcher Wichtigkeit sollen Nachrichten angezeigt werden? (Standard ist WARNING).
- `format`: Wie sieht die Zeile aus? (Zeitstempel, Level, Nachricht).
- `filename`: (Optional) Schreibt die Logs in eine Datei statt in die Konsole.

## 4. Best Practices
- Nutze **F-Strings** für Variablen: `logger.info(f"User {name} eingeloggt")`.
- Nutze `__name__`: Damit weißt du immer, aus welchem Modul der Log kommt.
