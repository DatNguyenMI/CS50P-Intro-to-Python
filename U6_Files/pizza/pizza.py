import sys
from tabulate import tabulate
import csv

pizza =[]
def main():
    if len(sys.argv)<2:
        sys.exit ("Too few command-line arguments")
    elif len (sys.argv) >2:
        sys.exit ("Too many command-line arguments")
    elif not sys.argv [1].endswith(".csv"):
        sys.exit ("Not a CSV file")
    else:
        try:
            with open (f"{sys.argv[1]}","r") as file:
                reader = csv.reader (file)
                for row in reader:
                    pizza.append ({"name":row[0],"small":row[1],"large":row[2]})
            print(tabulate(pizza,headers="firstrow",tablefmt ="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
main()
