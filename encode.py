import argparse

from PIL import Image

from color import colored_square
from modes import DiagonalMode, ImageMode, VerticalMode  # all encryption modes
from loadThemeFile import load_theme_file


def string_to_ascii(string):  # returns a list with ascii values from a string
    return list(ord(i) for i in string)


# fills the rows with transcoded data, and stacks it, so it's a square
def generate_image(
    clear_text: str,
    ascii_values: list,
    file_name: str,
    encryption_mode: ImageMode,
) -> None:
    size = len(ascii_values)
    image = Image.new("RGB", (size, size), "white")
    theme = load_theme_file()

    # purely aesthetic conversion printing
    for x, ascii_val in enumerate(ascii_values):
        pixel_color = tuple(theme[str(ascii_val)])
        print(
            f"{clear_text[x]} ➡️ {str(ascii_val).zfill(3)} ➡️ {colored_square(pixel_color)} {pixel_color}"
        )

    image = encryption_mode.apply(ascii_values, image, theme, size)

    print("\nAttemting file save")
    try:
        image.save(f"{file_name}.png")
        print(f"Encoded image saved succesfully as {file_name}.png")
    except IOError as e:
        print(f"Error saving the image: {e}")
        print(e.strerror)


if __name__ == "__main__":
    modes = {
        "diagonal": DiagonalMode(),
        "vertical_bars": VerticalMode(),
    }

    arguments = [
        {"flags": ["-t", "--text"], "help": "message to encrypt"},
        {"flags": ["-f", "--file"], "help": "image name"},
        {"flags": ["-m", "--mode"], "help": "image encryption mode"},
    ]
    parser = argparse.ArgumentParser(description="text -> image")

    parser.add_argument("mode", metavar="mode", type=str, help="encryption mode")

    for arg in arguments:
        parser.add_argument(*arg["flags"], help=arg["help"])

    args = parser.parse_args()

    fileName = args.file
    mode = args.mode
    text = args.text

    asciiText = string_to_ascii(text)
    print(f"\nascii values: {asciiText}\n")

    generate_image(text, asciiText, fileName, modes[mode])
