import re
import curses
from .contact import Contact
from .storage import Storage

class ContactList:
    def __init__(self):
        self.contacts = Storage.load_contacts()

    # Method for creating contacts
    def create_contact(self):
        first_name = self.get_valid_name('Name: ')
        last_name = self.get_valid_name('Last name: ')

        print("\r\nSelect your mobile operator's prefix:")
        print('1) 0412')
        print('2) 0426')
        print('3) 0414')
        print('4) 0424')
        
        question = True
        while question:
            try:
                option = input('\r\nSelect an option: ')
                option = int(option)

                if option == 1:
                    prefix = '412'
                    question = False
                elif option == 2:
                    prefix = '426'
                    question = False
                elif option == 3:
                    prefix = '414'
                    question = False
                elif option == 4:
                    prefix = '424'
                    question = False
                else:
                    print('\r\nInvalid option, please try again')
            except ValueError:
                print('\r\nInvalid input, please enter a number')

        phone_number = self.get_valid_phone_number('Phone number: ')
        # Add country code phone number
        phone_number = f'+58{prefix}{phone_number}'

        # Validate if the phone number already exists
        if self.contact_exists(phone_number):
            print(f'Error: The contact with phone number {phone_number} already exists.')
            return  # Exit without creating the contact
        
        new_contact = Contact(first_name.capitalize(), last_name.capitalize(), phone_number)
        self.contacts.append(new_contact)
        Storage.save_contacts(self.contacts)

        print(f'Contact created: {new_contact}')
    
    # Method to display the contact list
    def show_contacts(self):
        if not self.contacts:
            print('There are no saved contacts.')
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f'{index}. {contact.first_name} {contact.last_name} - Phone: {contact.phone_number}')
    
    # Method to search for contact
    def search_contact(self):
        search_term = input('Enter your search term (first name, last name or phone number): ').strip().lower()

        matching_contacts = [
            contact for contact in self.contacts
            if search_term in contact.first_name.lower() or
                search_term in contact.last_name.lower() or
                search_term in contact.phone_number
        ]

        if not matching_contacts:
            print(f'No contacts were found that match the term: {search_term}')
        else:
            print(f"Search results for '{search_term}':")
            for index, contact in enumerate(matching_contacts,  start=1):
                print(f'{index}. {contact.first_name} {contact.last_name} - Phone: {contact.phone_number}')
    
    # Method to update contact
    def update_contact(self):
        if not self.contacts:
            print('The contact list is empty.')
            return

        def show_contacts_menu(stdscr):
            curses.curs_set(0) # Hide the cursor
            current_row =  0

            while True:
                stdscr.clear()
                stdscr.addstr(0, 0, 'Select a contact to update (use arrows and Enter):')

                # Show contact list
                for index, contact in enumerate(self.contacts):
                    if index == current_row:
                        stdscr.attron(curses.color_pair(1))
                        stdscr.addstr(index + 1, 0, f"{contact.first_name} {contact.last_name} - {contact.phone_number}")
                        stdscr.attroff(curses.color_pair(1))
                    else:
                        stdscr.addstr(index + 1, 0, f'{contact.first_name} {contact.last_name} - {contact.phone_number}')

                stdscr.refresh()
                key = stdscr.getch()

                if key == curses.KEY_UP and current_row > 0:
                    current_row -= 1
                elif key == curses.KEY_DOWN and current_row < len(self.contacts) - 1:
                    current_row += 1
                elif key == curses.KEY_ENTER or key in [10, 13]: 
                    return current_row
                
        # Initialize the curses interface
        curses.wrapper(show_contacts_menu)

        # Get the index of the selected contact
        selected_contact_index = curses.wrapper(show_contacts_menu)

        if selected_contact_index is not None:
            selected_contact = self.contacts[selected_contact_index]
            print(f'You selected: {selected_contact.first_name} {selected_contact.last_name} - {selected_contact.phone_number}')

            # Data to update the contact
            update_first_name = input('Do you want to update the name? (y/n): ').lower() == 'y'
            if update_first_name:
                selected_contact.first_name = self.get_valid_name('Name to update: ')
            
            update_last_name = input('Do you want to update the last name? (y/n): ').lower() == 'y'
            if update_last_name:
                selected_contact.last_name = self.get_valid_name('Last name to update: ')
            
            update_phone_number = input('Do you want to update your phone number? (y/n): ').lower() == 'y'
            if update_phone_number:
                print("\r\nSelect your mobile operator's prefix:")
                print('1) 0412')
                print('2) 0426')
                print('3) 0414')
                print('4) 0424')

                question = True
                while question:
                    try:
                        option = input('\r\nSelect an option: ')
                        option = int(option)

                        if option == 1:
                            prefix = '412'
                            question = False
                        elif option == 2:
                            prefix = '426'
                            question = False
                        elif option == 3:
                            prefix = '414'
                            question = False
                        elif option == 4:
                            prefix = '424'
                            question = False
                        else:
                            print('\r\nInvalid option, please try again')
                    except ValueError:
                        print('\r\nInvalid input, please enter a number')

                new_phone_number = self.get_valid_phone_number('Phone number to update: ')
                selected_contact.phone_number = f'+58{prefix}{new_phone_number}'

            # Save changes
            Storage.save_contacts(self.contacts)
            print('Contact updated successfully.')
    
    # Function to validate the first or last name
    def get_valid_name(self, prompt: str, max_length: int = 15) -> str:
        # Requests a name from the user and validates that it only contains letters
        while True:
            name = input(prompt)
            # Validate name length
            if len(name) > max_length:
                print(f'The name must not exceed {max_length} characters. Please try again.')
                continue
            # Validate that the name only contains letters and spaces
            if re.match(r"^[A-Za-zÀ-ÿ]+$", name):
                return name
            else:
                print('Error: The name must only contain letters. Please try again.')

    # Function to validate the phone number
    def get_valid_phone_number(self, prompt: str) -> str:
        # Request a phone number and validate that it only contains numbers and is 7 characters long
        while True:
            number = input(prompt)
            if re.match(r"^\d{7}$", number):
                return number
            else:
                print('Error: The phone number is invalid')
    
    # Function to validate if the contact already exists
    def contact_exists(self, phone_number: str) -> bool:
        # Check if there is already a contact with the same phone number
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                return True
        return False
    
