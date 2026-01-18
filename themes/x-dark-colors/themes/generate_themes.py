import json
import os
import re

TEMPLATES_DIR = "/Users/xscriptor_1/Documents/repos/xscriptordev/vscode/themes/x-dark-colors/themes"
TEMPLATE_FILE = os.path.join(TEMPLATES_DIR, "x-medellin.json") # Using Medellin (formerly Candy) as template

PALETTES = {
    # Batch 1 (Already generated, keeping for reference or re-gen if needed)
    "Kyoto": {
        "color0":  "#0f111a", "color1":  "#007acc", "color2":  "#007acc", "color3":  "#007acc",
        "color4":  "#007acc", "color5":  "#007acc", "color6":  "#007acc", "color7":  "#e6f3ff",
        "color8":  "#414d66", "color9":  "#3399ff", "color10": "#3399ff", "color11": "#3399ff",
        "color12": "#3399ff", "color13": "#3399ff", "color14": "#3399ff", "color15": "#ffffff"
    },
    "Marrakech": {
        "color0":  "#1a0f0f", "color1":  "#cc3300", "color2":  "#cc3300", "color3":  "#cc3300",
        "color4":  "#cc3300", "color5":  "#cc3300", "color6":  "#cc3300", "color7":  "#ffe6e6",
        "color8":  "#664141", "color9":  "#ff6633", "color10": "#ff6633", "color11": "#ff6633",
        "color12": "#ff6633", "color13": "#ff6633", "color14": "#ff6633", "color15": "#ffffff"
    },
    "Reykjavik": {
        "color0":  "#0f1a1a", "color1":  "#008080", "color2":  "#008080", "color3":  "#008080",
        "color4":  "#008080", "color5":  "#008080", "color6":  "#008080", "color7":  "#e6ffff",
        "color8":  "#416666", "color9":  "#00b3b3", "color10": "#00b3b3", "color11": "#00b3b3",
        "color12": "#00b3b3", "color13": "#00b3b3", "color14": "#00b3b3", "color15": "#ffffff"
    },
    "Cairo": {
        "color0":  "#1a1a0f", "color1":  "#cc9900", "color2":  "#cc9900", "color3":  "#cc9900",
        "color4":  "#cc9900", "color5":  "#cc9900", "color6":  "#cc9900", "color7":  "#ffffe6",
        "color8":  "#666641", "color9":  "#ffcc00", "color10": "#ffcc00", "color11": "#ffcc00",
        "color12": "#ffcc00", "color13": "#ffcc00", "color14": "#ffcc00", "color15": "#ffffff"
    },
    "Rio": {
        "color0":  "#0a1a0a", "color1":  "#ff3399", "color2":  "#00cc44", "color3":  "#ff3399",
        "color4":  "#00cc44", "color5":  "#ff3399", "color6":  "#00cc44", "color7":  "#e6ffe6",
        "color8":  "#416641", "color9":  "#ff66b2", "color10": "#33ff77", "color11": "#ff66b2",
        "color12": "#33ff77", "color13": "#ff66b2", "color14": "#33ff77", "color15": "#ffffff"
    },
    "Athens": {
        "color0":  "#0a0a1a", "color1":  "#ff6600", "color2":  "#0066ff", "color3":  "#ff6600",
        "color4":  "#0066ff", "color5":  "#ff6600", "color6":  "#0066ff", "color7":  "#e6e6ff",
        "color8":  "#414166", "color9":  "#ff9933", "color10": "#3399ff", "color11": "#ff9933",
        "color12": "#3399ff", "color13": "#ff9933", "color14": "#3399ff", "color15": "#ffffff"
    },
    "Istanbul": {
        "color0":  "#1a0a1a", "color1":  "#ffcc00", "color2":  "#6600cc", "color3":  "#ffcc00",
        "color4":  "#6600cc", "color5":  "#ffcc00", "color6":  "#6600cc", "color7":  "#f2e6ff",
        "color8":  "#554166", "color9":  "#ffda4d", "color10": "#9933ff", "color11": "#ffda4d",
        "color12": "#9933ff", "color13": "#ffda4d", "color14": "#9933ff", "color15": "#ffffff"
    },
    "Sidney": {
        "color0":  "#001a1a", "color1":  "#ff6666", "color2":  "#009999", "color3":  "#ff6666",
        "color4":  "#009999", "color5":  "#ff6666", "color6":  "#009999", "color7":  "#e6ffff",
        "color8":  "#416666", "color9":  "#ff9999", "color10": "#00cccc", "color11": "#ff9999",
        "color12": "#00cccc", "color13": "#ff9999", "color14": "#00cccc", "color15": "#ffffff"
    },
    # Batch 2
    "Paris": {
        "color0":  "#1e1e24", "color1":  "#e6adac", "color2":  "#92a1cf", "color3":  "#e6adac",
        "color4":  "#92a1cf", "color5":  "#e6adac", "color6":  "#92a1cf", "color7":  "#f0f0f5",
        "color8":  "#5b5b66", "color9":  "#ffcccc", "color10": "#b3c2f2", "color11": "#ffcccc",
        "color12": "#b3c2f2", "color13": "#ffcccc", "color14": "#b3c2f2", "color15": "#ffffff"
    },
    "London": {
        "color0":  "#1a1a1a", "color1":  "#cc0000", "color2":  "#808080", "color3":  "#cc0000",
        "color4":  "#808080", "color5":  "#cc0000", "color6":  "#808080", "color7":  "#e6e6e6",
        "color8":  "#4d4d4d", "color9":  "#ff3333", "color10": "#a6a6a6", "color11": "#ff3333",
        "color12": "#a6a6a6", "color13": "#ff3333", "color14": "#a6a6a6", "color15": "#ffffff"
    },
    "Barcelona": {
        "color0":  "#001a33", "color1":  "#ffcc00", "color2":  "#0099ff", "color3":  "#ffcc00",
        "color4":  "#0099ff", "color5":  "#ffcc00", "color6":  "#0099ff", "color7":  "#e6f7ff",
        "color8":  "#336699", "color9":  "#ffe066", "color10": "#33adff", "color11": "#ffe066",
        "color12": "#33adff", "color13": "#ffe066", "color14": "#33adff", "color15": "#ffffff"
    },
    "Rome": {
        "color0":  "#1a0f1a", "color1":  "#660066", "color2":  "#cc9900", "color3":  "#660066",
        "color4":  "#cc9900", "color5":  "#660066", "color6":  "#cc9900", "color7":  "#f9e6ff",
        "color8":  "#4d2e4d", "color9":  "#993399", "color10": "#e6ac00", "color11": "#993399",
        "color12": "#e6ac00", "color13": "#993399", "color14": "#e6ac00", "color15": "#ffffff"
    },
    "Berlin": {
        "color0":  "#0d0d0d", "color1":  "#39ff14", "color2":  "#ff00ff", "color3":  "#39ff14",
        "color4":  "#ff00ff", "color5":  "#39ff14", "color6":  "#ff00ff", "color7":  "#f2f2f2",
        "color8":  "#404040", "color9":  "#66ff4d", "color10": "#ff4dff", "color11": "#66ff4d",
        "color12": "#ff4dff", "color13": "#66ff4d", "color14": "#ff4dff", "color15": "#ffffff"
    },
    "Vienna": {
        "color0":  "#1a0d0d", "color1":  "#800020", "color2":  "#fffdd0", "color3":  "#800020",
        "color4":  "#fffdd0", "color5":  "#800020", "color6":  "#fffdd0", "color7":  "#fffef0",
        "color8":  "#4d2929", "color9":  "#b3002d", "color10": "#ffffe6", "color11": "#b3002d",
        "color12": "#ffffe6", "color13": "#b3002d", "color14": "#ffffe6", "color15": "#ffffff"
    },
    "Stockholm": {
        "color0":  "#0a1a2a", "color1":  "#005b96", "color2":  "#fecc00", "color3":  "#005b96",
        "color4":  "#fecc00", "color5":  "#005b96", "color6":  "#fecc00", "color7":  "#e6f2ff",
        "color8":  "#33557a", "color9":  "#3380b2", "color10": "#ffd633", "color11": "#3380b2",
        "color12": "#ffd633", "color13": "#3380b2", "color14": "#ffd633", "color15": "#ffffff"
    },
    "Oslo": {
        "color0":  "#0f1a26", "color1":  "#003366", "color2":  "#e6f7ff", "color3":  "#003366",
        "color4":  "#e6f7ff", "color5":  "#003366", "color6":  "#e6f7ff", "color7":  "#f0fbff",
        "color8":  "#3d5c7a", "color9":  "#336699", "color10": "#ffffff", "color11": "#336699",
        "color12": "#ffffff", "color13": "#336699", "color14": "#ffffff", "color15": "#ffffff"
    },
    "Helsinki": {
        "color0":  "#120a1a", "color1":  "#00cc66", "color2":  "#9933ff", "color3":  "#00cc66",
        "color4":  "#9933ff", "color5":  "#00cc66", "color6":  "#9933ff", "color7":  "#f2e6ff",
        "color8":  "#4d3366", "color9":  "#33ff99", "color10": "#b266ff", "color11": "#33ff99",
        "color12": "#b266ff", "color13": "#33ff99", "color14": "#b266ff", "color15": "#ffffff"
    },
    "Moscow": {
        "color0":  "#1a0505", "color1":  "#cc0000", "color2":  "#ffcc00", "color3":  "#cc0000",
        "color4":  "#ffcc00", "color5":  "#cc0000", "color6":  "#ffcc00", "color7":  "#ffcccc",
        "color8":  "#661a1a", "color9":  "#ff3333", "color10": "#ffd633", "color11": "#ff3333",
        "color12": "#ffd633", "color13": "#ff3333", "color14": "#ffd633", "color15": "#ffffff"
    },
    "Dubai": {
        "color0":  "#0a0a05", "color1":  "#cfb53b", "color2":  "#000000", "color3":  "#cfb53b",
        "color4":  "#000000", "color5":  "#cfb53b", "color6":  "#000000", "color7":  "#fffbe6",
        "color8":  "#4d451a", "color9":  "#e6c34d", "color10": "#333333", "color11": "#e6c34d",
        "color12": "#333333", "color13": "#e6c34d", "color14": "#333333", "color15": "#ffffff"
    },
    "Tokyo": {
        "color0":  "#110a1a", "color1":  "#ff00cc", "color2":  "#00ffff", "color3":  "#ff00cc",
        "color4":  "#00ffff", "color5":  "#ff00cc", "color6":  "#00ffff", "color7":  "#f9e6ff",
        "color8":  "#4d2e66", "color9":  "#ff33d6", "color10": "#33ffff", "color11": "#ff33d6",
        "color12": "#33ffff", "color13": "#ff33d6", "color14": "#33ffff", "color15": "#ffffff"
    },
    "Seoul": {
        "color0":  "#0f0f1a", "color1":  "#cd2e3a", "color2":  "#0047a0", "color3":  "#cd2e3a",
        "color4":  "#0047a0", "color5":  "#cd2e3a", "color6":  "#0047a0", "color7":  "#e6e6f2",
        "color8":  "#3b3b5c", "color9":  "#e64552", "color10": "#3373cc", "color11": "#e64552",
        "color12": "#3373cc", "color13": "#e64552", "color14": "#3373cc", "color15": "#ffffff"
    },
    "Mumbai": {
        "color0":  "#1a1205", "color1":  "#ff9933", "color2":  "#138808", "color3":  "#ff9933",
        "color4":  "#138808", "color5":  "#ff9933", "color6":  "#138808", "color7":  "#fff0e6",
        "color8":  "#664d1f", "color9":  "#ffb366", "color10": "#33cc22", "color11": "#ffb366",
        "color12": "#33cc22", "color13": "#ffb366", "color14": "#33cc22", "color15": "#ffffff"
    },
    "Bangkok": {
        "color0":  "#12051a", "color1":  "#800080", "color2":  "#ff8c00", "color3":  "#800080",
        "color4":  "#ff8c00", "color5":  "#800080", "color6":  "#ff8c00", "color7":  "#f2e6ff",
        "color8":  "#4d1f66", "color9":  "#b300b3", "color10": "#ffa64d", "color11": "#b300b3",
        "color12": "#ffa64d", "color13": "#b300b3", "color14": "#ffa64d", "color15": "#ffffff"
    },
    "Singapore": {
        "color0":  "#051a05", "color1":  "#009933", "color2":  "#ffffff", "color3":  "#009933",
        "color4":  "#ffffff", "color5":  "#009933", "color6":  "#ffffff", "color7":  "#e6ffe6",
        "color8":  "#1f6629", "color9":  "#33cc66", "color10": "#f2f2f2", "color11": "#33cc66",
        "color12": "#f2f2f2", "color13": "#33cc66", "color14": "#f2f2f2", "color15": "#ffffff"
    },
    "New York": {
        "color0":  "#1a1a1a", "color1":  "#f7b500", "color2":  "#708090", "color3":  "#f7b500",
        "color4":  "#708090", "color5":  "#f7b500", "color6":  "#708090", "color7":  "#e6e6e6",
        "color8":  "#4d4d4d", "color9":  "#ffcd33", "color10": "#8ca6bf", "color11": "#ffcd33",
        "color12": "#8ca6bf", "color13": "#ffcd33", "color14": "#8ca6bf", "color15": "#ffffff"
    },
    "Chicago": {
        "color0":  "#0d131a", "color1":  "#4682b4", "color2":  "#a9a9a9", "color3":  "#4682b4",
        "color4":  "#a9a9a9", "color5":  "#4682b4", "color6":  "#a9a9a9", "color7":  "#e6eef4",
        "color8":  "#364559", "color9":  "#6b9cc2", "color10": "#bfbfbf", "color11": "#6b9cc2",
        "color12": "#bfbfbf", "color13": "#6b9cc2", "color14": "#bfbfbf", "color15": "#ffffff"
    },
    "San Francisco": {
        "color0":  "#1a0d0a", "color1":  "#c0362c", "color2":  "#cfd8dc", "color3":  "#c0362c",
        "color4":  "#cfd8dc", "color5":  "#c0362c", "color6":  "#cfd8dc", "color7":  "#f5eef0",
        "color8":  "#593633", "color9":  "#d15e55", "color10": "#eceff1", "color11": "#d15e55",
        "color12": "#eceff1", "color13": "#d15e55", "color14": "#eceff1", "color15": "#ffffff"
    },
    "Toronto": {
        "color0":  "#1a0a0a", "color1":  "#ff0000", "color2":  "#ffffff", "color3":  "#ff0000",
        "color4":  "#ffffff", "color5":  "#ff0000", "color6":  "#ffffff", "color7":  "#ffe6e6",
        "color8":  "#662929", "color9":  "#ff3333", "color10": "#f2f2f2", "color11": "#ff3333",
        "color12": "#f2f2f2", "color13": "#ff3333", "color14": "#f2f2f2", "color15": "#ffffff"
    }
}

# Candy colors map for replacement (Using standard template replacement strategy)
# Note: Since I'm using Medellin (was Candy) which might have different keys if I strictly follow the previous script logic.
# However, the previous script used 'x-dark-candy.json'. The user renamed it to 'x-medellin.json'.
# I'll check if 'x-medellin.json' exists. If not, I'll use another one. I'll rely on listing themes first if unsure, but I know user renamed them.
# I will use 'x-medellin.json' assuming it exists.

# I need to match the colors in x-medellin.json to color keys.
# Let's assume standard mapping based on the palette I extracted earlier for Medellin (Candy).
MEDELLIN_MAP = {
    "#000000": "color0",
    "#FF4C8B": "color1", 
    "#7FFFD4": "color2", 
    "#FFD84C": "color3", 
    "#00FFA8": "color4", 
    "#D36CFF": "color5", 
    "#47CFFF": "color6", 
    "#f7f1ff": "color7", 
    "#69676c": "color8"
}

def generate():
    if not os.path.exists(TEMPLATE_FILE):
        print(f"Template file not found: {TEMPLATE_FILE}")
        return

    with open(TEMPLATE_FILE, "r") as f:
        template_content = f.read()

    for city, colors in PALETTES.items():
        # Clean city name for filename (e.g. New York -> new-york)
        safe_city_name = city.lower().replace(" ", "-")
        filename = f"x-{safe_city_name}.json"
        
        # Skip if file already exists? No, overwrite to ensure consistency.
        
        new_content = template_content
        
        # 1. Textual Replacement
        for candy_hex, color_key in MEDELLIN_MAP.items():
            new_hex = colors[color_key]
            new_content = new_content.replace(candy_hex, new_hex)
        
        # Remove trailing commas (JSONC support)
        new_content = re.sub(r",(\s*[\}\]])", r"\1", new_content)

        # 2. Parse and Overwrite specific keys
        try:
            data = json.loads(new_content)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for {city}: {e}")
            continue
        
        # Update Name
        data["name"] = f"X {city}"
        
        # Update Terminal Colors Explicitly
        data["colors"]["terminal.ansiBlack"] = colors["color0"]
        data["colors"]["terminal.ansiRed"] = colors["color1"]
        data["colors"]["terminal.ansiGreen"] = colors["color2"]
        data["colors"]["terminal.ansiYellow"] = colors["color3"]
        data["colors"]["terminal.ansiBlue"] = colors["color4"]
        data["colors"]["terminal.ansiMagenta"] = colors["color5"]
        data["colors"]["terminal.ansiCyan"] = colors["color6"]
        data["colors"]["terminal.ansiWhite"] = colors["color7"]
        data["colors"]["terminal.ansiBrightBlack"] = colors["color8"]
        data["colors"]["terminal.ansiBrightRed"] = colors["color9"]
        data["colors"]["terminal.ansiBrightGreen"] = colors["color10"]
        data["colors"]["terminal.ansiBrightYellow"] = colors["color11"]
        data["colors"]["terminal.ansiBrightBlue"] = colors["color12"]
        data["colors"]["terminal.ansiBrightMagenta"] = colors["color13"]
        data["colors"]["terminal.ansiBrightCyan"] = colors["color14"]
        data["colors"]["terminal.ansiBrightWhite"] = colors["color15"]

        # Update Backgrounds to color0
        bg_keys = [
            "editor.background", "sideBar.background", "activityBar.background", 
            "statusBar.background", "titleBar.activeBackground", "titleBar.inactiveBackground",
            "panel.background", "terminal.background", "input.background", 
            "dropdown.background", "peekViewEditor.background", "peekViewResult.background",
            "editorGroupHeader.tabsBackground", "editorGroupHeader.noTabsBackground",
            "editorWidget.background", "notifications.background", "menu.background", "quickInput.background",
            "list.focusBackground", "list.hoverBackground", "list.inactiveFocusBackground",
            "tab.activeBackground", "tab.inactiveBackground", "tab.hoverBackground", "tab.unfocusedHoverBackground",
            "breadcrumbPicker.background"
        ]
        
        for k in bg_keys:
            if k in data["colors"]:
                data["colors"][k] = colors["color0"]
                
        # Write file
        filepath = os.path.join(TEMPLATES_DIR, filename)
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Generated {filename}")

if __name__ == "__main__":
    generate()
