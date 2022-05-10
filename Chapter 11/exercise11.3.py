# Programming Exercise 11-3

class Person:
    # Create initializer method to hold data attributes
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    # Accessor Methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    # __str__ method for returning state of object
    def __str__(self):
        return f'Name: {self.__name}\n'\
               f'Address: {self.__address}\n'\
               f'Phone Number: {self.__phone}\n'

# Create Customer subclass
class Customer(Person):
    # Create initializer method to inherit Person class data and
    # add specific data for Customer class objects
    def __init__(self, name, address, phone, cust_num, mail):
        # Call the superclass's __init__ method and pass required arguments
        Person.__init__(self, name, address, phone)

        # Initialize Customer-specific attributes
        self.__cust_num = cust_num
        self.__mail = mail

    # Mutators
    def set_cust_num(self, cust_num):
        self.__cust_num = cust_num

    def set_mail(self, mail):
        self.__mail = mail

    # Accessors
    def get_cust_num(self):
        return self.__cust_num

    def get_mail(self):
        return self.__mail

    # __str__ method to return state of object
    def __str__(self):
        return f'Name: {self._Person__name}\n'\
               f'Address: {self._Person__address}\n'\
               f'Phone Number: {self._Person__phone}\n'\
               f'Customer Number: {self.__cust_num}\n'\
               f'Mailing list?: {self.__mail}\n'

# Create simple program to demonstrate an instance of the Customer class
def main():
    # Ask user for customer information
    print('Enter information for a customer.')
    name = input('Name: ')
    address = input('Address: ')
    phone = input('Phone Number: ')
    cust_num = input('Customer Number: ')
    mail = input('Mailing List? (Y or N): ')

    # Set mail variable to boolean value
    if mail == "Y" or mail == "y":
        mail = True
    elif mail == "N" or mail == "n":
        mail = False

    # Create an instance of Customer object using the input as the data attributes
    cust1 = Customer(name, address, phone, cust_num, mail)

    # Display the state of the new object
    print()
    print('Here is the Customer you added and their information.')
    print(cust1)

# Call main function
if __name__ == '__main__':
    main()
