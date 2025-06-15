number_list = []  # List to store user input

num_rounds = 5  # Renamed variable for clarity

for round_num in range(num_rounds):  # Using a more descriptive variable name
    user_number = int(input(f"Enter number for round {round_num + 1}: "))  # Added prompt clarity
    number_list.append(user_number)

# Displaying the results
print(f"First number entered: {number_list[0]}")
print(f"Last number entered: {number_list[-1]}")
print(f"Smallest number in the list: {min(number_list)}")
print(f"Largest number in the list: {max(number_list)}")
sum_of_numbers = sum(number_list)  # Renamed for clarity
average = sum_of_numbers / num_rounds
print(f"Average of the numbers: {average:.2f}")

# List of valid usernames
valid_usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                   'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                   'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input_username = input("Enter your username: ")

# Check if the entered username is valid
if user_input_username in valid_usernames:
    print("Access granted.")
else:
    print("Access denied.")
