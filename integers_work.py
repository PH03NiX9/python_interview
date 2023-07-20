# Write a function that takes a list of integers as input and returns the sum of all even numbers in the list
def sum_even_numbers(numbers):
    # Variable to hold the running sum
    total = 0

    # Iterating over each number in the list
    for num in numbers:
        # If the number is even, add it to the total
        if num % 2 == 0:
            total += num
    return total

numbers = [1,2,3,4,5,6]
print(sum_even_numbers(numbers))


# Write a Python function that takes a list of numbers as input and returns the median value of the list.
def median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle = length // 2

    if length % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]
# The function first sorts the list of numbers in ascending order.
# It then calculates the length of the list and finds the middle index of the list.
# If the length of the list is even, it returns the average of the two middle values.
# If the length of the list is odd, it returns the middle value.
