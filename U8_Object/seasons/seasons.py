from datetime import date
import inflect
p= inflect.engine()
import sys

class Birthday:
    def __init__(self,birthday):
        try:
           self.birthday = date.fromisoformat(birthday)
        except ValueError:
            raise ValueError

    def get_minute(self):
         age =  date.today() - self.birthday
         minutes = 24*60*int(age.days)
         return minutes

    def __str__(self):
        minutes = self.get_minute()
        return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"


def main():
    try:
        birthday = Birthday((input ("Date of Birth: ")))
        print (birthday)
    except ValueError:
        sys.exit ("Invalid date")



if __name__ == "__main__":
    main()
