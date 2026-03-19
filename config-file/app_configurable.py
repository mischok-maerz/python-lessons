import yaml

def start_app():
    # 1. Konfiguration laden (ohne try-except)
    file = open("config.yaml", "r", encoding="utf-8")
    config = yaml.safe_load(file)
    file.close()
    
    # 2. Den Wert für die Hintergrundfarbe auslesen
    ui_config = config["ui"]
    bg_color = ui_config["background_color"]
    
    # 3. Atomische Werte für Breite und Höhe auslesen
    width = ui_config["width"]
    height = ui_config["height"]
    
    print(f"--- App gestartet ---")
    print(f"Hintergrundfarbe: {bg_color}")
    print(f"Fensterbreite:   {width}px")
    print(f"Fensterhöhe:    {height}px")

if __name__ == "__main__":
    start_app()
