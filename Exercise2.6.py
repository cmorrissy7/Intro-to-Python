# Get amount of purchase
purchase = float(input('Enter amount of purchase: '))

# Calculate sales tax by mulitplying amount by 5 percent
state_tax = purchase * .05

# Calculate county tax by multiplying amount by 2.5 percent
county_tax = purchase * .025

# Calculate total tax amount
total_tax = state_tax + county_tax

# Calculate the total of the sale by adding purchase
# amount and total tax
total_sale = purchase + total_tax

# Display purchase amount, state tax, county tax,
# total tax, and total of the sale
print(f'Purchase amount: {purchase:,.2f}')
print(f'State sales tax: {state_tax:,.2f}')
print(f'County sales tax: {county_tax:,.2f}')
print(f'Total sales tax: {total_tax:,.2f}')
print(f'Total of sale: {total_sale:,.2f}')
