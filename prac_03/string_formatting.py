"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

# Constants for guitar information
name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# The ‘old’ manual way to format text with string concatenation
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format()
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# And with f-string formatting (introduced in Python 3.6)
print(f"My {name} was first made in {year} (that's right, {year}!)")

# Formatting currency (grouping with comma, 2 decimal places)
print(f"My {name} would cost ${cost:,.2f}")

# Aligning columns by using width after the :
numbers = [1, 19, 123, 456, -25]
print("\nAligned Numbers:")
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# Producing the output: 1922 Gibson L-5 CES for about $16,035!
print(f"\n{year} {name} for about ${cost:,.0f}!")

# Using a for loop with the range function for right-aligned output
print("\nRight-Aligned Outputs:")
for i in range(0, 151, 50):
    print(f"{i:>3}")