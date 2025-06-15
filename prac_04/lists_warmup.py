numbers = ["ten", 1, 4, 1, 5, 9, 1]

print(numbers[0])            # Accessing the first element
print(numbers[len(numbers)-1]) # Accessing the last element using len()
print(numbers[3])            # Accessing the fourth element
print(numbers[:len(numbers)-1]) # Slicing the list to exclude the last element
print(numbers[3:4])          # Accessing only the fourth element using slice
print(5 in numbers)          # Checking if 5 is in the list
print(7 not in numbers)      # Checking if 7 is NOT in the list
print("3" not in numbers)    # Checking if "3" is NOT in the list
print(numbers + [6, 5, 3])   # Concatenating another list to the original
numbers[0] = "TEN"           # Changing the first element to "TEN"
numbers[-1] = 100            # Changing the last element to 100
print(numbers[2:])           # Printing from the third element onward
print(9 in numbers)          # Checking if 9 is in the list



