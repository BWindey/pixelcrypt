from PIL import Image


def stringToBinary(string):
    return list(ord(i) for i in string)


print(stringToBinary(input()))


def generateImage(size):
    image = Image.new("RGB", (size, size), "white")
    image.save("image.png")


generateImage(int(input()))
