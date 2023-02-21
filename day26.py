"""
Day 26: Sort Words.
Write a function called sort_words that takes a string of words as an argument, removes whitespaces, and returns a list
of letters sorted in alphabetical order. Letters will be separated by commas. All letters should appear once in the list.
This means that you sort and remove duplicates. For example 'love life' should return as ['e,f,i,l,o,v']
"""


def sort_words(text: str) -> list:
    return [','.join(sorted(set(letter for letter in text.replace(' ', ''))))]


"""
Extra Challenge: Length of Words
s = 'Hi my name is Richard'
Write a function called string_length that takes a string of words (words and spaces) as argument.
This function should return the length of all the words in the string. Return the results in a form of a dictionary.
The string above should return:
{'Hi':2, 'my':2, 'name':4, 'is':2, 'Richard':7}
"""


def string_length(text: str) -> dict:
    return {word: len(word) for word in text.split(' ')}


if __name__ == '__main__':
    print(sort_words('love life'))

    s = 'Hi my name is Richard'
    print(string_length(s))