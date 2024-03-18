import argparse

from PIL import Image

from encryption_modes import DiagonalMode, ImageMode  # all encryption modes
from loadThemeFile import load_theme_file


def string_to_ascii(string):  # returns a list with ascii values from a string
    return list(ord(i) for i in string)


# fills the rows with transcoded data, and stacks it, so it's a square
def generate_image(
    ascii_values: list,
    file_name: str,
    encryption_mode,
) -> None:
    size = len(ascii_values)
    image = Image.new("RGB", (size, size), "white")
    theme = load_theme_file()

    # purely aesthetic conversion printing
    for x, ascii_val in enumerate(ascii_values):
        pixel_color = tuple(theme[str(ascii_val)])
        print(f"{clear_text[x]} ➡️ {str(ascii_val).zfill(3)} ➡️ {pixel_color}")

    image = encryption_mode.apply(ascii_values, image, theme, size)

    print("\nAttemting file save")
    try:
        image.save(f"{file_name}.png")
        print(f"Encoded image saved succesfully under {file_name}.png")
    except IOError as e:
        print(f"Error saving the image: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="text -> image")

    parser.add_argument(
        "message", metavar="message", type=str, help="enter a message to encode"
    )

    parser.add_argument(
        "fileName", metavar="filename", type=str, help="filename of saved image"
    )

    args = parser.parse_args()

    clear_text = args.message
    fileName = args.fileName

    asciiText = string_to_ascii(clear_text)
    print(f"\nascii values: {asciiText}\n")

    generate_image(asciiText, fileName, encryption_mode=DiagonalMode())
