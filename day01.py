# Day 1: Division and square-root
"""
Write a function called divide_or_square that takes one argument (a number),
and returns the square root of the number if it is divisible by 5,
returns its remainder if it is not divisible by 5.
For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.
"""

from math import sqrt


def divide_or_square(number: int):
    return round(sqrt(number), 2) if number % 5 == 0 else number % 5


# extra challenge: longest value
"""
Write a function called longest_value that takes a dictionary as an argument and returns the first longest value
of the dictionary. For example, the following dictionary should return - apple as the longest value.
fruits = {'fruit': 'apple', 'color': 'green'}
"""


def longest_value(collection: dict):
    return max(collection.values(), key=len)


if __name__ == '__main__':
    print(divide_or_square(10))
    print(divide_or_square(11))
    fruits = {'apple': 'green', 'lemon': 'yellow', 'orange': 'orange'}
    print(longest_value(fruits))
