import json

DB_FILE = "library.json"

def search_book():
    with open(DB_FILE, "r") as file:
        books = json.load(file)

    keyword = input("Enter title or author to search: ").lower()
    found = False
    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")
            found = True

    if not found:
        print("No matching books found.")
