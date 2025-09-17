import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

infile = sys.argv[1]
outfile = sys.argv[2]


allowed = {".jpg", ".jpeg", ".png"}
in_ext = os.path.splitext(infile)[1].lower()
out_ext = os.path.splitext(outfile)[1].lower()

if in_ext not in allowed:
    sys.exit("Invalid input")
if out_ext not in allowed:
    sys.exit("Invalid output")
if in_ext != out_ext:
    sys.exit("Input and output have different extensions")


try:
    shirt = Image.open("shirt.png") #overlay
    with Image.open(infile) as img: #open input image
        fitted = ImageOps.fit(img, shirt.size) #resize/crop to shirt size
        fitted.paste(shirt, (0, 0), shirt) #overlay using shirt as mask
        fitted.save(outfile) #write result
except FileNotFoundError:
    sys.exit("Input does not exist")
