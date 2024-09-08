from classes.contact_list import ContactList

def main():
    # Instance of the ContactList class
    contact_list = ContactList()
    
    show_menu()
    
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
            elif option == 2:
                print('\r\nContact list:')
                contact_list.show_contacts()
            elif option == 3:
                print('Edit contact...')
                question = True
            elif option == 4:
                print('Searching...')
                question = False
            elif option == 5:
                print('Delete contact...')
                question = False
            elif option == 0:
                print('\r\nClosing the program...')
                break
            else:
                print('\r\nInvalid option, please try again')
        except ValueError:
            print('\r\nInvalid input, please enter a number')

def show_menu():
    print('Options menu:')
    print('1) Add new contact')
    print('2) Show contact list')
    print('3) Edit contact')
    print('4) Search contact')
    print('5) Delete contact')
    print('0) Exit')

if __name__ ==  '__main__':
    main()

