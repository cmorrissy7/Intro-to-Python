# This program calculates a total number of bugs collected over 5 days

# Initialize an accumulator for number of bugs
total_bugs = 0.0

# Determine total number of bugs caught
for days in range(1, 6):
    bugs_caught = int(input(f'Enter number of bugs collected for day {days}: '))
    total_bugs += bugs_caught # Adds the bugs caught every day to the total

# Display the total number of bugs collected
print(f'Total number of bugs collected: {total_bugs}')
