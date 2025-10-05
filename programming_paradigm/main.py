# import sys
# from robust_division_calculator import safe_divide
# from library_management import Book, Library

# def main():
#     if len(sys.argv) != 3:
#         print("Usage: python main.py <numerator> <denominator>")
#         sys.exit(1)

#     numerator = sys.argv[1]
#     denominator = sys.argv[2]

#     result = safe_divide(numerator, denominator)
#     print(result)

# if __name__ == "__main__":
#     main()


# def main():
#     # Setup a small library
#     library = Library()
#     library.add_book(Book("Brave New World", "Aldous Huxley"))
#     library.add_book(Book("1984", "George Orwell"))

#     # Initial list of available books
#     print("Available books after setup:")
#     library.list_available_books()

#     # Simulate checking out a book
#     library.check_out_book("1984")
#     print("\nAvailable books after checking out '1984':")
#     library.list_available_books()

#     # Simulate returning a book
#     library.return_book("1984")
#     print("\nAvailable books after returning '1984':")
#     library.list_available_books()

# if __name__ == "__main__":
#     main()


import sys
from robust_division_calculator import safe_divide
from library_management import Book, Library

def run_calculator(numerator, denominator):
    result = safe_divide(numerator, denominator)
    print(result)

def run_library_demo():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py calc <numerator> <denominator>")
        print("  python main.py library")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "calc":
        if len(sys.argv) != 4:
            print("Usage: python main.py calc <numerator> <denominator>")
            sys.exit(1)
        numerator = sys.argv[2]
        denominator = sys.argv[3]
        run_calculator(numerator, denominator)

    elif mode == "library":
        run_library_demo()

    else:
        print(f"Unknown mode: {mode}")
        print("Use 'calc' or 'library'.")

if __name__ == "__main__":
    main()

