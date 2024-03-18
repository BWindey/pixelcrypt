from PIL import Image
import argparse

from loadThemeFile import loadThemeFile


# returns a list with ascii values from a string
def stringToAscii(string):
    return list(ord(i) for i in string)


# fills the rows with transcoded data, and stacks it so it's a square
def generateImage(asciiValues: list, fileName: str) -> None:
    size = len(asciiValues)
    image = Image.new("RGB", (size, size), "white")
    theme = loadThemeFile()

    for x, ascii_val in enumerate(asciiValues):
        ascii_str = str(ascii_val)

        color = theme[ascii_str]
        # Ensure that the color is a list
        if not isinstance(color, list):
            raise ValueError("Invalid color format in theme file")

        # Extract RGB values from the list
        pixel_color = tuple(color)
        # print debug info
        print(f"    {clearText[x]} ➡️ {ascii_val} ➡️ {pixel_color}")

        # Fill the entire column with the pixel color
        for y in range(size):
            image.putpixel((x, y), pixel_color)

    try:
        image.save(f"{fileName}.png")
        print(f"\nEncoded image saved succesfully under {fileName}.png\n")
    except IOError as e:
        print(f"Error saving the image: {e}")


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
