# Assignment 04
**Task 1: Read a File and Handle Errors **
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
 
Solution:
Step 1: The program starts with a try block to handle possible file-related errors during execution.

Step 2: The open() function is used in read text mode ("rt") to open the file named sample.txt.
The with statement ensures the file is automatically closed after use.

Step 3: The readlines() method reads all lines from the file and stores them as a list in the variable data.

Step 4: A counter variable i is initialized with value 1 to keep track of line numbers.

Step 5: A message "Reading file content:" is printed to indicate the start of file reading.

Step 6: A for loop iterates through each line in the data list.

Step 7: For each line: The line number is printed using the counter i. rstrip() is used to remove the trailing newline character from each line.
The counter i is incremented by 1 after printing each line.

Step 8: If the file sample.txt does not exist, the program jumps to the except block.

Step 9: The except FileNotFoundError block prints an error message indicating that the file was not found.

------------------------------------------------------------------------------------------------------------------

**Task 2: Write and Append Data to a File **
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

Solution:
Step 1: The input() function is used to take a line of text from the user and store it in the variable line1.

Step 2: The file output.txt is opened in write mode ("wt") using the with open() statement.
        If the file already exists, its overwrites.
        If the file does not exist, it is created.

Step 3: The text stored in line1 is written to the file using the write() function, followed by a newline character (\n).

Step 4: A confirmation message is printed indicating that the data has been successfully written to the file.

Step 5: The input() function is used again to take additional text from the user and store it in the variable line2.

Step 6: The file output.txt is opened in append mode ("at").

Step 7: The text stored in line2 is appended to the file using the write() function, followed by a newline.

Step 8: A message is printed to confirm that the data has been successfully appended.

Step 9: The file output.txt is opened in read mode ("rt") to read its contents.

Step 10: The readlines() function reads all lines from the file and stores them in the list data.

Step 11: A header message is printed, and a for loop is used to display each line from the file.

Step 12: The rstrip() function removes any extra newline characters while printing each line, ensuring clean output.

