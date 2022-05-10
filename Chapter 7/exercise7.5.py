# This program reads the file "charge_accounts.txt"
# and puts it's contents in a list

def main():
    # Open the file for reading
    infile = open('charge_accounts.txt', 'r')

    # Read the contents of the file into a list
    accounts = infile.readline()

    # Close the file
    infile.close()

    # Ask user to enter a charge account number
    search = input('Enter a charge account number to search for: ')

    # Determine if account number entered is in the list
    if search in accounts:
        print(f'The account number {search} is valid.')
    else:
        print(f'The account number {search} is invalid.')

# Call the main function
main()
