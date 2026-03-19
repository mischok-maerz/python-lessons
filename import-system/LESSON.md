# Python Import-System: Code auslagern und nutzen

In dieser Lektion lernst du, wie du deinen Python-Code übersichtlicher gestaltest, indem du Funktionen in eigene Dateien auslagerst.

## 1. Eine Hilfsdatei erstellen (`math_utils.py`)

Zuerst erstellen wir eine Datei, die eine nützliche Funktion enthält. Wir nennen sie "Modul".

```python
# math_utils.py
def addiere(a, b):
    """Gibt die Summe von zwei Zahlen zurück."""
    return a + b
```

## 2. Das Modul im Hauptprogramm nutzen (`main.py`)

Nun erstellen wir unsere Hauptdatei. Hier "importieren" wir den Code aus der anderen Datei.

```python
# main.py
# Wir importieren das gesamte Modul
import math_utils

# Jetzt können wir auf die Funktionen darin zugreifen
ergebnis = math_utils.addiere(5, 3)

print(f"Das Ergebnis der Addition ist: {ergebnis}")
```

## 3. Alternative Art zu importieren (`main_alt.py`)

Es gibt auch eine zweite Methode, bei der wir nur die spezifische Funktion importieren. Das macht den Code oft etwas kürzer.

```python
# main_alt.py
# Wir importieren nur die gewünschte Funktion
from math_utils import addiere

# Jetzt können wir die Funktion direkt aufrufen, ohne den Modulnamen davor zu schreiben
ergebnis = addiere(10, 20)

print(f"Das Ergebnis der direkten Addition ist: {ergebnis}")
```

## Zusammenfassung

1.  **Erstelle ein Modul:** Speichere Funktionen oder Variablen in einer separaten `.py`-Datei (z.B. `math_utils.py`).
2.  **Importiere es:** Nutze `import name_des_moduls` (ohne die Endung `.py`), um den Code in deiner Hauptdatei verfügbar zu machen.
3.  **Greife darauf zu:** Rufe die Funktionen mit `name_des_moduls.funktionsname()` auf.

Dies hilft dir, deinen Code in logische Teile zu unterteilen und große Programme besser zu organisieren.
