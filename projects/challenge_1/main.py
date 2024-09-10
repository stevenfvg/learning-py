from classes.contact_list import ContactList

def main():
    # Instance of the ContactList class
    contact_list = ContactList()
    show_options_menu()
    
    # Ask the user for the action to perform
    question = True
    while question:
        try:
            option = input('\r\nSelect an option: ')
            option = int(option)
            # Execute the options
            if option == 1:
                print('\r\nAdd new contact')
                contact_list.create_contact()
                show_options_menu()
            elif option == 2:
                print('\r\nContact list:')
                contact_list.show_contacts()
                show_options_menu()
            elif option == 3:
                print('\r\nSearch contact')
                contact_list.search_contact()
                show_options_menu()
            elif option == 4:
                print('\r\nUpdate contact')
                contact_list.update_contact()
                show_options_menu()
            elif option == 5:
                print('\r\nDelete contact')
                contact_list.delete_contact()
                show_options_menu()
            elif option == 0:
                print('\r\nClosing the program...')
                break
            else:
                print('\r\nInvalid option, please try again')
        except ValueError:
            print('\r\nInvalid input, please enter a number')

def show_options_menu():
    print('\r\nOptions menu:')
    print('1) Add new contact')
    print('2) Show contact list')
    print('3) Search contact')
    print('4) Update contact')
    print('5) Delete contact')
    print('0) Exit')

if __name__ ==  '__main__':
    main()

