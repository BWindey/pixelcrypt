from PIL import Image

from loadThemeFile import load_theme_file


def string_to_ascii(string):  # returns a list with ascii values from a string
    return list(ord(i) for i in string)


# fills the rows with transcoded data, and stacks it, so it's a square
def generate_image(ascii_values, save_location="image.png"):
    size = len(ascii_values)
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

        # Fill the entire column with the pixel color
        for y in range(size):
            image.putpixel(((x + y) % size, y), pixel_color)

    image.save(save_location)


if __name__ == "__main__":
    clearText = input("message to encode: ")
    save_location = input("File to save to: ")

    imageSize = len(clearText)
    asciiText = string_to_ascii(clearText)
    theme = load_theme_file()

    generate_image(asciiText, save_location)
