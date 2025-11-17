import csv #to work with csv file
import sys #to exit program


def main():
    month, year = check_input(int(input("Month: ")),int(input("Year: ")))
    required_hours = get_required_hours (month,year)
    reminder_list = check_missing_hours (month, year, required_hours)
    if len(reminder_list) >0:
        for person in reminder_list:
            receiver_email = person["email"]
            subject,body = draft_email(personal_info = person,month = month,year = year, required_hours = required_hours)
            print (f"Sending reminder to {person["name"]}\n" )
            print (f""" From: ABC@email.com
    to: {person["email"]}
    Subject: {subject}
    {body}\n""")
            print ("Email sent.\n")

def check_input(month,year):
    while True:
        try:
            if 1<= month <= 12 and 1900 <= year <= 9999:
                return month, year
            else:
                print ("Please input valid month and year in format MM YYYY")
        except ValueError:
            print ("Please input month and year in format MM YYY")
            pass

def get_required_hours(month,year):
    # Get the required hours for respective months depending on user input of month and year
    with open ("hours.csv","r") as file: #open master data for required hours per month
        reader = csv.DictReader(file)
        for row in reader:
            try:
                if int(row["month"])== month and int (row["year"])==year:
                    return int(row["required hours"])
            except (ValueError, TypeError, KeyError):
                pass
        #if found nothing, quit program
        sys.exit (f"Check hours.csv for required hours for {month}/{year}")

def check_missing_hours (month,year,required_hours):
    # get the user name and hours from booking.csv and check if matching requires hours
    reminder_list =[]
    with open ("booking.csv","r") as file: #open master data for required hours per month
        reader = csv.DictReader(file)
        for row in reader:
            try:
                if int(row["month"])== month and int (row["year"])==year and int(row["hour input"]) < required_hours:
                    personal_info = {"name":row["name"],
                                         "email":row["email"],
                                         "hour input":row["hour input"]}
                    reminder_list.append(personal_info)
            except (ValueError, KeyError, TypeError):
                print (f"check row {row} for error in input file")
    return reminder_list


def draft_email(personal_info,month, year, required_hours):
   subject = "Action Required: Please book your missing hours"
   body = f"""Dear {personal_info["name"]},
Please be inform that for {month}/{year}, the required booking hours are {required_hours} hours.
However we notice in the system you only book {personal_info["hour input"]} hours.
Please book the missing hours as soon as possible.
Any question , please contact billing department.
Thank you"""
   return subject, body


if __name__=="__main__":
    main()
