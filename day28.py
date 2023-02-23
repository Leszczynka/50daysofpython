"""
Day 28: Return Indexes.
Write a function called index_position. This function takes a string as a parameter and returns the positions or indexes
of all lower letters in the string. For example 'LovE' should return [1,2].
"""


def index_position(text: str) -> list:
    return [text.index(letter) for letter in text if letter.islower()]


"""
Extra Challenge: Largest Number.
Write a function called largest_number that takes a list of integers and re-arrange the individual digits to create the
largest number possible. For example, if you pass the following as an argument: list1 = [3, 67, 87, 9, 2]. 
Your code should return the number in this exact format: 9,877,632 as the largest number.
"""


def largest_number(numbers: list):
    numbers_str = []
    for number in numbers:
        if len(str(number)) > 1:
            for i in range(len(str(number))):
                numbers_str.append(str(number)[i])
        else:
            numbers_str.append(str(number))

    str_num = ''.join(sorted(numbers_str, reverse=True))
    return "{:,}".format(int(str_num))


if __name__ == '__main__':
    print(index_position('LovE'))
    list1 = [3, 67, 87, 9, 2]
    print(largest_number(list1))