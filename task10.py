import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("=" * 50)
        print("📚 Welcome to the Library Management System 📚".center(50))
        print("=" * 50)
        print("Please choose an option:")
        print()
        print("1. View All Books")
        print("2. List Borrowed Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Add New Book")
        print("6. Remove Book")
        print("7. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            view_all_books()
        elif choice == '2':
            list_borrowed_books()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            add_book()
        elif choice == '6':
            remove_book()
        elif choice == '7':
            print("\nThank you for using the Library System. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number from 1 to 7.")
            input("Press Enter to continue...")

