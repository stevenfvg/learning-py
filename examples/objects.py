# Example of a Python dictionary
# A dictionary is a collection of key-value pairs where each key is unique
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing elements in a dictionary
# You can access the value associated with a key using the key name
person_name = person["name"]
person_age = person["age"]
person_city = person["city"]

print("Name:", person_name)
print("Age:", person_age)
print("City:", person_city)

# Mixing dictionary values with a string
# You can combine dictionary values with strings using string formatting
greeting = f"Hello, my name is {person['name']} and I am {person['age']} years old."
print("\nGreeting:", greeting)

# Adding new key-value pairs to the dictionary
# You can add a new key-value pair by simply assigning a value to a new key
person["email"] = "john@example.com"
print("\nDictionary after adding 'email':", person)

# Replacing (updating) an existing value
# To update the value associated with a key, assign a new value to that key
person["city"] = "San Francisco"
print("\nDictionary after updating 'city':", person)

# Removing a key-value pair from the dictionary
# You can remove a key-value pair using the del statement or the pop() method
del person["age"]  # Using del to remove the key 'age'
print("\nDictionary after removing 'age' using del:", person)

# Alternatively, you can use the pop() method to remove a key-value pair
# The pop() method also returns the value associated with the removed key
removed_value = person.pop("email")  # Using pop() to remove 'email'
print("\nDictionary after removing 'email' using pop():", person)
print("Removed value:", removed_value)