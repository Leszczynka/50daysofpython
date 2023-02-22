"""
Day 27: Unique Numbers.
Write a function called unique_numbers that takes a list of numbers as an argument. Your function is going to find all
the unique numbers in the list. It will then sum up the unique numbers. You will calculate the difference between the
sum of all the numbers in the original list and the sum of unique numbers in the list.
If the difference is an even number, your function should return the original list.
If the difference is an odd number, your function should return a list with unique numbers only.
For example [1, 2, 4, 5, 6, 7, 8, 8] should return [1, 2, 3, 4, 5, 6, 7, 8, 8].
"""


def unique_numbers(numbers: list) -> list:
    unique = [number for number in numbers if numbers.count(number) == 1]
    diff = sum(numbers) - sum(unique)
    return numbers if diff % 2 == 0 else unique


"""
Extra Challenge: Difference of two Lists.
Write a function called difference that takes two lists as arguments. This function should return all the elements that
are in list a but not in list b and all the elements in list b not in list a. For example:
list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
should return: [4, 6, 7, 9]
Use list comprehension in your function.
"""


def difference(array1: list, array2: list) -> list:
    elements1 = [x for x in array1 if x not in array2]
    elements2 = [x for x in array2 if x not in array1]
    return elements1 + elements2


if __name__ == '__main__':
    n = [1, 2, 4, 5, 6, 7, 8, 8]
    print(unique_numbers(n))

    list1 = [1, 2, 4, 5, 6]
    list2 = [1, 2, 5, 7, 9]
    print(difference(list1, list2))