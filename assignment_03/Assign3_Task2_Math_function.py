'''
Task 1: Check if a Number is Even or Odd
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.

logic implemented:
a. Takes a number input from the user.
b. Check if the number is divisible by 2 or not
c. if num%2==0 is True, number is even.
d. and if num%2==1 is False, number is odd.
'''

num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")