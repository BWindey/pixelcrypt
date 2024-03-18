from PIL import Image
import argparse

from loadThemeFile import load_theme_file


def string_to_ascii(string):  # returns a list with ascii values from a string
    return list(ord(i) for i in string)


# fills the rows with transcoded data, and stacks it so it's a square
def generateImage(asciiValues: list, fileName: str, modus=str) -> None:
    # modus wordt een object die een image vult op basis van diens specificaties. Hiermee kan gemakkelijk een patroon gespecifieerd worden, en het is modulair. bv. vertical, diagonaal, spiral, random
    size = len(asciiValues)
    image = Image.new("RGB", (size, size), "white")
    theme = load_theme_file()

    for x, ascii_val in enumerate(ascii_values):
        ascii_str = str(ascii_val)

        color = theme[ascii_str]
        # Ensure that the color is a list
        if not isinstance(color, list):
            raise ValueError("Invalid color format in theme file")

        # Extract RGB values from the list
        pixel_color = tuple(color)
        # print debug info
        print(f"    {clearText[x]} ➡️ {str(ascii_val).zfill(3)} ➡️ {pixel_color}")

        # Fill the entire column with the pixel color
        for y in range(size):
            image.putpixel(((x + y) % size, y), pixel_color)

    try:
        image.save(f"{fileName}.png")
        print(f"\nEncoded image saved succesfully under {fileName}.png\n")
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


    clearText = args.message
    fileName = args.fileName

    asciiText = stringToAscii(clearText)
    print(f"\nascii values: {asciiText}\n")
    theme = loadThemeFile()

    generateImage(asciiText, fileName)
