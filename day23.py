"""
Day 23: Simple Calculator.
Create a simple calculator. The calculator should be able to perform basic math operations:
add, subtract, divide and multiply. The calculator should take input from users.
The calculator should be able to handle ZeroDivisionError, NameError, and ValueError.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Error with divide by 0'


def calculate(option, a, b):
    match option:
        case 1:
            result = add(a, b)
        case 2:
            result = subtract(a, b)
        case 3:
            result = multiply(a, b)
        case 4:
            result = divide(a, b)
        case _:
            raise ValueError
    return f'Result: {result}'


def main():
    while True:
        try:
            a = float(input('Enter the first value: '))
            b = float(input('Enter the second value: '))
            operation = int(input("Enter corresponding number to operation which you want to perform:\n1.Add\n2.Substract\n3.Multiply\n4.Divide\n"))
            return calculate(operation, a, b)
        except (ValueError, NameError):
            print('Invalid input.')
            continue


"""
Extra Challenge: Multiply Words.
s = "love live and laugh"
Write a function called multiply_words that takes a string as an argument and multiplies the length
of each word in the string by the length of other words in the string. 
For example, the string above should return 240 - love (4) live (4) and (3) laugh (5).
However, your function should only multiply words will all lowercase letters. Of a word has one upper case letter,
it should be ignored. For example, the following string: s = "Hate war love Peace" should return 12 - war (3) love (4).
Hate and Peace will be ignored because they have at least one uppercase letter.
"""


def multiply_words(text: str) -> int:
    total_length = 1
    lengths = (len(word) for word in text.split() if word.islower())
    for length in lengths:
        total_length *= length
    return total_length


if __name__ == '__main__':
    print(main())

    s1 = "love live and laugh"
    s2 = "Hate war love Peace"
    print(multiply_words(s1))
    print(multiply_words(s2))

