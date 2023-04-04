"""
Day 32: Password Validator.
Write a function called password_validator. The function asks the user to enter a password.
A valid password should have at least one upper letter, one lower letter and one number.
It should not be less than 8 characters long. When the user enters a password, the function should check if the password
is valid. If the password is valid, the function should return the valid password.
If the password is not valid, the function should tell the user the errors in the password and prompt the user to enter
another password. The code should stop once the user enters a valid password. (use while loop).
"""
import re


def password_validator():
    while True:
        password = input('Enter your password: ')
        conditions = [
            (len(password) >= 8, 'Password should be longer than 8 characters.'),
            (any(x.isupper() for x in password), 'Password should have at least one upper letter.'),
            (any(x.islower() for x in password), 'Password should have at least one lower letter.'),
            (any(x.isdigit() for x in password), 'Password should have at least one number.')
        ]
        if all(condition[0] for condition in conditions):
            return password
        print('\n'.join([condition[1] for condition in conditions if not condition[0]]))


"""
Extra Challenge: Valid Email.
emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
Write a function called email_validator that takes a list of emails and checks if the emails are valid.
The function returns a list od only valid emails. A valid email address will have the following
@ symbol (if the @ sign is at the beginning of the name, the email id invalid. If there are more than one @ signs,
the email is invalid. All valid emails must have a dot com at the end (.com), if not, the email is invalid.
For example, the list of emails above should output the following as valid emails: ['ben@mail.com', 'kenny@gmail.com'].
If no emails in the list are valid, the function should return 'all emails are invalid'.
"""


def email_validator(emails: list) -> list:
    email_pattern = r"[A-Za-z0-9]+@[A-Za-z0-9]+(\.com)"
    correct_emails = [email for email in emails if re.fullmatch(email_pattern, email)]
    return correct_emails if correct_emails else 'all emails are invalid'


if __name__ == '__main__':
    password_validator()

    emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
    print(email_validator(emails))


