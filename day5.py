"""
Day 5: My Discount.
Create a function called my_discount. The function takes no arguments but asks the user to input the price
and the discount (percentage) of the product. Once the user inputs the price and discount, it calculates the price after
discount. For example, if the user enters 150 as price and 15% as the discount, your function should return 127.5.
"""
from collections import Counter


def my_discount():
    price = float(input('Enter the price of the product: '))
    discount = float(input('Enter the discount in %: '))
    if price > 0 and 0 <= discount <= 100:
        return round(price - price / 100 * discount, 2)
    return f'Incorrect data.'


"""
Extra Challenge: Tuple of Student Sex.
You work for school and your boss wants to know how many female and male students are enrolled in the school.
The school has saved the students in a list. Your task is to write a code that will count how many males and females
are in the list. Here is a list below:
students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
Your code should return a list of tuples. The list above should return: [('Male', 7), ('female', 6)]
"""


def count_students_sex(students: list):
    students_sex = {'Male': 0, 'female': 0}
    for student in students:
        if student.capitalize() == 'Male':
            students_sex['Male'] += 1
        elif student.lower() == 'female':
            students_sex['female'] += 1

    return list(students_sex.items())


if __name__ == '__main__':
    print(my_discount())

    students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female',
                'Male', 'female']
    print(count_students_sex(students))
