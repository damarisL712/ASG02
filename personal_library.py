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
    print(" Please select an option:")
    print("1. Add a title")
    print("2. Remove a book")
    print("3. List all book titles")
    print("4. Search a book title")
    print("5. Exit")

def add_book(library):
    '''
    add a book title to the library 

    parameters: 
        Library: A list containing book titles

    returns:
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
    
    returns: 
        none 
    '''
    if len(library) == 0:
        # make this print statement is the there is nothing in the library
        print("Your library is empty")
    else:
        print("\n==== Your Library ====")
        for index in range(len(library)):
            # print the book number, then print the book title at the position
            print(f"{index + 1 }. {library[index]}")

def remove_books(library):
    '''
    removes any books that are in the library function if asked

    parameters: 
        Library: A list containing book titles 

    returns:
    '''
    title = input("Enter the book title you want to remove: ")

    if title in library:
        library.remove(title)
        print(f"{title} was remove from your library")
    else:
        print(f"{title} was not found in your library. Try again :(")

def main():
    library = []
    display_menu()
    choice = input("Choose an option from the list:")
    if choice == "1":
        add_book(library)
    elif choice == "2":
        lists_books(library)
    elif choice == "3":
        remove_books(library)

if __name__ == "__main__":
    main()