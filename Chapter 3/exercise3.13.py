# Ask user to enter weight of a package
weight = float(input('Enter package weight (lbs): '))

# Calculate shipping charges by weight
if weight <= 2:
    print('Shipping charges: $1.50')
elif weight > 2 and weight <= 6:
    print('Shipping charges: $3.00')
elif weight > 6 and weight <= 10:
    print('Shipping charges: $4.00')
elif weight > 10:
    print('Shipping charges: $4.75')
