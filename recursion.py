# Write a Python function to calculate the factorial of a given number using recursion and unit test using pytest
import pytest


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800