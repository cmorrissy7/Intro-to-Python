# Ask user for a month, day, and year
month = int(input('Enter a month (numeric): '))
day = int(input('Enter a day: '))
year = int(input('Enter year (last two digits): '))

# Determine if the month times the date equals the year
# and display "The date is magic" if it does
# and display "The date is not magic" if it does not

if month * day == year:
    print('The date is magic')
else:
    print('The date is not magic')
