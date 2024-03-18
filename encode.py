from PIL import Image

from loadThemeFile import loadThemeFile


# returns a list with ascii values from a string
def stringToAscii(string):
    return list(ord(i) for i in string)


# fills the rows with transcoded data, and stacks it so it's a square
def generateImage(asciiValues):
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

        # Fill the entire column with the pixel color
        for y in range(size):
            image.putpixel((x, y), pixel_color)

    try:
        image.save("image.png")
    except IOError as e:
        print(f"Error saving the image: {e}")


clearText = input("message to encode: ")
imageSize = len(clearText)
asciiText = stringToAscii(clearText)
print(asciiText)
theme = loadThemeFile()

generateImage(asciiText)
