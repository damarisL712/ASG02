"""
Layer 2: Personal Library Manager - Tuples, Sets, Sorting, and Comprehensions
============================================================================

Purpose
-------
This is the SECOND layer of the Personal Library Manager project.
The goal of this layer is to improve the program by storing more
information about each book and introducing additional Python data
structures.

Each book now stores a title, author, and publication year inside
a tuple. A set is used to keep track of unique book titles and help
prevent duplicates. The program also sorts books alphabetically and
uses a list comprehension to analyze the library by identifying books
published before the year 2000.

Data Model
----------
The library is represented as a list of tuples:

    library = [
        ("Dune", "Frank Herbert", 1965),
        ("1984", "George Orwell", 1949)
    ]

A separate set stores the book titles:

    titles = {"Dune", "1984"}

Layer 2 Features
----------------
- Stores title, author, and publication year for each book.
- Uses tuples to group information about each book.
- Uses a set to prevent duplicate book titles.
- Displays books in alphabetical order by title.
- Allows books to be added, removed, listed, and searched.
- Uses a list comprehension to identify classic books published
  before the year 2000.

Limitations
-----------
- The library is still stored as a list, so some operations require
  searching through the list one book at a time.
- The library data is not saved after the program closes.
- Updating an existing book is not yet supported.

These limitations help motivate Layer 3, where the program will use
a dictionary-based design and file storage.
"""


def display_menu():
    '''
    display all the library options to the user

    parameters: 
        none

    returns:
        none
    '''
    print("\n==== Personal Library Manager ====")
    print(" Please select an option:")
    print("1. Add a title")
    print("2. Remove a book")
    print("3. List all book titles")
    print("4. Search a book title")
    print("5. Look at your classic books")
    print("6. Exit")


def add_book(library,titles):
    '''
    add a book title to the library 

    parameters: 
        Library: A list containing book tuples

        titles: a set containing different book title names

    returns:
        none 
    '''
    title = input("Enter a book title: ")

    if title in titles:
        print(f"{title} is already in your library. Try again")
    else:
        author = input("Enter the book author: ")

        year = int(input("Enter the publication year: "))

        # creates a tutple that containig all information on the book
        book = (title,author,year)    

        # add users input on book to the library list
        library.append(book)

        # take what the user entered for title and add it to the titles set
        titles.add(title)

        # print that the title, author, and year was added to the library
        print(f"\"{title}\" was added to your library")


def list_books(library):
    '''
    Displays all books that are in the library 

    parameters: 
        Library: A list containing book tuple
    
    returns: 
        none 
    '''
    if len(library) == 0:
        # make this print statement is the there is nothing in the library
        print("Your library is empty")
    else:
        print("\n==== Your Library ====")

        # sort the book titles in the library by alphabetical order
        sorted_library = sorted(library,key=lambda book: book[0].lower())
        for index in range(len(sorted_library)):
            #get the entire tuple for one book 
            book = sorted_library[index]
            # pull the title, author, and year from the book tuple
            print(f"{index + 1}. {book[0]} by {book[1]} ({book[2]})")

def remove_books(library,titles):
    '''
    removes any books that are in the library function if asked

    parameters: 
        Library: A list containing book tuple 

    returns:
        none
    '''
    title = input("Enter the book title you want to remove: ")

    # looop through each book in the library
    for book in library:
        # checks if the first value in the tuple matches the title
        if book[0] == title:
            library.remove(book)
            # remove title from the set
            titles.remove(title)
            print(f"{title} was removed from your library")
            # stop the function after the book that matches is removed
            return
    print(f"{title} was not found in your library. Try again :(")


def search_book_title(library):
    '''
    search for a book title in the library

    parameters:
        library: a list containing book tuple
    return:
        none
        '''
    title = input("Enter a title to search: ")
    
    # loops through each book in the library
    for book in library: 

        # if the first value in the tuple matches what the user entered as title
        if book[0] == title:
            print(f"{book[0]} by {book[1]} ({book[2]}) was found")
            return

    print(f"{title} was not found in your library")

def older_books(library):
    '''
    show books published anytime before the year 2000
    
    parameters:
        library: a list containing books
    
    returns:
        none
    '''

    if len(library) == 0:
        print("Your library is empty. Add some books and try again")
    else:
        # creates a list of book published before year 2000
        classic_books = [book for book in library if book[2]<2000]

        # are there no classic books?
        if len(classic_books) == 0:
            print("You do not have any classic books stored")
        else:
            print("\n==== Classic Books In Your Library ====")

            # display each book before year 2000
            for book in classic_books:
                print(f"{book[0]} by {book[1]} ({book[2]})")


def main():
    '''
    runs the personal library manager

    parameters:
        none
    returns: 
        none
    '''
    library = []

    # create a set to prevent duplicate book titles
    titles = set()

    display_menu()
    choice = input("Choose an option from the list:")
    while choice != "6":
        if choice == "1":
            add_book(library,titles)
        elif choice == "2":
            remove_books(library,titles)
        elif choice == "3":
            list_books(library)
        elif choice == "4":
            search_book_title(library)
        elif choice == "5":
            older_books(library)
        else:
            print("What you chose is not on the list")

        # display menu after completing an action
        display_menu()
        # ask the user to enter another option after the action was complete
        choice = input("Choose an option from the list:")
    print("You chose to exit. Cya!")

if __name__ == "__main__":
    main()