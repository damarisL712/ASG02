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


def add_book(library,titles):
    '''
    add a book title to the library 

    parameters: 
        Library: A list containing book titles

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
            #get the entire tuple for one book 
            book = library[index]
            # pull the title, author, and year from the book tuple
            print(f"{index + 1}. {book[0]} by {book[1]} ({book[2]})")

def remove_books(library,titles):
    '''
    removes any books that are in the library function if asked

    parameters: 
        Library: A list containing book titles 

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
        library: a list containing book title
    return:
        '''
    title = input("Enter a title to search: ")
    
    # loops through each book in the library
    for book in library: 

        # if the first value in the tuple matches what the user entered as title
        if book[0] == title:
            print(f"{book[0]} by {book[1]} ({book[2]}) was found")
            return

    print(f"{title} was not found in your library")


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
    while choice != "5":
        if choice == "1":
            add_book(library,titles)
        elif choice == "2":
            remove_books(library,titles)
        elif choice == "3":
            list_books(library)
        elif choice == "4":
            search_book_title(library)
        else:
            print("What you chose is not on the list")

        # display menu after completing an action
        display_menu()
        # ask the user to enter another option after the action was complete
        choice = input("Choose an option from the list:")
    print("You chose to exit. Cya!")

if __name__ == "__main__":
    main()