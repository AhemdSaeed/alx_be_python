from library_system import Book, EBook, PrintBook, Library
from polymorphism_demo import Shape, Rectangle, Circle
from class_static_methods_demo import Calculator


def test_library_system():
    print("=== Library System Demo ===")
    my_library = Library()

    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()
    print()  # سطر فاصل


def test_polymorphism_demo():
    print("=== Polymorphism Demo ===")
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
    print()  # سطر فاصل


def test_calculator_demo():
    print("=== Class & Static Methods Demo ===")
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
    print()  # سطر فاصل


if __name__ == "__main__":
    test_library_system()
    test_polymorphism_demo()
    test_calculator_demo()
