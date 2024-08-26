# Detailed Explanation of Getter and Setter Methods in Python

class Employee:
    def __init__(self, first_name, last_name, salary):
        # Constructor initializes the employee's first name, last name, and salary.
        # The salary is a private attribute to protect it from unauthorized changes.
        self.first_name = first_name
        self.last_name = last_name
        self.__salary = salary  # Private attribute

    # Getter method for salary
    # This method allows us to access the private attribute __salary from outside the class.
    def get_salary(self):
        print("Getting salary...")
        return self.__salary

    # Setter method for salary
    # This method allows us to modify the private attribute __salary from outside the class.
    # It includes validation logic to ensure that the salary is a positive number.
    def set_salary(self, new_salary):
        if new_salary > 0:
            print("Setting salary...")
            self.__salary = new_salary
        else:
            print("Invalid salary! Salary must be a positive number.")

    # Getter method for the full name
    # This method provides a convenient way to get the full name of the employee.
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Setter method for the full name
    # This method allows us to set both the first and last names using a single string.
    def set_full_name(self, full_name):
        first, last = full_name.split()
        self.first_name = first
        self.last_name = last


# Creating an object of the Employee class
employee = Employee("John", "Doe", 50000)

# Accessing the salary using the getter method
current_salary = employee.get_salary()
print(f"Current Salary: ${current_salary}")  # Outputs: Current Salary: $50000

# Modifying the salary using the setter method
employee.set_salary(55000)
print(f"Updated Salary: ${employee.get_salary()}")  # Outputs: Updated Salary: $55000

# Trying to set an invalid salary
employee.set_salary(-1000)  # Outputs: Invalid salary! Salary must be a positive number.

# Accessing the full name using the getter method
full_name = employee.get_full_name()
print(f"Full Name: {full_name}")  # Outputs: Full Name: John Doe

# Modifying the full name using the setter method
employee.set_full_name("Jane Smith")
print(f"Updated Full Name: {employee.get_full_name()}")  # Outputs: Updated Full Name: Jane Smith
print(f"First Name: {employee.first_name}")  # Outputs: First Name: Jane
print(f"Last Name: {employee.last_name}")  # Outputs: Last Name: Smith

# Encapsulation in action
# Direct access to the private attribute __salary is not allowed
# Uncommenting the following line will raise an AttributeError
# print(employee.__salary)
