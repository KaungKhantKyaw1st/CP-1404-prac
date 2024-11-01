def main():
    """Main function to execute the password validation and asterisk printing."""
    MIN_LENGTH = 8  # Define the minimum length for the password
    password = get_valid_password(MIN_LENGTH)  # Get a valid password from the user
    print_asterisks(password)  # Print the password as asterisks
def get_valid_password(min_length):
    """Prompt the user for a valid password meeting the minimum length requirement."""
    password = input(f"Enter a password (minimum {min_length} characters): ")

    # Keep prompting until a valid password is entered
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long. Please try again.")
        password = input(f"Enter a password (minimum {min_length} characters): ")

    return password
def print_asterisks(password):
    """Print the password as asterisks, masking the original characters."""
    print('*' * len(password))

main()
