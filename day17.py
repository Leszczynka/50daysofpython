from random import randint
"""
Day 17: User Name Generator.
Write a function called user_name, that creates a username for the user.
The function should ask a user to input their name.
The function should then reverse the name and attach a randomly issued number between 0-9 at the end of the name.
The function should return a username.
"""


def user_name() -> str:
    name = input('Enter your name: ')
    return name[::-1] + str(randint(0, 9))


"""
Extra Challenge: Sort by Length.
names = ["Peter", "Jon", "Andrew"]
Write a function called sort_length that takes a list of strings as an argument,
and sorts the strings in ascending order according to their length.
For example, the list above should return: ["Jon", "Peter", "Andrew"]. Do not use the built-in sort functions.
"""


def sort_length(array: list) -> list:
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if len(array[j]) > len(array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == '__main__':
    print(user_name())

    names = ["Peter", "Jon", "Andrew"]
    print(sort_length(names))
