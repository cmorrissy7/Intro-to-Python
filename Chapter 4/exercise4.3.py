# This program calculates the amount a user has gone over or under their budget

# Create a accumulator variable to hold the the expenses
total_expenses = 0.0

# Ask user for budget for month
budget = float(input('Enter budget for month: '))

# Create variable to control the loop
expense = 1

# Ask user for expenses and keep a total
while expense != 0:
    expense = float(input('Enter expense (or press 0 if finished): '))
    total_expenses += expense

# Calculate and display amount under or over budget
total_amount = budget - total_expenses
print(f'Budget remaining: ${total_amount:,.2f}')

