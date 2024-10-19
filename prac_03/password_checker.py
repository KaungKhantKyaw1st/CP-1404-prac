# password_checker.py

"""
CP1404/CP5632 - Practical
Password checker program to validate user passwords.
"""

# Constants for password validation
MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"\tand 1 or more special characters: {SPECIAL_CHARACTERS}")

    while True:
        password = input("> ")
        if is_valid_password(password):
            print(f"Your {len(password)}-character password is valid: {password}")
            break
        else:
            print("Invalid password!")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check password length
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    # Initialize counts for character types
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    # Count each type of character
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif SPECIAL_CHARS_REQUIRED and char in SPECIAL_CHARACTERS:
            count_special += 1

    # Check that all character type requirements are met
    if count_digit == 0 or count_lower == 0 or count_upper == 0:
        return False

    if SPECIAL_CHARS_REQUIRED and count_special == 0:
        return False

    # Password is valid if all checks are passed
    return True


if __name__ == "__main__":
    main()