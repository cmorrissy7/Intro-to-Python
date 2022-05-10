# This program takes a phone number from a user and converts any
# letters to corresponding numbers on a phone pad and displays the new number

def main():
    # Ask user to enter 10 digit phone number in format XXX-XXX-XXXX
    phone_number = input('Enter 10-digit phone number (XXX-XXX-XXXX): ')
    new_number = convert(phone_number)

    # Print the converted phone number
    print(f'Here is the converted phone number: {new_number}\n')

def convert(number):
    # Replace all letters with correct numbers
    number = number.replace('A', '2').replace('B', '2').replace('C', '2')\
             .replace('D', '3').replace('E', '3').replace('F', '3')\
             .replace('G', '4').replace('H', '4').replace('I', '4')\
             .replace('J', '5').replace('K', '5').replace('L', '5')\
             .replace('M', '6').replace('N', '6').replace('O', '6')\
             .replace('P', '7').replace('Q', '7').replace('R', '7').replace('S', '7')\
             .replace('T', '8').replace('U', '8').replace('V', '8')\
             .replace('W', '9').replace('X', '9').replace('Y', '9').replace('Z', '9')
    return number

# Call the main function
main()
