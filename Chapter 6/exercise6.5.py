# This program opens the file numbers.txt and adds
# all of the integers in the file together and then
# displays the total
def main():
    # Open the file numbers.txt
    numbersFile = open('numbers.txt', 'r')

    # Initialize accumulator to 0 to keep total
    total = 0

    # For each line in the file
    for line in numbersFile:
        # Convert the line to an integer
        integer = int(line)

        # Add the integer in the line to the total accumulator
        total += integer

    # Close the file
    numbersFile.close()

    # Display the total accumulator
    print(f'Sum of all integers in file: {total}')

# Call the main function
main()
