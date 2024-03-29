"""
Day 15: Same in Reverse.
Write a function called same_in_reverse that takes a string and checks if the string reads the same in reverse.
If it is the same, the code should return True if not, it should return False.
For example, 'dad' should return True, because in reads the same in reverse.
"""


def same_in_reverse(text: str) -> bool:
    return text == text[::-1]


"""
Extra Challenge: What's My Age?
Write a function called your_age. This function asks a student to enter their name and then returns their age.
For example, if a user enters Peter as their name, your function should return: 'Hi, Peter, you are 27 years old.'.
This function reads data from the database (dictionary below). If the name is not in the dictionary,
your code should tell the user that their name is not in the dictionary, and ask them for their age.
Your code should add the name and age to the dictionary of names age below.
Once added your code should return to the user 'Hi, (added name), you are (added age) years old.'.
Remember to convert the input from the user to lowercase letters.
"""

names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}


def your_age():
    name = input('Enter your name: ')
    if name in names_age.keys():
        age = names_age[name]
    else:
        age = int(input('Enter your age: '))
        names_age[name.lower()] = age
    return f'Hi, {name}, you are {age} years old.'


if __name__ == '__main__':
    print(same_in_reverse('dad'))
    print(same_in_reverse('car'))
    print(your_age())
