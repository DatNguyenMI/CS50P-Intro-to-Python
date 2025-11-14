
def main():
    grocery ={}
    while True:
        try:
            user = input().upper()
            if not user in grocery:
                value = 1
                grocery[user]= value
            else:
                value = int(grocery.get(user)) +1
                grocery.update({user:value})
        except EOFError:
            sorted_dict ={}
            sorted_key = sorted(grocery)
            for n in sorted_key:
                sorted_dict[n] =grocery[n]
            for n in sorted_dict:
                 print (f"{sorted_dict[n]} {n}", sep=" ")
            break

main()


