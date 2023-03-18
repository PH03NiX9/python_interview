import pytest
# Write a Pytest test case to check if a given string is a palindrome.
def is_palindrome(s):
    # Convert the input string to lowercase and remove all non-alphanumeric characters
    s = ''.join(c for c in s.lower() if c.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

def test_is_palindrome():
    # Test case 1: An empty string is a palindrome.
    assert is_palindrome("") == True

    # Test case 2: A single-character string is a palindrome.
    assert is_palindrome("a") == True

    # Test case 3: A palindrome with an odd number of characters.
    assert is_palindrome("racecar") == True

    # Test case 4: A palindrome with an even number of characters.
    assert is_palindrome("deified") == True

    # Test case 5: A non-palindrome string.
    assert is_palindrome("hello") == False

    # Test case 6: A string with mixed case and non-alphanumeric characters.
    assert is_palindrome("A man, a plan, a canal: Panama") == True


# Write a Pytest test case to check that a function that sorts a list of integers returns the list in ascending order.
def sort_integers(integers):
    #sort the list of integers in ascending order
    integers.sort()
    return integers

def test_sort_integers():
    unsorted_integers = [2, 1, 3, 4, 9, 7, 6, 5, 0]

    # Sort the list of integers
    sorted_integers = sort_integers(unsorted_integers)

    # Check that the sorted list is in an ascending order
    for i in range(len(sort_integers) - 1):
        assert sorted_integers[i] <= sorted_integers[i + 1]
# This test case defines a function sort_integers that takes a list of integers and sorts it in ascending order using the built-in sort() method. It then defines a Pytest test function test_sort_integers that calls sort_integers with an unsorted list of integers, and checks that the resulting sorted list is in ascending order.
# The test case uses a loop to check that each pair of adjacent integers in the sorted list is in ascending order, using the assert statement to raise an error if any pair of adjacent integers is not sorted correctly. If the test passes, the function returns with no errors. If the test fails, the assert statement will raise an error and the test case will fail.


# Write a Pytest test case to check that a function that finds the largest value in a list of integers returns the correct value.
def find_largest_value(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

def test_find_largest_value():
    # Test case 1: List with one value
    assert find_largest_value([5]) == 5
    
    # Test case 2: List with multiple values
    assert find_largest_value([10, 5, 20, 15]) == 20
    
    # Test case 3: List with negative values
    assert find_largest_value([-10, -5, -20, -15]) == -5
    
    # Test case 4: List with duplicate values
    assert find_largest_value([5, 10, 5, 20]) == 20
    
    # Test case 5: List with all equal values
    assert find_largest_value([10, 10, 10, 10]) == 10
# In this test case, we have defined five different test cases to check the behavior of the find_largest_value function. Each test case includes a list of integers and an assertion to check that the function returns the expected result.