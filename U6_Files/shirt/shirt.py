import sys
from PIL import Image
from PIL import ImageOps
from os.path import splitext


def main():
    check_input()
    with Image.open (f"{sys.argv[1]}") as input, Image.open ("shirt.png") as shirt:
        size = shirt.size #a function to return size of image as tupple (heigt, length)
        resize = ImageOps.fit (input, size)  #image as input, size as tupple 2 int values, method, bleed and centering are default, image as output
        resize.paste (shirt,shirt)
        resize.save (f"{sys.argv[2]}")

def check_input():
    if len(sys.argv)<3:
        sys.exit ("Too few command-line arguments")
    elif len (sys.argv) >3:
        sys.exit ("Too many command-line arguments")
    elif not sys.argv [1].endswith((".jpg",".jpeg","png")):
        sys.exit ("Invalid input")
    elif splitext(sys.argv [1]) [1] != splitext(sys.argv [2]) [1]:
        sys.exit ("Input and output have different extensions")
    else:
        try:
           open (f"{sys.argv[1]}","r")
        except FileNotFoundError:
           sys.exit(f"Could not read {sys.argv[1]}")

main()
