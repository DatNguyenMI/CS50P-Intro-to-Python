


def main():
    twit = input("Input: ")
    print (f"Output: {shorten (twit)}")

def shorten (word):
    vowels = ["a","i","e","o","u"]
    output =[]
    for char in word:
        if char.lower() not in vowels:
            output.append(char)
    output = "".join(output)
    return f"{output}"

if __name__=="__main__":
    main()
