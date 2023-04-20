import random
"""
Day 38: Guess a Number.
Write a function called guess_a_number. The function should ask a user to guess a randomly generated number.
If the user guesses a higher number, the code should tell them that the guess is too high, if the user guesses low,
the code should tell them that their guess is too low. The user should get a maximum of three guesses.
When the user guesses right, the code should declare them a winner.
After three wrong guesses, the code should declare them a loser.
"""


def guess_a_number():
    number = random.randint(1, 10)
    chances = 3
    while chances:
        guess = int(input(f'Guess a number. You have {chances} chances.\n'))
        if guess == number:
            print('You are a winner!')
            return
        elif guess > number:
            print('Your number is too high.')
        else:
            print('Your number is too low.')
        chances -= 1
    print('You are a looser :(')


"""
Extra Challenge: Find Missing Numbers
list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
Write a function called missing_numbers that takes a list of sequence of numbers and finds the missing numbers in the
sequence. The list above should return: [4, 8, 10, 13, 16, 29, 30]
"""


def find_missing_numbers(numbers: list) -> list:
    return [num for num in range(min(numbers), max(numbers)) if num not in numbers]


if __name__ == '__main__':
    guess_a_number()

    num_list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
    print(find_missing_numbers(num_list))
