from PIL import Image
from loadThemeFile import load_theme_file


def load_image(path="image.png", key="themes.toml"):
    theme = load_theme_file()
    image = Image.open(path)

    # debug information
    print("-" * 30)
    print("format:", image.format)
    print("size:", image.size)
    print("mode:", image.mode)
    print("-" * 30)

    width, _ = image.size

    # Retrieve RGB values of pixels in the first row
    pixels_first_row_rgb = [image.getpixel((x, 0)) for x in range(width)]

    keys = []
    for rgb_value in pixels_first_row_rgb:
        keys.append(
            chr(int([key for key, value in theme.items() if tuple(value) == tuple(rgb_value)][0]))
        )

    # Filter out None values and concatenate the keys into a single string
    keys_str = "".join(key for key in keys if key is not None)

    print("-" * 50)
    print(keys_str)


if __name__ == "__main__":
    load_image(input("image name (default in same dir is image.png): "))
