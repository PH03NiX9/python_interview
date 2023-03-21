# print integers from 1 to 100, but if the number is divisible by 3, print fizz. If the number is divisible by 5, print Buzz and if by both 3 and 5, print FizzBuzz

def fizzbuzz():
    for i in range(1,101):
        string = ""
        if i % 3 ==0 and i % 5 == 0:
            string = string + "FizzBuzz"
            print(string)
        elif i % 3 == 0:
            string = string + "Fizz"
            print(string)
        elif i % 5 == 0:
            string = string + "Buzz"
            print(string)
        else:
            print(i)

fizzbuzz()