"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    monthly_incomes = []  # Renamed variable for clarity
    total_months = int(input("Enter the number of months: "))  # Changed prompt wording

    for month_index in range(1, total_months + 1):
        income = float(input(f"Income for month {month_index}: "))  # Changed input message
        monthly_incomes.append(income)

    display_income_report(monthly_incomes, total_months)  # Renamed function for clarity


def display_income_report(incomes, total_months):  # Renamed parameters for consistency
    print("\nIncome Summary\n--------------")  # Slightly altered report title
    cumulative_total = 0
    for month_index in range(1, total_months + 1):
        monthly_income = incomes[month_index - 1]  # Renamed variable
        cumulative_total += monthly_income
        print(f"Month {month_index:2} - Income: ${monthly_income:10.2f} | Cumulative Total: ${cumulative_total:10.2f}")

main()

