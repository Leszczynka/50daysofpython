"""
Day 7: A string range.
Write a function called string_range that takes a single number and returns a string of its range.
The string characters should be separated by dots (.).
For example, if you pass 6 as an argument, your function should return '0.1.2.3.4.5'.
"""
from collections import Counter


def string_range(number: int) -> str:
    return '.'.join(str(number) for number in range(number + 1))


"""
Extra Challenge: Dictionary of names.
You are given a list of names, and you are asked to write a code that returns all the names that start with 'S'.
Your code should return a dictionary of all the names that start with S and how many times they appear in the dictionary.
Here is a list below: names = ['Joseph', 'Nathan', 'Sasha', 'Kelly', 'Muhammad', 'Jabulani', 'Sera', 'Patel', 'Sera']
Your code should return: {'Sasha': 1, 'Sera': 2}
"""


def find_names_starts_with_s(names: list) -> dict:
    name_counter = Counter(names)
    return {name: value for (name, value) in name_counter.items() if name.upper().startswith('S')}


if __name__ == '__main__':
    print(string_range(5))

    names = ['Joseph', 'Nathan', 'Sasha', 'Kelly', 'Muhammad', 'Jabulani', 'Sera', 'Patel', 'Sera']
    print(find_names_starts_with_s(names))
