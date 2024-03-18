import toml


# loads the theme file and returns its data
def loadThemeFile():
    try:
        with open("themes.toml", "r") as file:
            data = toml.load(file)
            theme = data.get("theme", {}).get("rainbow", None)
            if theme is None:
                raise ValueError("Theme 'rainbow' not found in the theme file.")
            return theme

    except FileNotFoundError:
        print("Error: Theme file 'themes.toml' not found.")
    except Exception as e:
        print(f"An error occurred while loading the theme file: {e}")
