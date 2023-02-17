"""
Day 25: All the Same.
Create function called all_the_same that takes one argument, a string, a list, or a tuple and checks if all the elements
are the same. If elements are the same, the function should return True. If not, it should return False.
For example, ['Mary', 'Mary', 'Mary'] should return True.
"""


def all_the_same(elements: (str, list, tuple)) -> bool:
    return len(set(elements)) == 1


"""
Extra Challenge: Reverse a String.
str1 = 'the love is real'
Write a function called read_backwards that takes a string as an argument and reverse it.
For example, the string above should return 'real is love the'.
"""


def read_backwards(text: str) -> str:
    return ' '.join(word for word in text.split()[::-1])


if __name__ == '__main__':
    names1 = ['Mary', 'Mary', 'Mary']
    names2 = ['Mary', 'Kate', 'Mary']
    print(all_the_same(names1))
    print(all_the_same(names2))

    str1 = 'the love is real'
    print(read_backwards(str1))