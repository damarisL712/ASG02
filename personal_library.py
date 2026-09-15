"""
Layer 1: Personal Library Manager - List of Titles
=====================================================
Purpose
-------
This is the FIRST layer of the Personal Library Manager project.
The goal here is not efficiency or good design -- it is to practice
basic Python control flow (loops, conditionals) and basic list
operations before introducing more advanced data structures.

Data Model
----------
The entire library is represented as a single list of strings:

    library = ["Dune", "1984", "The Hobbit"]

Limitations (intentional, to motivate Layer 2)
-----------------------------------------------
- Only the title is stored; there is no place for author or year.
- Checking for a duplicate title requires an O(n) linear scan.
- There is no structure for "author" statistics at all.

These limitations are exactly why the project moves on to Layer 2.
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
    print("1. Please select an option:")
    print("2. Add a title")
    print("3. Remove a book")
    print("4. List all book titles")
    print("5. Search a book title")
    print("6. Exit")

def add_book(library):
    '''
    add a book title to the library 

    parameters: 
        Library: A list containing book titles

    Returns:
        none 
    '''
    title = input("Enter a book title: ")

    # add users input on book to the library list
    library.append(title)

    # print that the title was added to the library
    print(f"{title} was added to your library")

def list_books(library):
    '''
    Displays all books that are in the library 

    parameters: 
        Library: A list containing book titles
        
    '''
    if len(library) == 0:
        # make this print statement is the there is nothing in the library
        print("Your library is empty")
    else:
        for index in range(len(library)):
            # print the book number, then print the book title at the position
            print(f"{index +1}. {library[index]}")

def main():
    library = []
    display_menu()
    add_book(library)
    list_books(library)

if __name__ == "__main__":
    main()