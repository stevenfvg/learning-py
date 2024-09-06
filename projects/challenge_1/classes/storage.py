import json
import os

from .contact import Contact

class Storage:
    FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'contacts.json')

    @classmethod
    def load_contacts(cls):
        try:
            with open(cls.FILE_PATH, 'r') as file:
                data = json.load(file)
                return [Contact(**contact) for contact in data]
        except FileNotFoundError:
            return []
    
    @classmethod
    def save_contacts(cls, contacts):
        with open(cls.FILE_PATH, 'w') as file:
            json.dump([contact.__dict__ for contact in contacts], file, indent=4)