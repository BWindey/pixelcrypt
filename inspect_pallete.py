import toml
import matplotlib.pyplot as plt

# Load color palette from TOML file

themefile = input("Please enter your theme file (no extension)") + ".toml"

with open(themefile, "r") as f:
    color_data = toml.load(f)

# Extract color values from the TOML data
colors = [
    color_data["theme"]["theme"][char] for char in sorted(color_data["theme"]["theme"])
]

# Create a plot to display the colors
fig, ax = plt.subplots(figsize=(10, 1))
for i, color in enumerate(colors):
    ax.bar(i, 1, color=[comp / 255 for comp in color], edgecolor="none")

ax.set_xticks([])
ax.set_yticks([])
plt.show()
