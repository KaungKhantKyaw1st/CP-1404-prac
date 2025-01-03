"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""

import random

# Constants for price change limits
MAX_INCREASE = 0.1  # 10% increase
MAX_DECREASE = 0.05  # 5% decrease
MIN_PRICE = 0.01  # Minimum price limit
MAX_PRICE = 1000.0  # Maximum price limit
INITIAL_PRICE = 10.0  # Starting price
OUTPUT_FILE = "capitalist_conrad.txt"  # Output file name

# Initialize variables
number_of_days = 0
price = INITIAL_PRICE

# Open the output file for writing
with open(OUTPUT_FILE, 'w') as out_file:
    print(f"Starting price: ${price:,.2f}", file=out_file)

    # Simulation loop
    while MIN_PRICE <= price <= MAX_PRICE:
        price_change = 0
        number_of_days += 1

        # Generate a random integer of 1 or 2
        # If it's 1, the price increases; otherwise, it decreases
        if random.randint(1, 2) == 1:
            # Generate a random floating-point number for price increase
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            # Generate a random floating-point number for price decrease
            price_change = random.uniform(-MAX_DECREASE, 0)

        # Update the price based on the change
        price *= (1 + price_change)

        # Print the price for the current day, formatted to 2 decimal places
        print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# File will automatically close when using 'with' statement