"""
Assignment 3
Task 1: Calculate Factorial Using a Function
1.   Defines a function named factorial that takes a number as an argument
and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.


logic implemented:
a. Takes a number input from the user.
b.
c. if num%2==0 is True, number is even.
d. and if num%2==1 is False, number is odd.
"""

def factorial(num):
    """Returns factorial of a non-negative integer, or None if input is negative."""
    if num < 0:
        return None

    else:
        if num==0:
            return 1
        return num * factorial(num-1)

number = int(input("Enter a number: "))
factorial_value = factorial(number)
if factorial_value is None:
    print("Factorial of negative number is not allowed")
else:
    print(f"Factorial of {number} is: {factorial_value}")


