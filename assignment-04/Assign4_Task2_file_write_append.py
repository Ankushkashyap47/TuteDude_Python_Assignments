"""
Assignment 4
Task 2: Write and Append Data to a File
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""
line1 = input("Enter text to write to the file: ")

with open("output.txt", "wt") as fh:
    fh.write(line1 + "\n")
    print("Data successfully written to output.txt\n")

line2 = input("Enter additional text to append: ")

with open("output.txt", "at") as fh:
    fh.write(line2 + "\n")
    print("Data successfully appended.\n")

with open("output.txt", "rt") as fh:
    data = fh.readlines()
    print("Final content of output.txt:")
    for line in data:
        print(line.rstrip())

