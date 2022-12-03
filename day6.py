"""
Day 6: UserName Generator.
Write a function called user_name that generates a username from the user's email.
The code should ask the user to input an email and the code should return everything before the @ sign as their username.
For example, if someone enters ben@gmail.com, the code should return ben as their username.
"""


def user_name(email: str) -> str:
    return email.partition('@')[0]


"""
Extra Challenge: Zero Both ends.
Write a function called zeroed that takes a list of numbers as an argument.
The code should zero (0) the first and the last number in the list.
For example, if the input is [2, 5, 7, 8, 9], your code should return [0, 5, 7, 8, 0]
"""


def zeroed(numbers: list) -> list:
    numbers[0], numbers[-1] = 0, 0
    return numbers


if __name__ == '__main__':
    print(user_name('ben@gmail.com'))

    numbers = [2, 5, 7, 8, 9]
    print(zeroed(numbers))
    