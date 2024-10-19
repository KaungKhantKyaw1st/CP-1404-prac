"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False  # Flag to indicate when to exit the loop

while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))  # Get user input and convert to integer
        is_finished = True  # Set flag to True to exit the loop if input is valid
    except ValueError:  # Catch ValueError if conversion fails
        print("Please enter a valid integer.")  # Prompt the user to try again

print(f"Valid result is: {result}")  # Output the valid integer