def search_book(book):
    count = 0

    while True:
        name = input()
        count += 1

        if name == "No More Books":
            print("The book you search is not here!")
            print(f"You checked {count - 1} books.")
            break

        if name == book:
            print(f"You checked {count - 1} books and found it.")
            break


book_to_search = input()
search_book(book_to_search)
