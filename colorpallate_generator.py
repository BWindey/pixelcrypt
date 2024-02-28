import colorsys
import toml


def generate_color_palette(theme_name):
    palette = []
    ascii_size = 127  # there are 127 characters in the base ASCII implementation
    hue_step = 1.0 / ascii_size

    for i in range(ascii_size):
        h = i * hue_step
        rgb_color = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        scaled_rgb = tuple(int(x * 255) for x in rgb_color)  # Scale RGB values to 0-255
        palette.append(scaled_rgb)
    return palette


def append_theme_to_toml(theme_name, palette):
    # Load existing themes from themes.toml
    try:
        with open("themes.toml", "r") as f:
            themes = toml.load(f)
    except FileNotFoundError:
        themes = {}

        themes["theme"][theme_name] = {chr(i): color for i, color in enumerate(palette)}

    # Write the updated dictionary back to themes.toml
    with open("themes.toml", "w") as f:
        toml.dump(themes, f)


# Prompt user for theme name
theme_name = input("Please give your theme a name: ")

# Generate color palette
palette = generate_color_palette(theme_name)

# Append theme to themes.toml
append_theme_to_toml(theme_name, palette)

print("Theme '{}' has been added to themes.toml.".format(theme_name))
