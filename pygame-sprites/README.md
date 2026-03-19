# Pygame Lektion: Ein Sprite für unseren Helden

In dieser Lektion lernen wir, wie man eine eigene Grafik (ein Sprite) für den Helden in ein Pygame-Spiel einbaut. Wir gehen dabei den Weg von der Bildersuche über die Bearbeitung bis hin zum fertigen Code.

## 1. Das passende Bild finden

Bevor wir programmieren, brauchen wir eine Grafik.

*   **Download:** Suche dir ein Bild für deinen Helden im Internet (z.B. auf Seiten wie [OpenGameArt.org](https://opengameart.org/)).
*   **Wichtig – Lizenzen:** Achte unbedingt auf die Lizenz des Bildes! Verwende nur Bilder, die für die Nutzung freigegeben sind (z.B. CC0 oder CC-BY).

## 2. Bildbearbeitung mit GIMP

Damit das Bild im Spiel gut aussieht, müssen wir es vorbereiten. Wir nutzen dazu das kostenlose Tool **GIMP**.

1.  **Skalieren:** Wenn das Bild zu groß ist, passe die Größe an.
    *   Gehe auf: **Bild -> Bild skalieren**.
    *   Gib die gewünschte Breite oder Höhe ein (z.B. 64x64 Pixel).
2.  **Transparenz:** Oft haben Bilder einen weißen oder einfarbigen Hintergrund. Dieser soll im Spiel unsichtbar sein.
    *   Wähle den Hintergrund mit dem Zauberstab-Werkzeug aus.
    *   Drücke **Entf** (Entfernen), um den Hintergrund zu löschen (er sollte nun ein graues Karomuster zeigen).
    *   *Hinweis:* Falls kein Karomuster erscheint, klicke rechts auf die Ebene und wähle "Alpha-Kanal hinzufügen".
3.  **Exportieren:** Speichere das Bild im richtigen Format.
    *   Gehe auf: **Datei -> Exportieren als...**
    *   Wähle einen Namen wie `luigi.png` (wichtig: die Endung **.png** unterstützt Transparenz).
    *   Speichere das Bild in einem Unterordner deines Projekts namens `img/`.

## 3. Code-Einbindung in Pygame

Nun bringen wir den Helden auf den Bildschirm.

### Schritt A: Bild laden
Bevor die Spielschleife beginnt, müssen wir das Bild in den Speicher laden. Wir nutzen `.convert_alpha()`, damit die Transparenz korrekt verarbeitet wird.

```python
# Vor der Hauptschleife laden wir das Bild
player = pygame.image.load('img/luigi.png').convert_alpha()
```

### Schritt B: Bild zeichnen
In der Hauptschleife (Main Loop) wird das Bild in jedem Frame neu gezeichnet.

```python
# In der Hauptschleife des Spiels
# posX und posY sind die aktuellen Koordinaten deines Helden
DISPLAYSURF.blit(player, (posX, posY))
```

---

## Vollständiges Beispiel

Hier siehst du, wie der Code in einem einfachen Grundgerüst aussieht:

```python
import pygame
import sys

# Initialisierung
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Mein erstes Sprite-Spiel')

# Konstanten und Variablen
posX = 100
posY = 100
HERO_WIDTH = 64 # Beispielwert

# 1. Bild laden (VOR der Schleife)
try:
    player = pygame.image.load('img/luigi.png').convert_alpha()
except:
    # Falls das Bild fehlt, erstellen wir ein rotes Rechteck als Ersatz
    player = pygame.Surface((HERO_WIDTH, HERO_WIDTH))
    player.fill((255, 0, 0))

# Hauptschleife
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Hintergrund zeichnen
    DISPLAYSURF.fill((255, 255, 255))

    # 2. Bild zeichnen (IN der Schleife)
    DISPLAYSURF.blit(player, (posX, posY))

    pygame.display.update()
```

Viel Erfolg beim Einbauen deines Helden!
