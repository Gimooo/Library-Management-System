def view_all_books(books):
    if not books:
        print("No books available.")
        return

    print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Year':<6}")
    print("-" * 65)
    for book in books:
        print(f"{book['id']:<5} {book['title']:<30} {book['author']:<20} {book['year']:<6}")
