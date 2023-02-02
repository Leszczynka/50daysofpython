from math import sqrt


"""
Day 8: Odd and Even.
Write a function called odd_even that has one parameter and takes a list of numbers as an argument.
The function returns the difference between the largest even number in the list and the smallest odd number in the list.
For example, if you pass [1, 2, 4, 6] as an argument the function should return 6-1=5.
"""


def odd_even(numbers: list) -> int:
    max_even = max(number for number in numbers if number % 2 == 0)
    min_odd = min(number for number in numbers if number % 2 == 1)
    return max_even - min_odd


"""
Extra Challenge: List of Prime Numbers.
Write a function called prime_numbers. This function asks a user to enter a number (integer) as an argument
and returns list of all the prime numbers within its range.
For example, if user enters 10 your code should return [2,3,5,7] as prime numbers.
"""


def prime_numbers(n):
    primes = []
    for i in range(2, n+1):
        prime = True
        for j in range(2, int(sqrt(i)+1)):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    return primes


if __name__ == '__main__':
    print(odd_even([1, 2, 4, 6]))

    number = int(input('Enter a number to return all prime numbers within its range: '))
    print(prime_numbers(number))