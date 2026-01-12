"""
Assignment 5
Task 2: Demonstrate List Slicing
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""
def process_numbers(number_list):
    print(f"Original list: {number_list}")

    sliced_list = number_list[:5]
    print(f"Extracted first five elements: {sliced_list}")

    sliced_list.reverse()
    print(f"Reversed extracted elements: {sliced_list}")

numbers = [1,2,3,4,5,6,7,8,9,10]
process_numbers(numbers)