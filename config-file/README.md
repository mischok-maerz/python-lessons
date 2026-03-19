# Lesson 01: Konfigurationen in YAML auslagern

## Ziel
Lerne, wie du Einstellungen (Konfigurationen) von deinem Python-Code trennst. So kannst du zum Beispiel die Hintergrundfarbe deiner App ändern, ohne den Code anzufassen.

## Warum YAML?
YAML ist ein Format, das sowohl für Menschen leicht lesbar als auch für Computer einfach zu verarbeiten ist.

## Vorbereitung
Du benötigst die Bibliothek `PyYAML`. Installiere sie mit:
```bash
sudo apt install python3-yaml
```

## Die Dateien in dieser Lektion

### 1. `config.yaml`
Dies ist unsere "Datenbank" für Einstellungen. Wir haben separate Felder für `width` (Breite) und `height` (Höhe).

### 2. `app_configurable.py`
Das ist unser Python-Skript. Es liest die YAML-Datei beim Starten ein und nutzt die Werte daraus direkt über die Schlüssel.

## Deine Aufgabe
1. Öffne `config.yaml`.
2. Ändere den Wert von `background_color` zum Beispiel auf `"darkred"`.
3. Ändere die `width` auf `1280` und die `height` auf `720`.
4. Führe das Skript aus: `python app_configurable.py`.
5. Beachte, dass du das Skript nicht bearbeiten musstest, um die Farbe oder Größe zu ändern!

---
**Merksatz:** Code = Logik, Konfigurationsdatei = Daten/Einstellungen.
