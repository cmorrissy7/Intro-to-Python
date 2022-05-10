# Programming Exercise 2 - Capital Quiz

# Constant for number of states to quiz the user on
NUM_STATES = 5

def main():
    # Initialize the state capital dictionary
    state_caps = state_cap_dictionary()

    # Initialize variables to count the number of correct and incorrect responses
    correct = 0
    incorrect = 0

    # Explain program to user
    print('This program will quiz you on the U.S. State capitals.')
    print("Enter the state's capital.\n")

    # Create a loop that iterates 5 times and quizzes the user
    for count in range(NUM_STATES):
        # Get a random entry from the dictionary and remove it(so its not chosen again)
        state, capital = state_caps.popitem()

        # Quiz the user.
        print(f'What is the capital of {state}? ')
        response = input()

        # Check if response is correct
        if response.lower() == capital.lower():
            # Add one to correct counter
            correct += 1
            print('Correct!\n')
        else:
            incorrect += 1
            print('Incorrect.\n')

    # Display the results
    print(f'Correct responses: {correct}')
    print(f'Incorrect responses: {incorrect}\n')
    
# Create function that builds dictionary with States and capitals
def state_cap_dictionary():
    # Create a dictionary with U.S. states as keys and their capitals as values
    sc = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix',
          'Arkansas':'Little Rock', 'California':'Sacramento', 'Colorado':'Denver',
          'Connecticut':'Hartford', 'Delaware':'Dover', 'Florida':'Tallahassee',
          'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise',
          'Illinois':'Springfield', 'Indiana':'Indianapolis', 'Iowa':'Des Moines',
          'Kansas':'Topeka', 'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
          'Maine':'Augusta', 'Maryland':'Annapolis', 'Massachusettes':'Boston',
          'Michigan':'Lansing', 'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
          'Missouri':'Jefferson City', 'Montana':'Helena', 'Nebraska':'Lincoln',
          'Nevada':'Carson City', 'New Hampshire':'Concord', 'New Jersey':'Trenton',
          'New Mexico':'Santa Fe', 'New York':'Albany', 'North Carolina':'Raleigh',
          'North Dakota':'Bismark', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
          'Oregon':'Salem', 'Pennsylvania':'Harrisburg', 'Rhode Island':'Providence',
          'South Carolina':'Columbia', 'South Dakota':'Pierre', 'Tennessee':'Nashville',
          'Texas':'Austin', 'Utah':'Salt Lake City', 'Vermont':'Montpelier',
          'Virginia':'Richmond', 'Washington':'Olympia', 'West Virginia':'Charleston',
          'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

    return sc

# Call main function
if __name__ == '__main__':
    main()
