"""
Day 22: Add Under_Score.
Create three functions. The first called add_hash takes a string and a hash (#) between the words.
The second function called add_underscore removes the hash (#) and replaces it with an underscore "_".
The third function called remove_underscore, removes the underscore and replaces with nothing.
If you pass 'Python' as an argument for the three functions, and you call them at the same time like:
print(remove_underscore(add_underscore(add_hash('Python')))) it should return Python.
"""


def add_hash(text: str) -> str:
    return text.replace(' ', '#')


def add_underscore(text: str) -> str:
    return text.replace('#', '_')


def remove_underscore(text: str) -> str:
    return text.replace('_', '')


if __name__ == '__main__':
    print(remove_underscore(add_underscore(add_hash('Python'))))
