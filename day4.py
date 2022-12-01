"""
Day 4: Only Floats.
Write a function called only_floats, which takes two parameters a and b, and returns 2 if both arguments are floats,
returns 1 if only one argument is float, and returns 0 if neither argument is float.
If you pass (12.1, 23) as an argument, your function should return a 1.
"""


def only_floats(a, b):
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0


"""
Extra Challenge: Index of the Longest Word.
Write a function called word_index that takes one argument, a list of strings and returns the index of the longest
word in the list. If there is no longest word (if all the strings are of the same length), 
the function should return zero (0). For example, the list below should return 2.
words1 = ['Hate', 'remorse', 'vengeance']
And this below, should return zero (0)
words2 = ['Love', 'Hate']
"""


def word_index(words: list) -> int:
    word_iterator = iter(words)
    length = len(next(word_iterator))
    if all(len(word) == length for word in word_iterator):
        return 0

    return words.index(max(words, key=len))


if __name__ == '__main__':
    print(only_floats(12.1, 23))
    print(only_floats(1, 2))
    print(only_floats(1.5, 2.5))

    words1 = ['Hate', 'remorse', 'vengeance']
    words2 = ['Love', 'Hate']
    print(word_index(words1))
    print(word_index(words2))

