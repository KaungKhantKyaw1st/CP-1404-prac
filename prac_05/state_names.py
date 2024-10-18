"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Dictionary of Australian state codes and names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Display the dictionary
print("State codes and their full names:")
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()

while state_code != "":
    # Attempt to display the full name of the entered state code
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print(f"Invalid short state: {state_code}")
    state_code = input("Enter short state: ").upper()

# Display all states and their names in a formatted manner
print("\nAll state codes and their corresponding names:")
for code, full_name in CODE_TO_NAME.items():
    print(f"{code:3} is {full_name}")
