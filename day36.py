"""
Day 36: Count String.
Write a function called count that takes one argument string and returns a dictionary of how many times
each element appears in the string. For example 'hello' should return {'h': 1, 'e': 1, 'l': 2, 'o': 1}.
"""


def count(text: str) -> dict:
    return {letter: text.count(letter) for letter in text}


if __name__ == '__main__':
    print(count('hello'))