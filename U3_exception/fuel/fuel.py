
def get_value():
    while True:
        try:
            x = input("Fraction: ").split ("/")
            value = round(int(x[0])/int(x[1])*100)
            if 0<= value <=1:
                print ("E")
            elif 99 <= value <= 100:
                print ("F")
            elif 1< value < 99:
                print (f"{value}%")
            else:
                raise ValueError ()
            break
        except (ValueError, ZeroDivisionError):
            pass

get_value()
