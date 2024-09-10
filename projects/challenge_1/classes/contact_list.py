import re
import curses
from .contact import Contact
from .storage import Storage

class ContactList:
    def __init__(self):
        self.contacts = Storage.load_contacts()

    # Method for creating contacts
    def create_contact(self):
        first_name = self.__get_valid_name('Name: ')
        last_name = self.__get_valid_name('Last name: ')
        prefix = self.__select_mobile_operator()
        
        phone_number = self.__get_valid_phone_number('Phone number: ')
        phone_number = f"+58{prefix.lstrip('0')}{phone_number}"
        
        if self.__contact_exists(phone_number):
            print(f'Error: The contact with phone number {phone_number} already exists.')
            return
        
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
        
        selected_contact_index = curses.wrapper(self.__show_contacts_menu)
        selected_contact = self.contacts[selected_contact_index]

        print(f'You selected: {selected_contact.first_name} {selected_contact.last_name} - {selected_contact.phone_number}')
        selected_contact.first_name = self.__update_field('name', selected_contact.first_name).capitalize()
        selected_contact.last_name = self.__update_field('last name', selected_contact.last_name).capitalize()

        if input('Do you want to update your phone number? (y/n): ').lower() == 'y':
            prefix = self.__select_mobile_operator()
            phone_number = self.__get_valid_phone_number('Phone number to update: ')
            selected_contact.phone_number = phone_number = f"+58{prefix.lstrip('0')}{phone_number}"
        
        Storage.save_contacts(self.contacts)
        print('Contact updated successfully.')
    
    # Method to delete contact
    def delete_contact(self):
        if not self.contacts:
            print('The contact list is empty.')
            return
        
        selected_contac_index = curses.wrapper(self.__show_contacts_menu)
        selected_contact = self.contacts[selected_contac_index]

        print(f'You selected: {selected_contact.first_name} {selected_contact.last_name} - {selected_contact.phone_number}')
        # Ask the user if they want to confirm the deletion of the contact
        confirmation = input(f'Are you sure you want to delete {selected_contact.first_name} {selected_contact.last_name}? (y/n): ').lower()

        if confirmation == 'y':
            # Remove contact from list
            del self.contacts[selected_contac_index]
            # Save changes to storage
            Storage.save_contacts(self.contacts)
            print('Contact deleted: {selected_contact.first_name} {selected_contact.last_name}')
        else:
            print('Deletion cancelled.')


    # Function to show contact list using curses
    def __show_contacts_menu(self, stdscr):
        curses.curs_set(0) # Hide the cursor
        curses.start_color() # Enable colors
        # Define green color on black background
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

        current_row =  0

        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, 'Select a contact (use arrows and Enter):')

            for index, contact in enumerate(self.contacts):
                if index == current_row:
                    stdscr.attron(curses.color_pair(1)) # Highlight selection in green.
                    stdscr.addstr(index + 1, 0, f'{contact.first_name} {contact.last_name} - {contact.phone_number}')
                    stdscr.attroff(curses.color_pair(1)) # Turn off the green color when you stop selecting the contact.
                else:
                    stdscr.addstr(index + 1, 0, f'{contact.first_name} {contact.last_name} - {contact.phone_number}')
            
            stdscr.refresh()
            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.contacts) - 1: 
                current_row += 1
            elif key in (curses.KEY_ENTER, 10, 13):
                return current_row
            
    # Function to select mobile operator's prefix
    def __select_mobile_operator(self) -> str:
        options = {
            1: '0412',
            2: '0426',
            3: '0414',
            4: '0424'
        }
        print("\r\nSelect your mobile operator's prefix:")
        for option, prefix in options.items():
            print(f'{option}) {prefix}')
        
        while True:
            try:
                option = int(input('\r\nSelect an option: '))
                if option in options:
                    return options[option]
                else:
                    print('Invalid option, please try again.')
            except ValueError:
                print('Invalid input, please enter a number.')
    
    # Function to update a field
    def __update_field(self, field_name: str, current_value: str) -> str:
        if input(f'Do you want to update the {field_name}? (y/n): ').lower() == 'y':
            return self.__get_valid_name(f'{field_name} to update: ')
        return current_value

    # Function to validate the first or last name
    def __get_valid_name(self, prompt: str, max_length: int = 15) -> str:
        while True:
            name = input(prompt)
            if len(name) > max_length:
                print(f'The name must not exceed {max_length} characters. Please try again.')
                continue
            # Validate that the name only contains letters and spaces
            if re.match(r"^[A-Za-zÀ-ÿ]+$", name):
                return name
            print('Error: The name must only contain letters. Please try again.')

    # Function to validate the phone number
    def __get_valid_phone_number(self, prompt: str) -> str:
        # Request a phone number and validate that it only contains numbers and is 7 characters long
        while True:
            number = input(prompt)
            if re.match(r"^\d{7}$", number):
                return number
            print('Error: The phone number is invalid')
    
    # Function to check if contact already exists
    def __contact_exists(self, phone_number: str) -> bool:
        return any(contact.phone_number == phone_number for contact in self.contacts)
