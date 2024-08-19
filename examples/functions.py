# Example of functions with parameters and arguments, and functions that return values in Python.

# Function with parameters and arguments
def greet(name, age):
    """
    This function takes a name and age as parameters
    and prints a greeting message.
    """
    print(f"Hello {name}, you are {age} years old.")

# Calling the function with arguments
greet("Alice", 30)
greet("Bob", 25)

# Function that returns a value
def add_numbers(a, b):
    """
    This function takes two numbers as parameters,
    adds them together, and returns the result.
    """
    return a + b

# Storing the returned value in a variable
result = add_numbers(5, 7)
print(f"The result of addition is: {result}")

# Function with default parameter values
def greet_with_default(name, age=20):
    """
    This function takes a name as a required parameter
    and age as an optional parameter with a default value of 20.
    """
    print(f"Hello {name}, you are {age} years old.")

# Calling the function with and without the optional argument
greet_with_default("Charlie")
greet_with_default("Diana", 35)

# Difference between Functions and Methods
# - A function is a block of code that performs a specific task and is defined using the `def` keyword.
#   Functions can be called independently using their name.
# - A method is similar to a function, but it is associated with an object and is called on that object.
#   Methods are functions that belong to a class and are called using the dot notation (object.method()).

# Example of a method
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        """
        This is a method that belongs to the Dog class.
        It prints a message when the dog barks.
        """
        print(f"{self.name} says: Woof!")

# Creating an instance of the Dog class
my_dog = Dog("Rex")

# Calling the method on the object
my_dog.bark()

# In this example:
# - `greet`, `add_numbers`, and `greet_with_default` are functions because they are defined outside of any class.
# - `bark` is a method because it is defined within the `Dog` class and is associated with an instance of `Dog`.