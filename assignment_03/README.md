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

Solution:
Step 1: Imported the math module to access mathematical functions such as square root, logarithm, and sine.

Step 2: Defined a function square_root(num) to calculate the square root of a number. If the number is negative,
the function returns None because the square root of a negative number is not defined.
If the number is non-negative, the function returns the square root using math.sqrt().

Step 3: Defined a function natural_log(num) to calculate the natural logarithm of a number.If the number is less than 
or equal to zero, the function returns None because the natural logarithm is defined only for positive numbers.
If the number is positive, the function returns the natural logarithm using math.log().

Step 4: Defined a function sine(num) to calculate the sine of a number.The input value is considered to be in radians.
The sine value is calculated using math.sin().

Step 5: integer input from the user using the input() function taken and converted it into an integer using int().

Step 6: Call the square_root(), natural_log(), and sine() functions with the user-provided number and store their 
returned values in separate variables.

Step 7: Checked the returned value of the square root function. If the value is None, displayed a message indicating
that the square root is not defined for negative numbers.
Otherwise, display the calculated square root.

Step 8: Checked the returned value of the natural logarithm function.If the value is None, displayed a message 
indicating that the natural logarithm is defined only for positive numbers.
Otherwise, display the calculated logarithm.

Step 9: Displayed the sine value of the number, as sine is defined for all real numbers.


