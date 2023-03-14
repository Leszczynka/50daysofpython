"""
Day 30: Most Repeated Name.
Write a function called repeated_name that finds the most repeated name in the following list:
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
"""


def repeated_name(names: list) -> str:
    return max(set(names), key=names.count)


"""
Extra Challenge: Sort by Last Name.
You work for a local school in your area. The school has a list of names of students saved in a list.
The school has asked you to write a program that takes a list of names and sorts them alphabetically.
The names should be sorted by last names. Here is a list of names:
['Beyonce Knowles', 'Alicja Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']
Your code should not just sort them alphabetically, but it should also switch the names (the last name must be the first).
Here is how your code output should look:
['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Knowles Beyonce', 'Perry Katie']
Write a function called sorted_names.
"""


def sorted_names(names: list) -> list:
    return sorted([f'{name.split()[1]} {name.split()[0]}' for name in names])


if __name__ == "__main__":
    names = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
    print(repeated_name(names))

    students = ['Beyonce Knowles', 'Alicja Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']
    print(sorted_names(students))

