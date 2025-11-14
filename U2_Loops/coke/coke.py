def main():
    due =50
    while due > 0:
        print (f"Amount Due: {due}")
        insert =int(input("Insert coin: "))
        if insert in [5,10,25]:
            due = due-insert
    change_owed = abs(due)
    print (f"Change Owed: {change_owed}")
main()
