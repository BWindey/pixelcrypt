import toml


def check_duplicate_values(theme_file):
    theme_data = toml.load(theme_file)
    all_values = set()
    duplicates = []

    for theme_name, theme_values in theme_data.items():
        for ascii_value, color_values in theme_values.items():
            color_tuple = tuple(color_values)
            if color_tuple in all_values:
                duplicates.append((theme_name, ascii_value))
            else:
                all_values.add(color_tuple)

    return duplicates


def checker(theme_file: str):
    duplicate_rows = check_duplicate_values(theme_file)

    if duplicate_rows:
        print("Warning: duplicate rows found:")
        for theme_name, ascii_value in duplicate_rows:
            print(f"Theme: {theme_name}, ASCII Value: {ascii_value}")

        print(
            "\nproper encoding and decoding cannot be guaranteed with improper key theme file\n"
        )
    else:
        print(
            f"Encryption key {theme_file} evaluated succesfully: no duplicate rows found!\n"
        )


if __name__ == "__main__":
    checker("themes.toml")
