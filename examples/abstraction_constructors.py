# Example of Abstraction and Constructors in Python

from abc import ABC, abstractmethod

# Abstraction Example
# Abstraction is a concept where we hide complex implementation details and expose only the necessary parts.
# In Python, we can achieve abstraction using abstract classes and methods.

# Abstract Class
# An abstract class is a class that cannot be instantiated and often contains abstract methods.
# Abstract methods are methods that are declared but contain no implementation.

class Animal(ABC):
    # Abstract method
    # This method must be implemented by any subclass that inherits from Animal.
    @abstractmethod
    def make_sound(self):
        pass

    # Constructor
    # The constructor initializes common attributes for all animals.
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Concrete method
    # This method can be used by all subclasses that inherit from Animal.
    def describe(self):
        return f"{self.name} is a {self.species}."


# Subclass of Animal
# This subclass must implement the abstract method 'make_sound'
class Dog(Animal):
    # Constructor
    # The constructor initializes the name and species attributes of the dog.
    def __init__(self, name):
        # Calling the constructor of the superclass (Animal)
        super().__init__(name, "Dog")

    # Implementation of the abstract method
    def make_sound(self):
        return f"{self.name} says: Woof!"


# Subclass of Animal
# This subclass must also implement the abstract method 'make_sound'
class Cat(Animal):
    # Constructor
    # The constructor initializes the name and species attributes of the cat.
    def __init__(self, name):
        # Calling the constructor of the superclass (Animal)
        super().__init__(name, "Cat")

    # Implementation of the abstract method
    def make_sound(self):
        return f"{self.name} says: Meow!"


# Creating objects of the subclasses
# Note that we cannot create an object of the abstract class Animal directly.
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Using the methods of the subclasses
print(dog.describe())  # Outputs: Buddy is a Dog.
print(dog.make_sound())  # Outputs: Buddy says: Woof!

print(cat.describe())  # Outputs: Whiskers is a Cat.
print(cat.make_sound())  # Outputs: Whiskers says: Meow!
