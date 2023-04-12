"""
Day 34: Just Digits.
In this challenge, copy the text below and save it as a CSV file python.csv (day34.csv).
Write a function called just_digits that reads the text from the CSV file and returns only digit elements from the file.
Your function should return 1991, 2, 2000, 3, 2008 as a list of strings.
"""


def just_digits():
    with open("day34.csv", "r") as file:
        text = file.read()
        return [element for element in text.split() if element.isdigit()]


if __name__ == '__main__':
    print(just_digits())