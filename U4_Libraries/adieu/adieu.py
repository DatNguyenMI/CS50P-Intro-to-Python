import inflect

p = inflect.engine()


def main():
    name_list = []
    while True:
        try:
            name_list.append(input("Name: "))
        except EOFError:
            print(f"\nAdieu, adieu, to {p.join(name_list)}")
            break


main()
