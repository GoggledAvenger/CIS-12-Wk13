#https://thartmanoftheredwoods.github.io/CIS-12/week_13pyCh14.html
# Chapter 14 - Classes and Functions

class Book:
    """Represents a book in a library."""

def display_book(book):
    print(f"{book.title} by {book.author}, published in {book.year}.")

my_book1 = Book()
my_book1.title = "The Great Gatsby"
my_book1.author = "F. Scott Fitzgerald"
my_book1.year = 1925

my_book2 = Book()
my_book2.title = "1984"
my_book2.author = "George Orwell"
my_book2.year = 1949

def create_book(title, author, year):
    book = Book()  # Creating an instance of Book (i.e. an object)
    book.title = title  # Setting the title instance variable / attribute
    book.author = author
    book.year = year
    return book

new_book = create_book("To Kill a Mockingbird", "Harper Lee", 1960)  # Returned the address of the object to new_book, so new_book now points at the object.
#display_book(new_book)

#mutable

def update_year(book, new_year):
    book.year = new_year

update_year(new_book, 1961)
#display_book(new_book)  # Year is now updated to 1961

#pure function (immutable)

from copy import copy

book_copy = copy(new_book)
update_year(book_copy, 2020)
#display_book(new_book)   # Original book remains unchanged
#display_book(book_copy)  # Copy has the updated year

#https://thartmanoftheredwoods.github.io/CIS-12/week_13pyCh15.html
# Chapter 15 - Classes and Methods

class Dog:

    def __init__(self, name, age):  # This is a special method that assigns values to attributes, kinda like a C# or Java constructor.
        self.name = name
        self.age = age

my_dog1 = Dog("Buddy", 5)  # Code outside the class to create an instance of class Dog (i.e. my_dog points at an object)
#print(my_dog1.name)  # Output: Buddy
#print(my_dog1.age)   # Output: 5

def bark(d1):
    d1.bark()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", 5)
my_dog.bark()  # Calling the method with an object, my_dog gets passed as self
bark(my_dog)   # Calling a function
