# Write a unittest test case to check that a function that calculates the factorial of a given number returns the correct value.
import unittest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

if __name__ == '__main__':
    unittest.main()

# Write a unittest test case to check that a function that converts a Celsius to Fahrenheit returns the correct value.
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_zero_degrees_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_freezing_point(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_negative_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

if __name__ == '__main__':
    unittest.main()
