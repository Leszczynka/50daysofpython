"""
Day 11: Are They Equal?
Write a function called equal_strings. The function takes two strings as arguments and compares them.
If the strings are equal (if they have the same characters and have equal length), it should return True,
if they are not, it should return False. For example, 'love' and 'evol' should return True.
"""


def equal_strings(word1: str, word2: str) -> bool:
    return set(word1) == set(word2) and len(word1) == len(word2)


"""
Extra Challenge: Swap Values.
Write a function called swap_values. This function takes a list of numbers and swaps the first element
with the last element. For example, if you pass [2, 4, 67, 7] as a parameter, your function should return [7, 4, 67, 2].
"""


def swap_values(numbers: list) -> list:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    return numbers


if __name__ == '__main__':
    print(equal_strings('love', 'evol'))
    print(equal_strings('tree', 'reteee'))
    print(equal_strings('karolina', 'karolina'))

    n = [2, 4, 67, 7]
    print(swap_values(n))