from PIL import Image
import imgkit
from bs4 import BeautifulSoup

# Render HTML to PNG
imgkit.from_file("web/index.html", "assets/site.png")

# Convert PNG to SVG wrapper
img = Image.open("assets/site.png")
img.save("assets/site.svg")

# Inject internal glow + style aura
with open("assets/site.svg", "r") as f:
    soup = BeautifulSoup(f, "xml")

style = soup.new_tag("style")
style.string = """
svg { background:#050908; }
"""
soup.svg.insert(0, style)

with open("assets/site.svg", "w") as f:
    f.write(str(soup))
