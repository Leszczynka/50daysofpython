"""
Day 14: Flatten the List.
Write a function called flat_list that takes one argument, a nested list.
The function converts the nested list into a one-dimension list. For example [[2,4,5,6]] should return [2,4,5,6]
"""


def flat_list(nested_list: list) -> list:
    return [x for x in nested_list for x in x]


"""
Extra Challenge: Teacher's Salary.
A school asked you to write a program that will calculate teacher's salaries. The program should ask the user to enter
teacher's name, the number of periods taught in a month, and the rate per period. The monthly salary is calculated by
multiplying the number of periods by the monthly rate. The current monthly rate per period is $20.
If a teacher has more than 100 periods in a month, everything above 100 is overtime. Overtime is $25 per period.
For example, if a teacher has taught 105 periods, their monthly gross salary should be 2,125. 
Write a function called your_salary that calculates a teacher's gross salary.
The function should return the teacher's name, periods taught, and a gross salary.
Here is how you should format your output:
Teacher: John Kelly,
Periods: 105
Gross Salary: 2,125
"""


def your_salary():
    name = input('Enter your name: ')
    periods = int(input('Enter number of periods: '))
    rate = float(input('Enter your monthly rate per period: '))

    if periods > 100:
        salary = rate * 100 + 25 * (periods - 100)
    else:
        salary = rate * periods

    return f'Teacher: {name},\nPeriods: {periods}\nGross salary: {int(salary):,}'


if __name__ == '__main__':
    print(flat_list([[2, 4, 5, 6]]))
    print(your_salary())