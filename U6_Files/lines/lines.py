import sys


def main():
    if len(sys.argv)<2:
        sys.exit ("Too few command-line arguments")
    elif len (sys.argv) >2:
        sys.exit ("Too many command-line arguments")
    elif not sys.argv [1].endswith(".py"):
        sys.exit ("Not a python file")
    else:
        try:
            with open (f"{sys.argv[1]}","r") as file:
                content = file.readlines()
                count = 0
            for row in content:
                if not row.strip() == "" and not row.lstrip().startswith ("#") == True:
                    count = count +1
            print (count)
        except FileNotFoundError:
            sys.exit("File does not exist")

main()
