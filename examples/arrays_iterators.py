# Example of a Python list
# Lists are ordered collections that are mutable (modifiable)

fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements in a list
# Elements in a list are accessed using their index, which starts at 0
first_fruit = fruits[0]  # Access the first element
second_fruit = fruits[1]  # Access the second element
last_fruit = fruits[-1]  # Access the last element using negative indexing

print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
print("Last fruit:", last_fruit)

# Iterating over a list using a for loop
print("\nIterating over the list:")
for fruit in fruits:
    print(fruit)

# Example of using the range() function in a for loop
# range() generates a sequence of numbers, which can be used to iterate over list indices
print("\nIterating over the list using range():")
for i in range(len(fruits)):
    print(f"Fruit at index {i}: {fruits[i]}")

# Using the .sort() method
# The .sort() method sorts the elements of the list in ascending order by default
numbers = [5, 2, 9, 1, 5, 6]
print("\nOriginal numbers list:", numbers)
numbers.sort()
print("Sorted numbers list:", numbers)

# Using the .append() method
# The .append() method adds an element to the end of the list
fruits.append("elderberry")
print("\nList after appending 'elderberry':", fruits)

# Using the .pop() method
# The .pop() method removes and returns the last element from the list by default
# You can also specify an index to remove a specific element
popped_fruit = fruits.pop()  # Removes the last element
print("\nPopped fruit:", popped_fruit)
print("List after popping the last fruit:", fruits)

# Using the .remove() method
# The .remove() method removes the first occurrence of a specified element from the list
# If the element is not found, it raises a ValueError
fruits.remove("banana")
print("\nList after removing 'banana':", fruits)