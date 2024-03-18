def rgb_to_terminal_color(RGB):
    """
    Approximate RGB values to a terminal color index.
    """
    # Convert RGB to a colorama color
    # Determine the closest ANSI color for each channel
    r, g, b = RGB
    closest_r = round(r / 255 * 5)
    closest_g = round(g / 255 * 5)
    closest_b = round(b / 255 * 5)
    # Convert ANSI color to colorama color code
    ansi_color_code = 16 + 36 * closest_r + 6 * closest_g + closest_b
    return ansi_color_code


def colored_square(rgb: tuple):
    # Convert RGB to terminal color index
    color_code = rgb_to_terminal_color(rgb)
    # Print a square using Unicode block characters
    return f"\033[48;5;{color_code}m  \033[0m"


# Example usage
if __name__ == "__main__":
    colored_square((255, 0, 0))  # Red square
    colored_square((0, 255, 0))  # Green square
    colored_square((0, 0, 255))  # Blue square
