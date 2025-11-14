def main():
    expression = input ("Expression: ").strip().split()
    x = int(expression [0])
    y = expression [1]
    z = int(expression [2])
    if y == "+":
        print (float(x+z))
    elif y == "-":
        print (float(x-z))
    elif y== "*":
        print(float(x*z))
    elif y== "/":
        print (round(x/z,1))
    else:
        print ("function invalid")

main()
