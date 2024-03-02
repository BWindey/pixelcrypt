from PIL import Image


def stringToAscii(string):
    return list(ord(i) for i in string)


def generateImage(size, asciiValues):
    image = Image.new("RGB", (size, size), "white")

    width, height = size

    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), ())

    image.save("image.png")


clearText = input("message to encode: ")
imageSize = len(clearText)
asciiText = stringToAscii(clearText)

generateImage(imageSize, asciiText)
