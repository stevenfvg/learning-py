import os

# Default name of the created directory
PATH = 'contacts/'
FILE_EXTENSION = '.txt'

class Contact:

    def __init__(self, first_name: str, last_name: str, phone_number: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

class ContactList:
    
    def __init__(self, contact_name: str) -> None:
        self.name = contact_name

    # Add method to add new contact

    # Add method to update contact

    # Add method to display contact list

    # Add method to search for contact

    # Add method to delete contact

# Main function of the program
def app():
    # Call the function to check if the directory exists or not
    create_directory() # Default extension for contacts
    # Show options menu
    show_menu()

    # Ask the user for the action to perform
    question = True
    while question:
        option = input('\r\nSelect an option: ')
        option = int(option)

        # Execute the options
        if option == 1:
            print('Adding a new contact...')
            question = False
        elif option == 2:
            print('Edit contact...')
            question = False
        elif option == 3:
            print('Showing contact list...')
            question = False
        elif option == 4:
            print('Searching...')
            question = False
        elif option == 5:
            print('Delete contact...')
            question = False
        elif option == 0:
            print('Closing the program...')
            question = False
        else:
            print('Invalid option, please try again')

def show_menu():
    print('Options menu:')
    print('1) Add new contact')
    print('2) Edit contact')
    print('3) View contacts')
    print('4) Search contact')
    print('5) Delete contact')
    print('0) Exit')

def create_directory():
    if not os.path.exists(PATH):
        os.makedirs(PATH)

app()

