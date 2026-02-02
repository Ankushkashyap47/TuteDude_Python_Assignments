# Assignment 05
**Task 1: Create a Dictionary of Student Marks **
Problem Statement:  Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
 
Solution:
Step 1: A dictionary named student_data is created where student names are stored as keys and their corresponding 
        marks are stored as values.

Step 2: The input() function is used to accept a student’s name from the user and store it in the variable student_find.

Step 3: An if condition is used to check whether the entered student name exists as a key in the student_data dictionary.

Step 4: If the student name is found in the dictionary, the corresponding marks are retrieved using the key and
        displayed using the print() function.

Step 5: If the student name is not found, the else block is executed and message “Student not found.” is displayed.

------------------------------------------------------------------------------------------------------------------

**Task 2:  Demonstrate List Slicing **
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list


Solution:
Step 1: A function named process_numbers() is defined which accepts a list (number_list) as an argument.

Step 2: Inside the function, the original list is printed using the print() function.

Step 3: List slicing is used to extract the first five elements from the list using number_list[:5], 
        and the result is stored in sliced_list.

Step 4: The extracted list (sliced_list) is printed.

Step 5: The reverse() method is used to reverse the extracted list in place.

Step 6: The reversed extracted list is printed.

Step 7: Outside the function, a list named numbers containing values from 1 to 10 is created.

Step 8: The function process_numbers() is called by passing the numbers list as an argument.