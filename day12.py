from datetime import datetime


"""
Day 12: Count the Dots.
Write a function called count_dots. This function takes a string separated by dots as a parameter and counts how many
dots are in the string. For example 'h.e.l.p.' should return 4 dots, and 'he.lp.' should return 2 dots.
"""


def count_dots(text: str) -> int:
    return text.count('.')


"""
Extra Challenge: Your Age in Minutes.
Write a function called age_in_minutes that tells a user how old they are in minutes.
Your code should ask the user to enter their year of birth, and it should return their age in minutes
(by subtracting their year of birth to the current year).
Here are things to look out for:
a) The user can only input a 4-digit year of birth. For example, 1930 is a valid year.
However, entering any number longer or less than 4 digits long should render input invalid.
Notify the user to input four digits number.
b) If a user enters a year before 1900, your code should tell the user that input is invalid.
If the user enters the year after the current year, the code should tell the user that input is invalid.
The code should run until the user inputs a valid year.
"""


def age_in_minutes():
    current_year = datetime.now().year
    while True:
        birth_year = input("Enter year of your birth: ")
        if len(birth_year) != 4:
            print("Input Invalid. Year should be a 4-digits number. ")
            continue
        if int(birth_year) < 1900 or int(birth_year) > int(current_year):
            print("Input Invalid. ")
            continue
        else:
            break

    leap_years = (current_year - int(birth_year)) // 4
    age = (current_year - int(birth_year) - leap_years) * 60 * 24 * 365 + (leap_years * 60 * 24 * 366)
    return age


if __name__ == '__main__':
    print(count_dots('h.e.l.p.'))
    print(count_dots('he.lp.'))
    print(f'You are {age_in_minutes()} minutes old.')