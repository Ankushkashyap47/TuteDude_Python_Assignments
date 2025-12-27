"""
Task 2: Sum of Integers from 1 to 50 Using a Loop
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
logic implemented:
a. sum variable assigned with 0 values and to store the overall sum.
d. for loop initiated to run from 1 to 50 range.
c. result= Sum is printed thereafter.
"""

sum= 0
for i in range(1,50):
    sum= sum+i
print(f' The sum of numbers from 1 to 50 is: {sum}')