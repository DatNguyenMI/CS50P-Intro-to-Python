import random
import sys


def main():
    while True:
        try:
            n = int(input("Level: "))
            if not n >= 1:
                raise ValueError
            else:
                answer = random.randint(1, n)
                while True:
                    try:
                        guess = int(input("Guess: "))
                        if not guess >= 1:
                            raise ValueError
                        elif guess < answer:
                            print("Too small!")
                        elif guess > answer:
                            print("Too large!")
                        elif guess == answer:
                            sys.exit("Just right!")

                    except ValueError:
                        pass
        except ValueError:
            pass


main()
