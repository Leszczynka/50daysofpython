from emoji import emojize


"""
Day 13: Pay Your Tax.
Write a function called your_vat. The function takes no parameter. The function asks the user to input the price of
an item and VAT (vat should be a percentage). The function should return the price of the item plus VAT.
If the price is 220 and, VAT is 15% your code should return a vat inclusive price of 253.
Make sure that your code can handle ValueError. Ensure the code runs until valid numbers are entered.
(hint: Your code should include a while loop).
"""


def your_vat():
    while True:
        price = input('Enter a price of an item: ')
        vat = input('Enter a VAT ')
        try:
            price = float(price)
            vat = float(vat)
            break
        except ValueError:
            print('You entered an invalid value.')
    return price + price * vat / 100


"""
Extra Challenge: Pyramid of Snakes.
Write a function called python_snakes that takes a number as an argument and creates the following shape (pyramid),
using the number's range: (hint: Use the loops and emoji library).
"""


def python_snakes(n):
    snake = emojize(':snake:')
    for i in range(n + 1):
        space = ' ' * (n - i)
        print(space + snake * i)


if __name__ == '__main__':
    print(your_vat())
    python_snakes(7)