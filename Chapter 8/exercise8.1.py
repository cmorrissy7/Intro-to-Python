# This program gets a name from a user and displays their initials
def main():
    try:
        # Ask user to enter full name
        fullName = input('Enter a full name (first, middle, and last): ')

        # Split the string
        nameList = fullName.split()

        # Assign each token to corresponding name variable
        firstName = nameList[0]
        middleName = nameList[1]
        lastName = nameList[2]

        # Display first letter of each part of name with a period and space
        # between them
        print(f'{firstName[0].upper()}. {middleName[0].upper()}. {lastName[0].upper()}.')

    # Display messages for errors
    except IndexError:
        print('Error: Must enter first, middle, and last name.')
    except:
        print('Error occured.')

# Call main function
main()
