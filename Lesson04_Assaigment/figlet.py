import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv)==1:
    font_choice = choice(figlet.getFonts())
    figlet.setFont(font=font_choice)
    string = input("Input: ")
    print(figlet.renderText(string))

elif len(sys.argv)==3:
    if sys.argv[1]!="-f":
        print("Invalid usage...")
        sys.exit
    elif sys.argv[2] not in figlet.getFonts():
        print("Invalid usage...")
        sys.exit
    else:
        string = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(string))
else:
    print("Invalid usage...")
    sys.exit


