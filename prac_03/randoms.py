import random

# Generate and print a random integer between 5 and 20
random_integer = random.randint(5, 20)  # Line 1
print(f"Random integer between 5 and 20: {random_integer}")

# Generate and print a random integer from 3 to 10 with a step of 2
random_range = random.randrange(3, 10, 2)  # Line 2
print(f"Random integer between 3 and 10 (step 2): {random_range}")

# Generate and print a random floating-point number between 2.5 and 5.5
random_float = random.uniform(2.5, 5.5)  # Line 3
print(f"Random float between 2.5 and 5.5: {random_float}")

# Answers to questions:
# 1. What did you see on line 1?
# A random integer between 5 and 20 is displayed.
# 2. What was the smallest number you could have seen, what was the largest?
# The smallest number could be 5, and the largest could be 20.

# 3. What did you see on line 2?
# A random integer between 3 and 10 with differences of 2 is displayed.
# 4. What was the smallest number you could have seen, what was the largest?
# The smallest number could be 3, and the largest could be 9.
# 5. Could line 2 have produced a 4?
# No, it couldn't. It only produces odd numbers (3, 5, 7, 9).

# 6. What did you see on line 3?
# A random decimal number between 2.5 and 5.5 is displayed.
# 7. What was the smallest number you could have seen, what was the largest?
# The smallest number could be 2.5, and the largest could be just below 5.5.

# Generate and print a random integer between 1 and 100
random_number = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_number}")