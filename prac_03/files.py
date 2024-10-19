# files.py

# Constants for file names
OUT_FILE = "name.txt"
NUMBERS_FILE = "numbers.txt"

# Part 1: Writing the user's name to a file
name = input("Enter name: ")
with open(OUT_FILE, 'w') as out_file:  # Use 'with' to ensure the file is properly closed
    print(name, file=out_file)

# Part 2: Reading the name from the file and printing it
with open(OUT_FILE, 'r') as in_file:  # Use 'with' for reading
    text = in_file.read().strip()  # Strip any newline characters
print(f"Your name is {text}")

# Part 3: Creating the numbers file and reading the first two numbers
# Create the numbers.txt file with three numbers
with open(NUMBERS_FILE, 'w') as out_file:  # Open for writing
    out_file.write('17\n')
    out_file.write('42\n')
    out_file.write('400\n')

# Initialize total for the first two numbers
total = 0
with open(NUMBERS_FILE, 'r') as in_file:  # Open for reading
    for _ in range(2):  # Read only the first two lines
        value = in_file.readline().strip()  # Read line and strip whitespace
        total += int(value)  # Convert to integer and add to total
print(f"Total of first two numbers: {total}")  # Print the total

# Part 4: Printing all numbers from the numbers file
with open(NUMBERS_FILE, 'r') as in_file:  # Open for reading
    print("All numbers in the file:")
    for line in in_file:  # Iterate over each line
        print(line.strip())  # Print each line without extra whitespace