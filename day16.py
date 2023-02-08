"""
Day 16: Sum the List.
Write a function called sum_list with one parameter that takes a nested list of integers as an argument and returns the
sum of the integers. For example, if you pass [[2,3,5,6],[2,3,5,6]] as an argument your function should return a sum of 33.
"""


def sum_list(nested_list: list):
    return sum(number for sublist in nested_list for number in sublist)


"""
Extra Challenge: Unpack A Nest.
nested_list = [[12, 34, 56, 67], [34, 68, 78]]
Write a code that generates a list of the following numbers from the nested list above - 34, 67, 78. 
Your output should be another list: [34, 67, 78]. The list output should not have duplicates.
"""


def unpack_nested_list(nested_list: list) -> list:
    return list({number for sublist in nested_list for number in sublist if number in [34, 67, 78]})


if __name__ == '__main__':
    integers = [[2, 4, 5, 6], [2, 3, 5, 6]]
    print(sum_list(integers))

    nested_list = [[12, 34, 56, 67], [34, 68, 78]]
    print(unpack_nested_list(nested_list))