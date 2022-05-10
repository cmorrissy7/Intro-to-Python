# Programming Exercise 10-3

class PersonalInfo:
    # Create initializer method to hold data attributes
    def __init__(self, name, address, age, phone_num):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_num = phone_num

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_num

    # Create __str__ method to return state of object
    def __str__(self):
        return f'Name: {self.__name}\n'\
               f'Address: {self.__address}\n'\
               f'Age: {self.__age}\n'\
               f'Phone Number: {self.__phone_num}\n'

# Define main method which will create 3 instances of the PersonalInfo object
# with their own instance attributes
def main():
    # Create the object instances
    me = PersonalInfo('Connor', '123 A Street', 27, '123-456-7890')
    friend1 = PersonalInfo('Brian', '234 B Street', 28, '098-765-4321')
    friend2 = PersonalInfo('Ashley', '345 C Street', 25, '111-222-3333')

    # Display the states of the objects (for grading purpose)
    print(me)
    print(friend1)
    print(friend2)

# Call the main method
if __name__ == '__main__':
    main()
    
