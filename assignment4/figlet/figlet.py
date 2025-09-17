import pyfiglet
import sys
import random
from pyfiglet import FigletFont

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        fonts = FigletFont.getFonts()
        if sys.argv[2] in fonts:
            words = input("What do you want to say?: ")
            font = sys.argv[2]
            print(pyfiglet.figlet_format(words, font=font))
        else:
            sys.exit("Enter a valid font!")
    else:
        sys.exit("Enter a valid font!")
if len(sys.argv) == 1:
    words = input("What do you want to say?: ")
    fonts = FigletFont.getFonts()
    font = random.choice(fonts)
    print(pyfiglet.figlet_format(words, font=font))
if len(sys.argv) == 2:
    sys.exit("Enter a valid font!")



