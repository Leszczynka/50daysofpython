from collections import Counter

"""
Day 2: Strings to Integers.
Write a function called convert_add that takes a list of strings as an argument and converts it to integers
and sums the list. For example ['1', '3', '5'] should be converted to [1, 3, 5] and summed to 9.
"""


def convert_add(array: list) -> int:
    return sum([int(element) if element.isdigit() else 0 for element in array])


"""
Extra Challenge: Duplicate Names.
Write a function called check_duplicates that takes a list of strings as an argument.
The function should check if the list has any duplicates. Tf there are duplicates,
the function should return the duplicates. If there are no duplicates, the function should return "No duplicates".
For example, the list of fruits below should return apple as a duplicate and list of names should return "no duplicates".
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
"""


def check_duplicates(array: list) -> str:
    counter = Counter(array)
    for key in counter.keys():
        if counter[key] > 1:
            return key
        return 'No duplicates'


if __name__ == '__main__':
    elements = ['1', '3', '5']
    elements_mix = ['a', '3', 'b', '4']
    print(convert_add(elements))
    print(convert_add(elements_mix))

    fruits = ['apple', 'orange', 'banana', 'apple']
    names = ['Yoda', 'Moses', 'Joshua', 'Mark']
    print(check_duplicates(fruits))
    print(check_duplicates(names))
