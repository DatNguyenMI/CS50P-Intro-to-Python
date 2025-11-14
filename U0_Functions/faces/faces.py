
#def convert function
def convert(edited):
    if ":)" in edited:
        edited = edited.replace(":)","🙂")
    if ":(" in edited:
        edited= edited.replace(":(","🙁")
    return edited

#def main function
def main():
    edited = convert (input("input your text "))
    print (edited)

main()

