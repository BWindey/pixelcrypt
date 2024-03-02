from PIL import Image
from loadThemeFile import loadThemeFile


def loadImage(path="image.png", key="themes.toml"):
    theme = loadThemeFile()

    image = Image.open(path)

    print("Image format:", image.format)
    print("Image size:", image.size)
    print("Image mode:", image.mode)

    image.show()


loadImage(input())
