# Get price of all five items
price1 = float(input('Price of item: '))
price2 = float(input('Price of item: '))
price3 = float(input('Price of item: '))
price4 = float(input('Price of item: '))
price5 = float(input('Price of item: '))

# Calculate subtotal by adding all items.
subtotal = price1 + price2 + price3 + price4 + price5

# Calculate sales tax by multiplying subtotal by 7 percent
sales_tax = subtotal * .07

# Calculate total by adding subtotal and sales tax
total = subtotal + sales_tax

# Display subtotal, sales tax, and total
print(f'Subtotal: {subtotal:,.2f}')
print(f'Sales tax: {sales_tax:,.2f}')
print(f'Total: {total:,.2f}')

