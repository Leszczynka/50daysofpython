"""
Day 18: Any Number of Arguments.
Write a function called any_number that can receive any number of arguments (integers and floats) and return the average
of those integers. If you pass 12, 90, 12, 34 as arguments your function should return 37.0 as average.
If you pass 12, 90 your function should return 51.0 as average.
"""


def any_number(*args: (int, float)) -> float:
    return sum(args) / len(args)


"""
Extra Challenge: Add and Reverse.
Write a function called add_reverse. This function takes two lists as argument and adds each corresponding number,
and reverses the outcome. For example, if you pass [10, 12, 34] and [12, 56, 78], your code should return [112, 68, 22].
If the two lists are not of equal lengths, the code should return a message that "the lists are not of equal lengths".
"""


def add_reverse(arr1: list, arr2: list):
    if len(arr1) == len(arr2):
        return [arr1[i] + arr2[i] for i in range(len(arr1))][::-1]
    return 'the lists are not of equal lengths'


if __name__ == '__main__':
    print(any_number(12, 90, 12, 34))
    print(any_number(12, 90, 3.3))

    arr1 = [10, 12, 34]
    arr2 = [12, 56, 78]
    arr3 = [1]
    print(add_reverse(arr1, arr2))
    print(add_reverse(arr1, arr3))