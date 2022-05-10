# Programming Exercise 10-4

class Employee:
    # Create initializer method to hold data attributes
    def __init__(self, name, id_num, department, job_title):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__job_title = job_title

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_id_num(self):
        return self.__id_num

    def get_department(self):
        return self.__department

    def get_job_titleber(self):
        return self.__job_title

    # Create __str__ method to return state of object
    def __str__(self):
        return f'Name: {self.__name}\n'\
               f'ID #: {self.__id_num}\n'\
               f'Department: {self.__department}\n'\
               f'Job Title: {self.__job_title}\n'

# Define main method which will create 3 instances of the Employee object
# with their own instance attributes
def main():
    # Create the object instances
    employee1 = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    employee2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
    employee3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

    # Display the data for each employee
    print(employee1)
    print(employee2)
    print(employee3)

# Call the main method
if __name__ == '__main__':
    main()
    
