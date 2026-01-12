"""
Assignment 5
Task 1: Create a Dictionary of Student Marks
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""
student_data = {"Carol": 98, "Alice": 85, "Peter": 80, "Jortin": 60, "Andreas": 55}

student_find = input("Enter the student's name: ")

if student_find in student_data:
    print(f"{student_find}'s marks: {student_data[student_find]}")
else:
    print("Student not found.")