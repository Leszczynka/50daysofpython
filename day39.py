import random
import string
"""
Day 39: Password Generator.
Create a function called generate_password that generates any length of password for the user.
The password should have a random mix of upper letters, lower letters, numbers and punctuation symbols.
The function should ask the user how strong they want the password to be. The user should pick from - weak,
strong and very strong. If the user picks weak, the function should generate a 5-character long password.
If the user picks strong, generate an 8-character password and if they pick very strong,
generate a 12-character password.
"""


def generate_password():
    password_strengths = {'weak': 5, 'strong': 8, 'very_strong': 12}
    for key, value in password_strengths.items():
        print(f'{key} -> {value}')
    user_choice = int(input('How strong should the password be? Type corresponding number: '))
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    mix = lower_letters + upper_letters + digits + symbols
    if user_choice in password_strengths.values():
        while True:
            password = ''.join(random.choice(mix) for _ in range(user_choice))
            validate = all((any(map(str.isupper, password)),
                            any(map(str.islower, password)),
                            any(map(str.isdigit, password)),
                            any(elem for elem in password if elem in symbols)
                            ))
            if validate:
                return password
    else:
        print('Invalid input.')


if __name__ == '__main__':
    print(generate_password())