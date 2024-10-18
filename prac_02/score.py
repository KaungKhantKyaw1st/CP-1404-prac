import random

def main():
    """Main function to handle score input, process results, and print outputs."""
    user_score = int(input("Enter your score: "))
    user_result = [""]
    get_score_result(user_score, user_result)
    print(f"Your result: {user_result[0]}")

    random_score = random.randint(0, 100)
    random_result = [""]
    get_score_result(random_score, random_result)
    print(f"Random score: {random_score}, Result: {random_result[0]}")
def get_score_result(score, result):
    """Determine the result based on the score and update the result list."""
    if score < 0 or score > 100:
        result[0] = "Invalid score"
    elif score >= 90:
        result[0] = "Excellent"
    elif score >= 50:
        result[0] = "Passable"
    else:
        result[0] = "Bad"
main()
