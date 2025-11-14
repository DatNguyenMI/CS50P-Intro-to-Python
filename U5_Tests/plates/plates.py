
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    list =[" ","!","."]
    if not 2 <= len (s) <= 6:  #if not within the length
        return False
    if not s[0:2].isalpha(): #if first 2 letters are not alphabet
        return False
    if not s.isalnum(): #if it's not number or alphabet
        return False
    #check if first number is 0
    found_number = False #this switch is off
    for i in s:
        if i.isdigit(): # for the first digit we found
            if not found_number and i == "0": #not found_number = turn to True (turn on switch) and if first number is 0
                #this logic ensure that once we found the first digit,it turn on the switch (True) , any subsequent number found might
                #be equal to 0 but it will turn switch off again (True - True ->false)
                return False
            found_number = True
        elif found_number and i.isalpha(): # check if we found number and then found another digit, it false\
            return False
    else:
        return True


if __name__ == "__main__":
    main()

