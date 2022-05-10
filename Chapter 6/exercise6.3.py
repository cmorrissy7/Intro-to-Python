# This program asks a user for a file and displays
# the contents of the file with line numbers added
def main():
    # Ask user for the name of a file
    fileName = input('Enter the name of a file: ')

    # Open the file that was entered
    infile = open(fileName, 'r')

    # Add a counter to use for line numbers, starting at 1
    counter = 1

    # Read the file one line at a time
    for line in infile:
        # Strip the newline sequence from line variable
        line = line.rstrip('\n')
        # Display the line with the counter variable entered as a line number
        print(f'{counter}: {line}')
        # Iterate the counter
        counter += 1

    # Close the file
    infile.close()

# Call the main function
main()
