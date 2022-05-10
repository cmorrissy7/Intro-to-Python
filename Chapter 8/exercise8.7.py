# This program reads a file's contents and determines the number
# of uppercase letters, lowercase letters, digits, and whitespaces

def main():
    # Open the file for reading
    infile = open('text.txt', 'r')

    # Read the file's contents into a string
    contents = infile.read()

    # Close the file
    infile.close()
    
    # Accumulator variables to hold information
    uppercases = 0
    lowercases = 0
    digits = 0
    whitespaces = 0
    
    # Iterate through each character of the file_contents
    for ch in contents:
        # If the character is uppercase, add it to the uppercases accumulator
        if ch.isupper():
            uppercases += 1
        # If the character is lowercase, add it to lowercases accumulator
        if ch.islower():
            lowercases += 1
        # If the character is a number, add it to the digits accumulator
        if ch.isdigit():
            digits += 1
        # If the character is a whitespace character, add it to that accumulator
        if ch.isspace():
            whitespaces += 1

    # Display the file's information
    print('Here is information on the "text.txt" file:')
    print(f'Uppercase letters: {uppercases}')
    print(f'Lowercase letters: {lowercases}')
    print(f'Digits: {digits}')
    print(f'Whitespace characters: {whitespaces}')

# Call the main function
if __name__ == '__main__':
    main()
    
