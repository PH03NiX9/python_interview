# Write a Python program that accepts a string as input and returns the number of vowels in the string.

def only_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    res = 0

    for i in s:
        if i in vowels:
            res += 1
    
    return res

def test_only_vowels():
    assert only_vowels("apple") == 2
    assert only_vowels("anaconda") == 4
    assert only_vowels("brq") == 0