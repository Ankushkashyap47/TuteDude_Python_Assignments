"""
Assignment 3
Task 2: Using the Math Module for Calculations
1. math module imported in python program
2. sqrt() used to calculate the square root of a non-negative number.
3. log() used to calculate the natural logarithm of positive numbers.
4. sine() used to calculate the sine (in radians) of number.
5. results are printed accordingly.
"""

import math

def square_root(num):
    """Returns the square root of a non-negative number, or None if invalid."""
    if num < 0:
        return None
    else:
        return math.sqrt(num)

def natural_log(num):
    """Returns the natural logarithm of a positive number, or None if invalid."""
    if num <= 0:
        return None
    else:
        return math.log(num)

def sine(num):
    """Returns the sine of a number (input in radians)."""
    return math.sin(num)

number=int(input("Enter a number: "))

sqrt_val = square_root(number)
log_val = natural_log(number)
sin_val = sine(number)

if sqrt_val is None:
    print("Square root is not defined for negative numbers")
else:
    print(f"Square root: {sqrt_val}")
if log_val is None:
    print("Natural logarithm is defined only for positive numbers")
else:
    print(f"Logarithm: {log_val}")
print(f"Sine: {sin_val}")