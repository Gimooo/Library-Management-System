def list_borrowed_books(books):
    borrowed_books = [book for book in books if book.get('borrowed', False)]

    if not borrowed_books:
        print("No books are currently borrowed.")
        return

    print(f"{'ID':<5} {'Title':<30} {'Borrower':<20}")
    print("-" * 60)
    for book in borrowed_books:
        print(f"{book['id']:<5} {book['title']:<30} {book.get('borrower', 'Unknown'):<20}")
