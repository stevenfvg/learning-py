from .contact import Contact
from .storage import Storage

class ContactList:
    def __init__(self):
        self.contacts = Storage.load_contacts()

    def create_contact(self):
        first_name = input('Name: ')
        last_name = input('Last name: ')
        phone_number = input('Phone number: ')
        
        new_contact = Contact(first_name, last_name, phone_number)
        self.contacts.append(new_contact)
        Storage.save_contacts(self.contacts)

        print(f'Contact created: {new_contact}')