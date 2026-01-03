"""
Assignment 3
Task 1: Calculate Factorial Using a Function
1. Factorial function created using recursion method to calculate the factorial.
2. Function only return the factorial for non-negative integers.
3. n! = n*(n-1)*(n-2)...1
4. Returns the calculated factorial.
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

