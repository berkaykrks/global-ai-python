class Library:
    def __init__(self):
        self.filename = "books.txt"
        self.file = open(self.filename, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  # Move cursor to the beginning of the file
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(',')
            print("Title:", book_info[0])
            print("Author:", book_info[1])
            print("Release Date:", book_info[2])
            print("Number of Pages:", book_info[3])
            print()

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        release_date = input("Enter the release date: ")
        pages = input("Enter the number of pages: ")
        book_info = f"{title},{author},{release_date},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        for book in books:
            if title not in book:
                updated_books.append(book)
        self.file.seek(0)
        self.file.truncate()  # Clear the file contents
        for book in updated_books:
            self.file.write(book)
        print("Book removed successfully.")


def main():
    lib = Library()

    while True:
        print("*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        else:
            print("Invalid choice. Please enter a valid option.")

        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
