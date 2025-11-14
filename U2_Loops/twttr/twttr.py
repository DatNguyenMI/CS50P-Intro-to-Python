list = ["a","i","e","o","u"]

def main():
    output= []
    twit = input("Input: ")
    for char in twit:
        if char.lower() not in list:
            output.append(char)
    output = "".join(output)
    print (f"Output: {output}")

main()



