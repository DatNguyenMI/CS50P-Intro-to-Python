# Automated Email Reminder for missing booking hours
#### Video Demo:  <https://youtu.be/tX0yl4xiurA>
## Description:
### Purpose:
* In consulting industry, it's very important for consultants to book all their working hours during the month to specific clients projects.
* This will allow billing team to record and bill customers on monthly basis. Missing booking hours can lead to wrong revenue recognition for the period and also in some cases clients can reject the billing if it's not billed within certain timeframe.
* While it is important, the task is basically very manual and repetitive. It simply involves checking actual booked hours against a predefined set of required working hours per month, draft an email to the consultants with missing hours and ask them to input hours.
With this project, we try to create a python program to automate the process of checking missing hours as well as drafing emails.

### Assumptions:
I make follwoing assumptions in my setup:
* Each consulting firms has some sort of hours tracking and booking software and the data can be easily extracted in csv format with all required data.
* Also the required working hours are usually predetermined for entire year.

### Main Feature
This program works by I try to create a python program to:
    - Prompting the user (e.g., a billing administrator) for a specific month and year they want to execute the program.
    - Looking up the total required work hours for that specific month from a master data file (hours.csv).
    - Check input hours of each consultants (booking.csv) against the min required hours of that month.
    - Comparing the booked hours against the required hours and generating a "delinquent list" of all consultants who are missing time.
    - For each person on this list, it then drafts a personalized reminder email
    - Finally, it prints these drafted emails to the console, allowing the administrator to copy/paste them as needed.

### Knowledge from CS50 used:
This project utilizes Python skills in data processing, file I/O (using the csv module), error handling (try...except), and function-based program design.

### How the Program Works
The main program is controlled by the `main()` function:
1. The user executes the program by running python `project.py`.
2. The program first calls `check_input()` to get user input for `month` and `year` and validate the validity of user input. It ensures the inputs are valid numbers.
3. Next, `main()` calls `get_required_hours()`, passing in the month and year. This function opens `hours.csv`, finds the matching row, and returns the total hours required `required_hours` for that month (e.g., 145 for 11/2025).
4. If no `required_hours` are found for that date, the program exits with a `sys.exit` error, as it cannot proceed.
5. `main()` then calls `check_missing_hours()`, passing in the `month`, `year`, and the `required_hours` we just found.
6. `check_missing_hours()` opens `booking.csv`, iterates through all consultants, and finds those whose hour input is less than the `required_hours`. It builds a `reminder_list` (a list of dictionaries) and returns it.
7. Finally, `main()` loops through the `reminder_list`. For each person in the list, it calls `draft_email()` to generate a personalized subject and body, and then `print` the formatted email to the console.

### File Structure & Purpose

This project consists of 4 main files (plus this README):
* `project.py`: The main Python script that contains all the program logic.
  * `main()`: The main function that controls the overall program flow.
  * `check_input(month, year)`: This function is called by `main()` to get and validate the user's initial input. It ensures the month and year are numerical and within a reasonable range.
  * `get_required_hours(month, year)`: This is the first testable function. It takes a `month` and `year`, opens `hours.csv`, and finds the corresponding total work hours for that period. It is designed to be a lookup function.
  * `check_missing_hours(month, year, required_hours)`: This is the second testable function and the core of the project's data processing. It takes the period and required hours, reads `booking.csv`, and produces a new list containing only the people who need to be reminded.
  * `draft_email(personal_info, month, year, required_hours)`: This is the third testable function. It takes the data for one person and formats a professional, clear email subject and body.
*`hours.csv`: A "master data" or "lookup" file. It stores the official required work hours for each month and year. This file is small and rarely changes.
  * `month`: The month (as a number).
  * `required hours`: The total hours for that month.
  * `year`: The year.

* `booking.csv`: The "transactional data" file. This represents a hypothetical data export from the firm's time-booking software. It is expected to be large and change daily.
  * `name`: The consultant's full name.
  * `hour input`: The hours they have booked for the period.
  * `month`: The month of the booking.
  * `year`: The year of the booking.
  * `email`: The consultant's email address.

*` test_project.py`: This file contains the pytest functions to test the three custom functions (`test_get_required_hours`, `test_check_missing_hours`, `test_draft_email`) to ensure they work as expected.
* `requirements.txt`: This file would list any pip-installable libraries. For this project, only pytest (for testing) would be required, as all other modules (csv, sys) are part of the Python standard library.

### Design Choices
I made several specific design choices for this project:
* Functional Programming: Instead of one large main function or a complex class, I chose to use a functional approach. The program is broken into small, single-responsibility functions. `get_required_hours` only gets the hours. `check_missing_hours` only filters the list. `draft_email` only formats the string. This makes the code highly readable, maintainable, and, most importantly, very easy to test with `pytest`.
* Separate Data Files: I intentionally used two separate CSV files instead of one. `hours.csv` acts as a master lookup table (which is good database design), while `booking.csv` is the actual data the program works on. This separation is more realistic, as the required hours for a month are a single value that applies to everyone, while the bookings are individual.
* Flexible Error Handling: The code uses `try`...`except` (`ValueError`, `KeyError`, `TypeError`) when reading the CSVs. This is crucial for real-world data processing, as a single blank line, a typo, or a missing column in the CSV export would otherwise crash the entire program. This way, the program just skips the bad row and continues.
* Print email vs. Email sent: I deliberately chose not to implement the final step of sending a real email (e.g., with sendgrid) due to safety & security issue. It avoids the need to store a real email password or API key in the code, which is a major security risk given I haven't learnt much about security and data privacy in CS50 Intro course.
* Also the core goal of this project is utilizing CS50 concepts including data processing, file IO, Loop, Conditional. By successfully generating the final, formatted list of emails, the program has fully achieved its target.
* The final output printed to the console proves the logic is 100% successful.
