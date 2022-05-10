# Programming Exercise 11-1

# Create superclass Employee that holds info on employees
class Employee:
    # Create initializer method to hold data attributes
    def __init__(self, name, num):
        self.__name = name
        self.__number = num

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_number(self, num):
        self.__number = num
        
    # Accessor methods
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    # Create str method to return state of object
    def __str__(self):
        return f'Employee Name: {self.__name}\n'\
               f'Employee Number: {self.__number}\n'

# Create subclass ProductionWorker from Employee superclass
class ProductionWorker(Employee):
    # Create initializer method to inherit Employee class data
    # and add specific data for Production Workers
    def __init__(self, name, num, shift, pay):
        # Call the superclass's __init__ method and pass the required arguments.
        Employee.__init__(self, name, num)

        # Initialize shift and pay attributes
        self.__shift = shift
        self.__pay = pay

    # Add mutators for shift and pay
    def set_shift(self, shift):
        self.__shift = shift

    def set_pay(self, pay):
        self.__pay = pay

    # Add accessors for shift and pay
    def get_shift(self):
        return self.__shift

    def get_pay(self):
        return self.__pay

    # __str__ method to return state of object
    def __str__(self):
        return f'Employee Name: {self.__name}\n'\
               f'Employee Number: {self.__number}\n'\
               f'Shift: {self.__shift}\n'\
               f'Pay Rate: ${self.__pay:,.2f}\n'

# Create main function that will create a ProductionWorker object
# from user input, and then display it
def main():
    # Ask user to enter employee information
    print('Enter Employee Information')
    name = input('Employee Name: ')
    num = input('Employee Number: ')
    shift = int(input('Shift (enter 1 for day shift or 2 for night shift): '))
    pay = input('Pay Rate: ')

    # Create a ProductionWorker object with this info
    worker = ProductionWorker(name, num, shift, pay)

    # Use the object's accessor methods to display info on screen
    print('Employee Information:')
    print('Employee Name: ' + worker.get_name())
    print('Employee Number: ' + worker.get_number())
    print('Shift:', worker.get_shift())
    print('Pay Rate (in dollars):', worker.get_pay())

    print(worker)

# Call main function
if __name__ == '__main__':
    main()
