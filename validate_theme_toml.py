if __name__ == "__main__":
    with open("themes.toml", 'r') as file:
        content = file.readlines()[1:]
    content = [e.split('=')[1].strip() for e in content]

    print("Valid theme file: ", len(set(content)) == len(content))
