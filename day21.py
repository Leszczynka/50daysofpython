"""
Day 21: List of Tuples.
Write a function called make_tuples that takes two lists, equal lists, and combines them into a list of tuples.
For example, if list a is [1, 2, 3, 4] and list b is [5, 6, 7, 8], your function should return
[(1,5), (2, 6), (3, 7), (4, 8)].
"""


def make_tuples(arr1: list, arr2: list) -> list:
    return [(arr1[i], arr2[i]) for i in range(len(arr1))]


"""
Extra Challenge: Even Number or Average.
Write a function called even_or_average that ask a user to input five numbers.
Once the user is done, the code should return the largest even number in the inputted numbers.
If there is no even number in the list, the code should return the average of all the five numbers.
"""


def even_or_average():
    numbers = [int(input('Enter a number: ')) for _ in range(5)]
    even_nums = [number for number in numbers if number % 2 == 0]
    if even_nums:
        return max(even_nums)
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    print(make_tuples(a, b))
    
    print(even_or_average())