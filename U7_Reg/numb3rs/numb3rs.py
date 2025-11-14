import re
import sys


def main():
    print (validate (input ("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(0|[1-9][0-9]{0,2})\.(0|[1-9][0-9]{0,2})\.(0|[1-9][0-9]{0,2})\.(0|[1-9][0-9]{0,2})$"
    match = re.search (pattern, ip)
    if match:
        if int(match.group(1)) <=255 and int(match.group(2)) <=255 and int(match.group(3)) <=255 and int(match.group(4)) <=255:
            return True
        else:
            return False
    else:
        return False




if __name__=="__main__":
    main()
