from abc import ABC


class ImageMode(ABC):
    def apply(self, ascii_values: list, image, theme, size: int) -> None:
        pass


class DiagonalMode(ImageMode):
    def apply(self, ascii_values, image, theme, size: int) -> None:
        for x, ascii_val in enumerate(ascii_values):
            pixel_color = tuple(theme[str(ascii_val)])

            # Ensure that the color is a list
            if not isinstance(pixel_color, tuple):
                raise ValueError("Invalid color format in theme file")

            # Fill first row with encoded message, then apply a shift for subsequent rows
            for y in range(size):
                image.putpixel(((x + y) % size, y), pixel_color)

        return image
