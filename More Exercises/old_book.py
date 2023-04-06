searched_book = input()
searched_books_count = 0

while True:
    current_book = input()

    if current_book == searched_book:
        print(f'You checked {searched_books_count} books and found it.')
        break

    if current_book == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {searched_books_count} books.')
        break

    searched_books_count += 1