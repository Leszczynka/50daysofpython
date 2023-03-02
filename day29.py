"""
Day 29: Middle Figure.
Write a function called middle_figure that takes two parameters a and b. The two parameters are strings.
The function joins the two strings and finds the middle element. If the combined string has a middle element,
the function should return the element, otherwise, return 'no middle figure'.
Use 'make love' as an argument for a and 'not wars' as an argument b.
Your function should return 'e' as the middle element. Whitespaces should be removed.
"""


def middle_figure(a: str, b: str) -> str:
    combined_str = (a + b).replace(' ', '')
    n = len(combined_str)
    return combined_str[n // 2] if not n % 2 == 0 else 'no middle figure'


if __name__ == '__main__':
    print(middle_figure('make love', 'not wars'))