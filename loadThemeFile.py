import os

import toml


# loads the theme file and returns it's data
def loadThemeFile():
    file_path = "themes.toml"
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Theme file '{file_path}' not found.")

    with open("file_path", "r") as file:
        data = toml.load(file)

    return data["theme"]["rainbow"]
