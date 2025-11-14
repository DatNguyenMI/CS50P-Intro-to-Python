import sys
from random import choice
from pyfiglet import Figlet
figlet = Figlet()
font_list = figlet.getFonts()

def main():
    if len(sys.argv) >3:
        sys.exit ("Invalid Usage")
    elif len(sys.argv) == 1:
        user_text = input("Input: ")
        figlet.setFont(font=choice(font_list))
        print (figlet.renderText(user_text))
    elif len(sys.argv) ==2:
        sys.exit ("Invalid Usage")
    elif len(sys.argv) == 3:
        if not sys.argv[1] in ["-f","--font"]:
            sys.exit ("Invalid Usage")
        elif not sys.argv[2] in font_list:
            sys.exit ("Invalid Usage")
        else:
            user_text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print (figlet.renderText(user_text))
main()



