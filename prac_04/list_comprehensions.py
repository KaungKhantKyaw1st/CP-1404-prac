"""
CP1404/CP5632 Practical
List comprehensions
"""

# List of names and full names
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# Using a for loop to create a new list containing the first letter of each name
initials = []  # Renamed for clarity
for individual in names:  # Renamed loop variable
    initials.append(individual[0])
print(initials)

# List comprehension to achieve the same result as the loop above
initials = [individual[0] for individual in names]  # Renamed loop variable
print(initials)

# List comprehension to create a list of initials from full names
initials_from_full_names = [full_name.split()[0][0] + full_name.split()[1][0] for full_name in full_names]
print(initials_from_full_names)

# Using list comprehension to filter names starting with 'A'
names_starting_with_a = [individual for individual in names if individual.startswith('A')]
print(names_starting_with_a)

# Join method used to create a string of sorted names
print(" ".join(sorted(names)))

# TODO: List comprehension to create a list of all the full names in lowercase
lowercase_full_names = [full_name.lower() for full_name in full_names]  # Renamed loop variable
print(lowercase_full_names)

# List of numbers in string format
string_numbers = ['0', '10', '21', '3', '-7', '88', '9']  # Renamed for clarity

# TODO: List comprehension to convert strings to integers
converted_numbers = [int(string_number) for string_number in string_numbers]  # Renamed loop variable
print(converted_numbers)

# TODO: List comprehension to filter numbers greater than 9
large_numbers = [number for number in converted_numbers if number > 9]
print(large_numbers)

# TODO: (advanced) List comprehension and join method to create a string of last names from full names longer than 11 characters
long_names_last_names = ", ".join([full_name.split()[-1] for full_name in full_names if len(full_name) > 11])
print(long_names_last_names)