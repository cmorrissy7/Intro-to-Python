# Programming Exercise 11-2

# Import Employee class from employee module (exercise11.1)
from employee import Employee

# Create a new subclass for shift supervisor
class ShiftSupervisor(Employee):
    # Create initializer method to inherit Employee class data
    # and add specific data for Shift Supervisors
    def __init__(self, name, num, salary, bonus):
        # Call Employee's __init__ method to inherit data attributes
        Employee.__init__(self, name, num)

        # Initialize specific data attributes
        self.__salary = salary
        self.__bonus = bonus

    # Mutator methods
    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    # Accessor methods
    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus

    # __str__ method to return state of object
    def __str__(self):
        return f'Employee Name: {self._Employee__name}\n'\
               f'Employee Number: {self._Employee__number}\n'\
               f'Annual Salary: ${self.__salary:,.2f}\n'\
               f'Annual Bonus: ${self.__bonus:,.2f}\n'

# Create a program that uses a ShiftSupervisor object
def main():
    # Create a ShiftSupervisor object with random data
    supervisor = ShiftSupervisor('Connor', '12345', 70000, 5000)

    # Display current data in ShiftSupervisor object
    print(supervisor)
    print()

    # Change values of salary and bonus data attributes
    supervisor.set_salary(80000)
    supervisor.set_bonus(6000)

    # Display the newly-changed data in ShiftSupervisor object
    print(supervisor)
    print()

# Call main function
if __name__ == '__main__':
    main()
