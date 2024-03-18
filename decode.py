from PIL import Image
from loadThemeFile import load_theme_file
import sys


def load_image(path="image.png", key="themes.toml"):
    theme = load_theme_file()
    image = Image.open(path)

    # debug information
    print("-" * 15)
    print(f"image: {path}")
    print(f"key: {key}")
    print("format:", image.format)
    print("size:", image.size)
    print("mode:", image.mode)
    print("-" * 15)

    width, _ = image.size

    # Retrieve RGB values of pixels in the first row
    pixels_first_row_rgb = [image.getpixel((x, 0)) for x in range(width)]

    keys = []
    for rgb_value in pixels_first_row_rgb:
        keys.append(
            chr(int([key for key, value in theme.items() if tuple(value) == tuple(rgb_value)][0]))
        )

    #  concatenate the characters into a single string
    decodedMessage = "".join(key for key in keys)

    print(f"\ndecoded message: {decodedMessage}\n")


if __name__ == "__main__":
    load_image(sys.argv[1])
