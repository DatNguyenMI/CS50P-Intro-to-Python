
def main():
    while True:
        try:
            fraction = input("Fraction: ")
            pecentage=convert(fraction)
            print (gauge(pecentage))
        except (ValueError, ZeroDivisionError):
            pass

def convert (fraction):
    try:
        fraction = fraction.split("/")
        percentage = round(int(fraction[0])/int(fraction[1])*100)
        if 0<= percentage <= 100:
            return percentage
        else:
            raise ValueError
    except (ZeroDivisionError,ValueError):
        raise

def gauge (percentage):
    if 0 <= percentage <=1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
