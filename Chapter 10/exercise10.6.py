# Programming Exercise 10-6

# Create class that makes objects that hold information about a patient
class Patient:
    # Create initializer method to hold data attributes for a patient
    def __init__(self, first_name, mid_name, last_name, address,
                 city, state, zip_code, phone, emer_name, emer_phone):
        self.__first_name = first_name
        self.__mid_name = mid_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__zip_code = zip_code
        self.__phone = phone
        self.__emer_name = emer_name
        self.__emer_phone = emer_phone

    # Mutator methods
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_mid_name(self, mid_name):
        self.__mid_name = mid_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_zip_code(self, zip_code):
        self.__zip_code

    def set_phone(self, phone):
        self.__phone = phone

    def set_emer_name(self, emer_name):
        self.__emer_name = emer_name

    def set_emer_phone(self, emer_phone):
        self.__emer_phone = emer_phone

    # Accessor methods
    def get_first_name(self):
        return self.__first_name

    def get_mid_name(self):
        return self.__mid_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_zip_code(self):
        return self.__zip_code

    def get_phone(self):
        return self.__phone

    def get_emer_name(self):
        return self.__emer_name

    def get_emer_phone(self):
        return self.__emer_phone

    # Create __str__ method to return state of object
    def __str__(self):
        return f'First Name: {self.__first_name}\n'\
               f'Middle Name: {self.__mid_name}\n'\
               f'Last Name: {self.__last_name}\n'\
               f'Address: {self.__address}\n'\
               f'City: {self.__city}\n'\
               f'Zip: {self.__zip_code}\n'\
               f'Phone: {self.__phone}\n'\
               f'Emergency Contact: {self.__emer_name}\n'\
               f'Emergency Phone: {self.__emer_phone}\n'

# Create class that makes objects that hold information about procedures done on patients
class Procedure:
    # Create initializer method to hold data attributes for a procedure
    def __init__(self, name, date, prac, charge):
        self.__name = name
        self.__date = date
        self.__prac = prac
        self.__charge = charge

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_prac(self, prac):
        self.__prac = prac

    def set_charge(self, charge):
        self.__charge = charge

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_prac(self):
        return self.__prac

    def get_charge(self):
        return self.__charge

    # Create __str__ method to return the state of the object
    def __str__(self):
        return f'Procedure Name: {self.__name}\n'\
               f'Date: {self.__date}\n'\
               f'Practitioner: {self.__prac}\n'\
               f'Charge: ${self.__charge:,.2f}\n'

# Create main function
def main():
    # Create an instance of the Patient class with random data
    patient1 = Patient('Connor', 'John', 'Morrissy', '123 A St.', 'Steger', 'IL',
                       '60477', '111-222-3333', 'Elizabeth', '999-999-9999')

    # Create 3 instances of the Procedure class with data from book
    procedure1 = Procedure('Pyhsical Exam', '4/28/2022', 'Dr. Irvine', 250.00)
    procedure2 = Procedure('X-ray', '4/28/2022', 'Dr. Jamison', 500.00)
    procedure3 = Procedure('Blood Test', '4/28/2022', 'Dr. Smith', 200.00)

    # Display the patient's information
    print(patient1)

    # Display information about all 3 procedures
    print(procedure1)
    print(procedure2)
    print(procedure3)

    # Find the total of charges from all 3 procedures
    total = procedure1.get_charge() + procedure2.get_charge() + procedure3.get_charge()

    # Display the total charges
    print(f'Total Charges: ${total:,.2f}\n')

# Call the main function
if __name__ == '__main__':
    main()
