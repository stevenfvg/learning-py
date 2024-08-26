# Polymorphism in Python

# Polymorphism is an object-oriented programming concept where a single function, method, or operator can operate on different types of objects.
# In simpler terms, it means "many forms."
# Polymorphism allows methods in different classes to have the same name but behave differently.

# Example of Polymorphism with a common method name

class Bird:
    def sound(self):
        # Method that will be overridden in child classes to simulate different bird sounds.
        return "Birds make sounds."

class Sparrow(Bird):
    def sound(self):
        # Overriding the sound method to represent a sparrow's sound.
        return "Sparrow chirps."

class Parrot(Bird):
    def sound(self):
        # Overriding the sound method to represent a parrot's sound.
        return "Parrot talks."

# Example of Polymorphism in action

def make_bird_sound(bird):
    # This function takes a bird object and calls its sound method.
    # Polymorphism allows it to work with any object that has a sound method, regardless of its class.
    return bird.sound()

# Creating objects of different bird classes
sparrow = Sparrow()
parrot = Parrot()

# Demonstrating polymorphism by passing different bird objects to the same function
print(make_bird_sound(sparrow))  # Outputs: Sparrow chirps.
print(make_bird_sound(parrot))   # Outputs: Parrot talks.

# Another example of Polymorphism with built-in functions

# Polymorphism with len() function
# The len() function can be used with different types of objects, such as strings, lists, tuples, etc.
string = "Polymorphism"
my_list = [1, 2, 3, 4, 5]

print(len(string))  # Outputs: 12, the length of the string "Polymorphism"
print(len(my_list))  # Outputs: 5, the number of elements in the list

# Polymorphism with classes having the same method name

class Rectangle:
    def __init__(self, length, width):
        # Constructor initializes the dimensions of the rectangle.
        self.length = length
        self.width = width

    def area(self):
        # Method to calculate the area of a rectangle.
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        # Constructor initializes the radius of the circle.
        self.radius = radius

    def area(self):
        # Method to calculate the area of a circle.
        return 3.14159 * (self.radius ** 2)

# Function to demonstrate polymorphism
def print_area(shape):
    # This function takes an object (shape) and calls its area method.
    # Polymorphism allows it to work with any object that has an area method.
    print(f"The area is: {shape.area()}")

# Creating objects of different shapes
rectangle = Rectangle(4, 5)
circle = Circle(3)

# Demonstrating polymorphism by passing different shape objects to the same function
print_area(rectangle)  # Outputs: The area is: 20
print_area(circle)     # Outputs: The area is: 28.27331

# Polymorphism in Python is not limited to just class inheritance.
# It works with functions, operators, and other built-in methods,
# allowing for flexible and reusable code.
