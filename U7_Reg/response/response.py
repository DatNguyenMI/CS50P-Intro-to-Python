from validator_collection import validators,checkers,errors
import sys

email = input("What's your email address? ").strip()

email_address = checkers.is_email(email)
if email_address:
    print ("Valid")
else:
    print ("Invalid")
