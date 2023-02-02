"""
Day 3: Register Check.
Write a function called register_check that checks how many students are in school.
The function takes a dictionary as a parameter. If student is in school, the dictionary say 'yes'.
If the student is not in school, the dictionary says 'no'. Your function should return the number of students in school.
Use the dictionary below. Tour function should return 3.
register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
"""


def register_check(students: dict) -> int:
    return sum(1 for value in students.values() if value == 'yes')


"""
Extra Challenge: Lowercase Names.
names = ['kerry', 'dickson', 'John', 'Mary', 'carol', 'Rose', 'adam']
You are given a list of names above. This list is made up of names of lowercase and uppercase letters.
Your task is to write a code that will return a tuple of all the names in list that have only lowercase letters.
Your tuple should have names sorted alphabetically in descending order.
Using the list above, your code should return: ('kerry', 'dickson', 'carol', 'adam')
"""


def get_lowercase_names(array: list) -> tuple:
    return tuple(sorted((name for name in array if name.islower()), reverse=True))


if __name__ == '__main__':
    register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
    print(register_check(register))

    names = ['dickson', 'John', 'kerry', 'Mary', 'carol', 'Rose', 'adam']
    print(get_lowercase_names(names))
    