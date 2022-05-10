# Programming Exercise 7 - World Series Winners

# Global Constants
START_YEAR = 1903

# Define main fucntion
def main():
    # Open file for reading
    infile = open('WorldSeriesWinners.txt', 'r')

    # Read contents of file to a list and strip \n
    winners = infile.readlines()

    # Create frequency dictionary
    winner_frequency = create_frequency_dictionary(winners)

    # Create yearly winner dictionary
    yearly_winners = create_winners_dictionary(winners)

    # Ask user for a year between 1903 and 2009
    search = int(input('Enter a year between 1903 and 2009: '))

    # Check response for years where World Series was not played
    # and display message informing the user, and then exit the program
    if search == 1904 or search == 1994:
        print('World Serires was not played this year.\n')
        return exit

    # Display the name of the team that won that year
    if search in yearly_winners:
        print(f'Team that won this year: {yearly_winners[search]}')
    else:
        print('Invalid year entered.\n')

    # Display the number of times the team has won a World Series
    if search in yearly_winners:
        if yearly_winners[search] in winner_frequency:
            print('This team has won', winner_frequency.get(yearly_winners[search]), 'World Series.\n')
            
# Define fucntion that creates a dictionary out of a list with the values
# being the amount of times the key appears in the list
def create_frequency_dictionary(list):
    # Create empty dictionary
    frequency = {}

    # Iterate over the list
    for item in list:
        # If this item is already in the frequency dictionary...
        if item in frequency:
            #...then add 1 to the value of that item
            frequency[item] += 1
        # Else, if item is not already in the frequency dictionary...
        else:
            #...then initialize the count for that item
            frequency[item] = 1

    # Return the dictionary
    return frequency

# Define function that creates a dictionary where they keys are they years
# and the values are they team that won
def create_winners_dictionary(winner_list):
    # Pass the global variable
    global START_YEAR
    # Create an empty dictionary
    all_winners = {}

    # Iterate through the list and use it to populate the dictionary
    for item in winner_list:
        # Add element to dictionary with items in winners as the value
        # and the year they won as the key
        all_winners[START_YEAR] = item
        # Add one to the year so that it increases once for each entry
        START_YEAR += 1

    # Return the dictionary
    return all_winners

# Call main function
if __name__ == '__main__':
    main()
