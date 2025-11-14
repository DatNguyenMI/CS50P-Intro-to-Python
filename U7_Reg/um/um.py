import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = re.findall(r"\bum\b",s,re.IGNORECASE)
    count_item = len(s)
    return count_item




if __name__ == "__main__":
    main()
