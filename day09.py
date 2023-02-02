"""
Day 9: Biggest Odd Number.
Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list.
For example, if you pass '23569' as an argument, your function should return 9. Use list comprehension.
"""


def biggest_odd(numbers: str) -> int:
    return max([int(number) for number in numbers if int(number) % 2 != 0])


"""
Extra Challenge: Zeros to the End.
Write a function called zeros_last. This function takes a list as argument. If a list has zeros (0),
it will move them to the front of the list and maintain order of the other numbers in the list.
If there are no zeros in the list, the function should return the original list sorted in ascending order.
For example, if you pass [1, 4, 6, 0, 7, 0, 9] as an argument, your code should return [1, 4, 6, 7, 9, 0, 0].
If you pass [2, 1, 4, 7, 6] as your argument your code should return [1, 2, 4, 6, 7].
"""


def zeros_last(numbers: list) -> list:
    zeros = numbers.count(0)
    if zeros:
        for number in numbers:
            if not number:
                numbers.remove(number)
                numbers.append(number)
    else:
        numbers.sort()

    return numbers


if __name__ == '__main__':
    print(biggest_odd('23569'))

    numbers1 = [1, 4, 6, 0, 7, 0, 9]
    print(zeros_last(numbers1))

    numbers2 = [2, 1, 4, 7, 6]
    print(zeros_last(numbers2))