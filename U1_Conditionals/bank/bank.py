def main():
    answer = input ("Greeting:").strip().lower()
    if answer[:5] =="hello":
        print ("$0")
    elif answer[:1] == "h":
        print ("$20")
    else:
        print ("$100")

main()

