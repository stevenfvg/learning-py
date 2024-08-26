# Inheritance in Python

# Inheritance is a mechanism in object-oriented programming that allows a class to inherit attributes and methods from another class.
# The class that is inherited from is called the "parent" or "base" class.
# The class that inherits is called the "child" or "derived" class.

# Parent class
class Animal:
    def __init__(self, name, species):
        # Constructor initializes the name and species of the animal.
        self.name = name
        self.species = species

    def make_sound(self):
        # Method to simulate the sound made by the animal.
        return f"{self.name} makes a sound."

    def move(self):
        # Method to simulate the movement of the animal.
        return f"{self.name} moves around."

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # The Dog class inherits from Animal and adds a new attribute: breed.
        # We use super() to call the constructor of the parent class.
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        # Overriding the make_sound method to customize it for a dog.
        return f"{self.name} barks."

    def fetch(self):
        # New method specific to the Dog class.
        return f"{self.name} is fetching the ball."

# Another child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, color):
        # The Cat class inherits from Animal and adds a new attribute: color.
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        # Overriding the make_sound method to customize it for a cat.
        return f"{self.name} meows."

    def scratch(self):
        # New method specific to the Cat class.
        return f"{self.name} is scratching the furniture."

# Creating an object of the Dog class
dog = Dog("Buddy", "Golden Retriever")
print(dog.make_sound())  # Outputs: Buddy barks.
print(dog.move())        # Outputs: Buddy moves around.
print(dog.fetch())       # Outputs: Buddy is fetching the ball.

# Creating an object of the Cat class
cat = Cat("Whiskers", "Gray")
print(cat.make_sound())  # Outputs: Whiskers meows.
print(cat.move())        # Outputs: Whiskers moves around.
print(cat.scratch())     # Outputs: Whiskers is scratching the furniture.

# The Dog and Cat classes both inherit the move method from the Animal class,
# but they have their own implementations of the make_sound method.

# Checking the type and inheritance
print(isinstance(dog, Dog))        # Outputs: True
print(isinstance(dog, Animal))     # Outputs: True
print(isinstance(cat, Cat))        # Outputs: True
print(isinstance(cat, Animal))     # Outputs: True
