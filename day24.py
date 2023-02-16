"""
Day 24: Average Calories.
Create a function called average_calories that calculates the average calories intake of a user.
The function should ask the user to input their calories intake for any number of days and once they hit 'done'
it should calculate and return the average intake.
"""


def average_calories():
    calories = []
    while True:
        user_input = input('Enter calories consumed during a day, enter "done" to calculate an average of calories: ')
        if user_input == 'done':
            return round(sum(calories) / len(calories), 2)
        try:
            calories.append(int(user_input))
        except ValueError:
            print('Invalid input.')


"""
Extra Challenge: Create a Nested List.
Write a function called nested_list that takes any number of lists and creates a 2-dimensional nested list of lists.
For example, if you pass the following lists as arguments: [1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5].
Your code should return [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]].
"""


def nested_list(*args: list) -> list:
    return [arg for arg in args]


if __name__ == '__main__':
    print(average_calories())

    x = [1, 2, 3, 5]
    y = [1, 2, 3, 4]
    z = [1, 3, 4, 5]
    print(nested_list(x, y, z))