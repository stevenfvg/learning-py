# Example of using comparison operators to evaluate conditions

a = 10
b = 5
c = 15

# Comparison operators:
# > : Greater than
# < : Less than
# >=: Greater than or equal to
# <=: Less than or equal to
# ==: Equal to
# !=: Not equal to

# Using if-else statement
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Nested if example
# If-else statements can be nested to check multiple conditions
if a > b:
    if a > c:
        print("a is greater than both b and c")
    else:
        print("a is greater than b but not greater than c")
else:
    print("a is not greater than b")

# Using elif (else if) statement
# The elif statement is used to check multiple conditions one after another
if a > b and a > c:
    print("a is the greatest number")
elif b > a and b > c:
    print("b is the greatest number")
else:
    print("c is the greatest number")

# Example of using the and operator
# The and operator returns True if both conditions are True
x = 7
y = 3
z = 12

if x > y and z > y:
    print("x and z are both greater than y")

# Example of using the or operator
# The or operator returns True if at least one of the conditions is True
if x > y or x > z:
    print("x is greater than y or z (or both)")

# Lists, iterators, and if statement example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []

# Iterating over a list and using if to check if a number is even or odd
for number in numbers:
    if number % 2 == 0:  # The modulus operator (%) returns the remainder of division
        even_numbers.append(number)  # If the number is even, add it to the even_numbers list
    else:
        odd_numbers.append(number)  # If the number is odd, add it to the odd_numbers list

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)