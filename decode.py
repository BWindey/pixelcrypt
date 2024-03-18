from PIL import Image
from loadThemeFile import loadThemeFile
import sys


def loadImage(path="image.png", key="themes.toml"):
    theme = loadThemeFile()
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
        for key, theme_rgb in theme.items():
            # Check if the RGB values are within a certain tolerance
            if all(abs(a - b) <= 5 for a, b in zip(rgb_value, theme_rgb)):
                keys.append(chr(int(key)))
                break

    #  concatenate the keys into a single string
    keys_str = "".join(key for key in keys)

    print(f"\ndecoded message: {keys_str}\n")


loadImage(sys.argv[1])
