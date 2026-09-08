def show_menu():
    print("""
    ===== Notes Manager =====

1. Add note
2. Show notes
3. Clear notes
4. Exit
    """)

def add_note():
    file_notes = open('notes.txt','a')
    file_notes.write(input('Enter new note: ') + '\n')
    file_notes.close()

def show_notes():
    file_notes = open('notes.txt','r')
    lines = file_notes.read()
    if not lines:
        print('There are no notes yet.')
    else:
        print(lines, end="")
    file_notes.close()

def clear_notes():
    file_notes = open('notes.txt','w')
    file_notes.close()

def main():
    while True:
        show_menu()
        user_choice = input("Select an item: ")
        match user_choice:
            case '1':
                add_note()
                print('Note added')
            case '2':
                show_notes()
            case '3':
                clear_notes()
                print('Notes deleted')
            case '4':
                print('Goodbye!')
                break
            case _:
                print('Invalid operation!')

main()