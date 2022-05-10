# This program asks the user for a time period of days and then calculates
# the salary if the salary doubles every day, starting from $.01

# Ask user for number of days
time_period = int(input('Enter a number of days: '))

# Accumulator variable to keep track of total salary
total_salary = .01

# Starting salary constant
salary = .01

# Print the table heading
print('Day\tSalary')
print('-----------')

# Print the first day salary
print('1\t$0.01')

# Calculate salary
for day in range(2, time_period +1):
    salary = salary * 2
    total_salary += salary
    print(f'{day}\t${salary:,.2f}')

# Display total salary
print()
print(f'Total salary paid: ${total_salary:,.2f}')
