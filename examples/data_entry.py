# Python user input example

# This program will ask the user to enter a number
# and will determine if the number is even or odd.
# The program will continue to run until the user types 'exit'.

while True:
    # Ask the user to enter a number or type 'exit' to quit
    user_input = input("Please enter a number (or type 'exit' to quit): ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break  # Exit the while loop

    # Try to convert the input to an integer
    try:
        number = int(user_input)

        # Check if the number is even or odd
        if number % 2 == 0:
            print(f"The number {number} is even.")
        else:
            print(f"The number {number} is odd.")
    
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("That is not a valid number. Please try again.")
