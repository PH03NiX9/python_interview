# Write a Python function that returns reversed string
import unittest


def reverse_string(s):
    return s[::-1]

def test_reverse_string():
    assert reverse_string("Hello, world!") == "!dlrow ,olleH"
    assert reverse_string("Python is fun") == "nuf si nohtyP"
    assert reverse_string("12345") == "54321"
    assert reverse_string("") == ""