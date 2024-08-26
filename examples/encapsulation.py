# Encapsulation in Python

# Encapsulation is a concept in object-oriented programming where we restrict access to the attributes and methods of a class.
# This is done to protect the integrity of the object's data and prevent unauthorized access or modification.

class Person:
    # Constructor
    # The constructor initializes the attributes of the class.
    def __init__(self, name, age):
        # Public attribute
        # This attribute is accessible from outside the class.
        self.name = name

        # Private attribute
        # This attribute is not accessible directly from outside the class.
        # A private attribute is denoted by a double underscore prefix.
        self.__age = age

    # Public method
    # This method is accessible from outside the class.
    def display_info(self):
        # Accessing a private attribute within the class
        return f"Name: {self.name}, Age: {self.__age}"

    # Getter method
    # This method is used to access the value of a private attribute.
    def get_age(self):
        return self.__age

    # Setter method
    # This method is used to modify the value of a private attribute.
    # It can include logic to validate the data before setting it.
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age.")

# Creating an object of the Person class
person = Person("John Doe", 30)

# Accessing a public attribute
# You can access and modify public attributes directly.
print(person.name)  # Outputs: John Doe

# Accessing a private attribute (Not recommended)
# The following line will raise an AttributeError because __age is private.
# print(person.__age)  # Uncommenting this line will cause an error

# Accessing a private attribute using a public method
# Private attributes can be accessed through public methods, such as getters.
print(person.display_info())  # Outputs: Name: John Doe, Age: 30

# Modifying a private attribute using a setter method
# Private attributes can be modified through public methods, such as setters.
person.set_age(35)
print(person.display_info())  # Outputs: Name: John Doe, Age: 35

# Attempting to set an invalid age
person.set_age(-5)  # Outputs: Please enter a valid age.

# Using the getter method to access the private attribute
print(f"The person's age is {person.get_age()}")  # Outputs: The person's age is 35

# Private attributes can also be accessed using name mangling
# This is not recommended as it breaks encapsulation.
# The following line accesses the private attribute using the _ClassName__attributeName pattern.
print(person._Person__age)  # Outputs: 35 (but this is not recommended)
