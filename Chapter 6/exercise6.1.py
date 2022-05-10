# This program displays the content of a file
def main():
    try:
        # Open the numbers.txt file in read mode
        infile = open('numbers.txt', 'r')

        # Read the contents of the file
        fileContents = infile.read()

        # Close the file
        infile.close()

        # Print the contents of the file
        print(fileContents)

    # Creates exception for not finding a file   
    except FileNotFoundError:
        print('File was not found.')

# Call the main function
main()
