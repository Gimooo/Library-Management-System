import json

DB_FILE = "library.json"

def remove_book():
    with open(DB_FILE, "r") as file:
        books = json.load(file)

    try:
        book_id = int(input("Enter the ID of the book to remove: "))
    except ValueError:
        print("Invalid input. Please enter a valid book ID.")
        return

    updated_books = [book for book in books if book["id"] != book_id]

    if len(updated_books) == len(books):
        print("Book not found.")
    else:
        with open(DB_FILE, "w") as file:
            json.dump(updated_books, file, indent=4)
        print("Book removed successfully.")
