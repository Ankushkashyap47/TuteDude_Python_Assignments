# Assignment 03 
**Task 1: Calculate Factorial Using a Function **

Problem Statement:  Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a 
     loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

Solution:
Step 1: Defined a function named "factorial(num)" that calculates the factorial of a given number.

Step 2: Inside the function, check if the input number num is less than 0. If num < 0, return None because 
the factorial of a negative number is not defined.

Step 3: Check if the input number is equal to 0. If num == 0, return 1, since the factorial of 0 is 1.

Step 4:If the number is greater than 0, calculated the factorial recursively by multiplying the number 
with the factorial of (num − 1) and return the result.

Step 5: Taken an integer input from the user using the input() function and converted it to an integer using int().

Step 6: Called the factorial() function with the user-provided number and store the returned value in the 
variable factorial_value.

Step 7: Checked if the returned value is None. If it is None, printed a message indicating that the factorial of 
a negative number is not allowed.

Step 8: If the returned value is not None, printed the factorial of the entered number.

------------------------------------------------------------------------------------------------------------------

**Task 2: Using the Math Module for Calculations **

Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
    o   Square root of the number
    o   Natural logarithm (log base e) of the number
    o   Sine of the number (in radians)
3.   Displays the calculated results.


