# This program gets a store's sales for each day of the week
# and then calculates and displays the total sales of the week

# Define main function
def main():
    
    # Create a list of days of the week
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday,',
       'Saturday', 'Sunday']

    # Create accumulator to keep track of total
    total = 0.0

    # Iterate through each element of the list "week"
    for day in week:
        # Ask for the sales for each day
        dailySale = float(input(f'Sales for {day}: '))

        # Add daily sale to total
        total += dailySale

    # Print the new total of all daily sales
    print(f'Total sales for the week: ${total:,.2f}\n')

# Call the main function to execute program
main()
