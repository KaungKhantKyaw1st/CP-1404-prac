import random

MIN_NUMBER = 1  # Renamed variable for clarity
MAX_NUMBER = 45
NUM_PICKS = 6

quick_pick_count = int(input("How many quick picks would you like? "))  # Changed input prompt

for _ in range(quick_pick_count):
    selected_numbers = []  # Renamed for clarity
    while len(selected_numbers) < NUM_PICKS:  # Changed to use a while loop for clarity
        random_pick = random.randint(MIN_NUMBER, MAX_NUMBER)
        if random_pick not in selected_numbers:
            selected_numbers.append(random_pick)
    selected_numbers.sort()
    print(" ".join(f"{number:2}" for number in selected_numbers))  # Renamed loop variable

