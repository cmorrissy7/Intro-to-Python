# This program takes a person's weight and shows a projected weight for
# each month of weight loss and displays a table with the information

# Ask user for starting weight
weight = int(input('Enter current weight: '))

# Display the table heading
print('\nMonth\tWeight')
print('---------------')

# Subtract that weight by 4 pounds each month and display expected
# weights in a table
for month in range(1, 7):
    weight = weight - 4
    print(f'{month}\t{weight}')

print()
