import random
def main():
    score = [get_valid_score()]
    choice = ''
    while choice != 'Q':
        print_menu()
        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            get_valid_score(score)  # Update the score
        elif choice == 'P':
            result = ['']  # Initialize an empty list to hold the result
            get_score_result(score[0], result)
            print(f"Result: {result[0]}")
        elif choice == 'S':
            show_stars(score[0])
        elif choice == 'Q':
            print("Goodbye!")
        else:
            print("Invalid choice, please try again.")

def print_menu():
    """Displays the menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def get_valid_score(score=None):
    """Prompts the user for a valid score (0-100) and updates the score if passed."""
    if score is None:
        score = [0]  # Use list if no score passed in
    score[0] = int(input("Enter a valid score (0-100): "))
    while score[0] < 0 or score[0] > 100:
        print("Invalid score, please enter a score between 0 and 100.")
        score[0] = int(input("Enter a valid score (0-100): "))

def get_score_result(score, result):
    """Determines the result based on the score and updates the result list."""
    if score < 0 or score > 100:
        result[0] = "Invalid score"
    elif score >= 90:
        result[0] = "Excellent"
    elif score >= 50:
        result[0] = "Passable"
    else:
        result[0] = "Bad"
def show_stars(score):
    """Prints stars equivalent to the score."""
    print('*' * score)
main()
