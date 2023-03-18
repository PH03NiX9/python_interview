# Write a Python function that takes a list of strings as input and returns a new list containing only the strings that start with a vowel
def filter_vowels(strings):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for s in strings:
        if s[0].lower() in vowels:
            result.append(s)
    return result

strings = ['apple', 'banana', 'orange', 'pear', 'kiwi', 'mango']
print(filter_vowels(strings))