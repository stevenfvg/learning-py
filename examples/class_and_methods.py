# This is a basic example of how classes and methods work in Python.

# Defining a class
# A class is a blueprint for creating objects (instances)
class Dog:
    # The __init__ method is the constructor of the class
    # It initializes the attributes of the class
    def __init__(self, name, age, breed):
        # 'self' refers to the current instance of the class
        # Assigning parameters to instance attributes
        self.name = name
        self.age = age
        self.breed = breed

    # Defining a method
    # A method is a function that belongs to an object
    def bark(self):
        # This method will make the dog bark
        return f"{self.name} says: Woof!"

    # Another method to describe the dog
    def describe(self):
        # This method provides a description of the dog
        return f"{self.name} is a {self.age}-year-old {self.breed}."

    # Method to calculate dog years (1 human year = 7 dog years)
    def calculate_dog_years(self):
        # This method calculates the dog's age in dog years
        dog_years = self.age * 7
        return f"{self.name} is {dog_years} years old in dog years."


# Creating an object (instance) of the Dog class
# When you create an object, the __init__ method is called automatically
my_dog = Dog("Buddy", 3, "Golden Retriever")

# Accessing the attributes of the object
# You can access the attributes using dot notation
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
print(f"My dog is a {my_dog.breed}.")

# Calling methods of the object
# You can call the methods using dot notation
print(my_dog.bark())  # This will make the dog bark
print(my_dog.describe())  # This will describe the dog
print(my_dog.calculate_dog_years())  # This will calculate the dog's age in dog years

# You can create multiple objects from the same class
another_dog = Dog("Max", 5, "Bulldog")
print(another_dog.describe())  # This will describe the other dog
