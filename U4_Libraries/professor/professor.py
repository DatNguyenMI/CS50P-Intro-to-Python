import random


def main():
    level = get_level()
    score = 0
    n=0
    # run through session 10 times
    while n < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y
        tries = 3
        while tries > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct:
                    score = score + 1
                    break
                else:
                    tries = tries - 1
                    print("EEE")
            except ValueError:
                tries = tries - 1
                print("EEE")
            except EOFError:
                print(f"Score: {score}")
                return
        n = n+1
        if tries == 0:
            print(f"{x} + {y} = {correct}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not level in [1, 2, 3]:
                raise ValueError
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
