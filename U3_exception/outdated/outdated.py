month = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}


def main():
    while True:
        try:
            date_user = input("Date: ")
            if "/" in date_user:
                n = date_user.strip().split("/")
                if (
                    1 <= int(n[0]) <= 12
                    and 1 <= int(n[1]) <= 31
                    and 1000 <= int(n[2]) <= 9999
                ):
                    print(f"{n[2]}-{int(n[0]):02}-{int(n[1]):02}")
                    break
                else:
                    raise ValueError
            elif "," in date_user:
                n = date_user.replace(",", "").split(" ")
                if n[0] in month and 1 <= int(n[1]) <= 31 and 1000 <= int(n[2]) <= 9999:
                    print(f"{n[2]}-{month.get(n[0])}-{int(n[1]):02}")
                    break
                else:
                    raise ValueError
        except ValueError:
            pass


main()
