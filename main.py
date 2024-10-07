from library import Library
from book import Book

def menu():
    library = Library()
    while True:
        print("\n1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Save the library to a file")
        print("6. Load the library from a file")
        print("7. Quit")
        choice = input("Your choice: ")

        try:
            if choice == '1':
                isbn = input("ISBN: ")
                title = input("Title: ")
                author = input("Author: ")
                year = int(input("Year: "))
                book = Book(isbn, title, author, year)
                library.add_book(book)
                print("Book added successfully!")

            elif choice == '2':
                isbn = input("ISBN to remove: ")
                if library.remove_book(isbn):
                    print("Book removed successfully!")
                else:
                    print("Book not found!")

            elif choice == '3':
                search_type = input("Search by ISBN (1), Title (2), or Author (3): ")
                if search_type == '1':
                    isbn = input("ISBN: ")
                    result = library.search_book('isbn', isbn)
                elif search_type == '2':
                    title = input("Title: ")
                    result = library.search_book('title', title)
                elif search_type == '3':
                    author = input("Author: ")
                    result = library.search_book('author', author)
                else:
                    raise ValueError("Invalid search type")

                if result:
                    print(result.book)
                else:
                    print("Book not found.")

            elif choice == '4':
                sort_by = input("Sort by title (1) or year (2): ")
                if sort_by == '1':
                    library.display_books(sort_by='title')
                elif sort_by == '2':
                    library.display_books(sort_by='year')
                else:
                    raise ValueError("Invalid sort option")

            elif choice == '5':
                file_name = input("Enter file name to save: ")
                library.save(file_name)
                print("Library saved successfully!")

            elif choice == '6':
                file_name = input("Enter file name to load: ")
                library.load(file_name)
                print("Library loaded successfully!")

            elif choice == '7':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
        except ValueError as ve:
            print(f"Input error: {ve}")
        except FileNotFoundError:
            print("Error: File not found. Please provide a valid file.")
        except IOError:
            print("File operation error. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    menu()

