import toml

from validate_theme_toml import checker


# loads the theme file and returns it's data
def load_theme_file():
    checker("themes.toml")  # validate encryption key
    with open("themes.toml", "r") as file:
        data = toml.load(file)

    return data["theme"]["rainbow"]
