"""
Day 20: Capitalize First Letter.
Write a function called capitalize. This function takes a string as an argument and capitalizes the fist letter of each
word. For example 'i like learning' becomes 'I Like Learning'.
"""


def capitalize(text: str) -> str:
    return text.title()


"""
Extra Challenge: Reversed List.
str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'
You are given a string of words. Some of the words in the string contain uppercase letters. Write a code that will return all the words that have an uppercase letter. Your code should return a list of the words. Each word in the list should be reversed. Here is how your output should look:
['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']
"""


def find_words_with_upper_letters(text: str) -> list:
    return [word[::-1] for word in text.split() if not word.islower()]


if __name__ == '__main__':
    print(capitalize('i love learning'))

    text = 'leArning is hard, bUt if You appLy youRself you can achieVe success'
    print(find_words_with_upper_letters(text))