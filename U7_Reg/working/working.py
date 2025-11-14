import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = re.search(r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$",s,re.IGNORECASE)
    if pattern:
        #get all values
        from_h,from_m,from_ap,to_h,to_m,to_ap = pattern.groups ("0")
        #convert to integers
        from_h, from_m = int(from_h), int(from_m)
        to_h, to_m = int(to_h), int(to_m)
        if not (0 <= int(from_h) <=12 and 0 <= int(to_h)<=12 and 0<= int(from_m) <60 and 0<= int(to_m) <60):
            raise ValueError
        from_h_24 = format_hour(from_h,from_ap)
        to_h_24= format_hour(to_h,to_ap)
        return f"{from_h_24:02}:{from_m:02} to {to_h_24:02}:{to_m:02}"
    else:
        raise ValueError

def format_hour(hour,am_pm):
    if am_pm == "AM" and hour ==12:
        return 0 #midnight
    if am_pm== "PM" and hour != 12:
        return hour +12
    else:
        return hour

if __name__ == "__main__":
    main()
