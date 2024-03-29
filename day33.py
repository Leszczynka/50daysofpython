"""
Day 33: List Intersection.
Write a function called inter_section that takes two lists and finds intersection
(the elements that are presented in both lists). The function should return a tuple of intersections.
Use list comprehension in your solution. Use the lists below. Your function should return (30, 65, 80).
list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]
"""
import datetime


def inter_section(list1: list, list2: list) -> tuple:
    return tuple([elem for elem in list1 if elem in list2])


"""
Extra Challenge: Set or List.
You want to implement a code that will search for a number in a range.
You have a decision to make as to whether to store the number in a set or a list.
Your decision will be based on time. You have to pick a data type that executes faster.
You have a range and you can either store it in a set or a list depending on which one executes faster when you are
searching for a number in the range. See below:
a = range(10000000)
x = set(a)
y = list(a)
Let's say you are looking for a number 9999999 in the range above. Search for this number in the list and the set.
Your challenge is to find which code executes faster. You will pick the one that executes quicker, lists or sets.
Run the two searches and time them.
"""


def find_faster_way():
    numbers = range(10000000)
    numbers_list = list(numbers)
    numbers_set = set(numbers)
    calculate_execution_time(numbers_list)
    calculate_execution_time(numbers_set)


def calculate_execution_time(collection):
    start = datetime.datetime.now()
    print(9999999 in collection)
    end = datetime.datetime.now()
    print(f'Elapsed time for searching in {type(collection)}: {end - start}')


if __name__ == '__main__':
    list1 = [20, 30, 60, 65, 75, 80, 85]
    list2 = [42, 30, 80, 65, 68, 88, 95]
    print(inter_section(list1, list2))

    find_faster_way()