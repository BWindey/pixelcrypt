import toml


# loads the theme file and returns it's data
def load_theme_file():
    with open("themes.toml", "r") as file:
        data = toml.load(file)

    return data["theme"]["rainbow"]
