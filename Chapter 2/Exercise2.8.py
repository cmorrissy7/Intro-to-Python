# Get the charge for food
charge = float(input('Enter charge for food: '))

# Calculate tip amount by multiplying charge by 18 percent
tip = charge * .18

# Calculate sales tax
tax = charge * .07

# Calculate total by adding charge, tip, and tax
total = charge + tip + tax

# Display tip, sales, and total amount
print(f'Tip: {tip:,.2f}')
print(f'Sales tax: {tax:,.2f}')
print(f'Total: {total:,.2f}')
