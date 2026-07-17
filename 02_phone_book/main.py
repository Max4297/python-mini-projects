def show_menu():
    print("""
    ===== Phone Book =====

1. Add contact
2. Find contact
3. Show all contacts
4. Delete contact
5. Update contact
6. Exit
    """)

def add_contact(phone_book):
    new_contact = input('Enter name: ')
    if new_contact in phone_book:
        print('This contact already exists.')
    else:
        new_number = input('Enter number: ')
        phone_book[new_contact] = new_number
        print(f'New contact {new_contact} added!')

def find_contact(phone_book):
    name_contact = input("Enter name: ")
    if name_contact in phone_book:
        print(f'Contact name: {name_contact}')
        print(f'Contact number: {phone_book[name_contact]}')
    else:
        print('Contact not found')

def show_contacts(phone_book):
    for name, number in phone_book.items():
        print(f'{name}: {number}')
        
def delete_contact(phone_book):
    name_contact = input('Enter name: ')

    if name_contact in phone_book:
        del phone_book[name_contact]
        print(f'Contact {name_contact} deleted!')
    else:
        print('Contact not found!')

def update_contact(phone_book):
    name_contact = input('Enter name: ')
    if name_contact in phone_book:
        print(f'Old number: {phone_book[name_contact]}')
        phone_book[name_contact] = input('Enter new number: ')
        print(f'Contact {name_contact} updated!')
    else:
        print('Contact not found.')

def main():
    phone_book = {
        'Den': '+38324324'
    }
    
    while True:
        show_menu()
        user_choice = input("Select an item: ")
        match user_choice:
            case '1':
                add_contact(phone_book)
            case '2':
                find_contact(phone_book)
            case '3':
                if phone_book:
                    show_contacts(phone_book)
                else:
                    print('Phone book is empty!')
            case '4':
                delete_contact(phone_book)
            case '5':
                update_contact(phone_book)
            case '6':
                print('Goodbye!')
                break
            case _:
                print('Invalid operation!')

main()