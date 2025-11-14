import sys
import csv

pizza =[]
def main():
    check_input()
    with open (f"{sys.argv[1]}","r") as input,  open (f"{sys.argv[2]}","w") as output:
        reader = csv.DictReader (input)
        writer = csv.DictWriter(output,fieldnames = ["first","last","house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow(
                {"first":first,
                 "last": last,
                 "house": row ["house"]
                }
            )
def check_input():
    if len(sys.argv)<3:
        sys.exit ("Too few command-line arguments")
    elif len (sys.argv) >3:
        sys.exit ("Too many command-line arguments")
    elif not sys.argv [1].endswith(".csv") or not sys.argv [2].endswith(".csv"):
        sys.exit ("Not a CSV file")
    else:
        try:
           open (f"{sys.argv[1]}","r")
        except FileNotFoundError:
           sys.exit(f"Could not read {sys.argv[1]}")

main()
