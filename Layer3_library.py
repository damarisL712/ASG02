"""
Layer 3: Personal Library Manager - Dictionaries and File Persistence
=====================================================================

Purpose
-------
This is the FINAL layer of the Personal Library Manager project.
The goal of this layer is to improve the program by replacing the
list-and-tuple design with a dictionary-based structure.

Each book title is stored as a unique dictionary key. The value for
each title is another dictionary containing the author and publication
year. This makes it easier to search for, update, and remove books.

The program will also add author statistics and save the library to a
JSON file so the user's data can be loaded again when the program
starts.

Data Model
----------
The library is represented as a nested dictionary:

    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        },
        "1984": {
            "author": "George Orwell",
            "year": 1949
        }
    }

The book title is used as the dictionary key, so a separate title set
is no longer needed.

Layer 3 Features
----------------
- Uses a dictionary to store books by title.
- Stores author and publication year in a nested dictionary.
- Adds new books or updates existing books with the same title.
- Removes books by title.
- Displays all books in a readable format.
- Supports partial and case-insensitive title searches.
- Calculates how many books each author has in the library.
- Saves library data to a JSON file.
- Loads saved library data when the program starts.
- Handles missing or invalid data files without crashing.

Design Improvements
-------------------
- Dictionary keys make title lookups more direct than searching
  through a list.
- Existing books can be updated without creating duplicate titles.
- The nested dictionary structure makes it easier to add more book
  attributes later.
- JSON file storage allows library data to persist between program
  runs.
"""
import json

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
    print("6. Show author statistics")
    print("7. Exit")


def add_or_update_book(library):
    '''
    add a new book or update an exisitng one in the library

    parameters: 
        Library: a dictionary containing book info


    returns:
        none 
    '''
    title = input("Enter a book title: ")

    # if the book title is already in the dictionary
    if title in library:
        # state that the book was updated
        action = "Updated"
    else:
        # state that the book was added
        action = "added"

    author = input("Enter the book author: ")
    year = int(input("Enter the publication year: "))

    # store the author and year under the book title in the dictionary
    library[title] = {
        "author": author,
        "year": year
    }
        
    # print that the title, author, and year was added to the library
    print(f"\"{title}\" was {action}")


def list_books(library):
    '''
    Displays all books that are in the library 

    parameters: 
        Library: a dictionary containing book info
    
    returns: 
        none 
    '''
    # if library is empty
    if len(library) == 0:
        # tell user library is empty
        print("Your library is empty")
    else:
        print("\n==== Your Library ====")

        # sort the book titles in the library by alphabetical order
        sorted_titles = sorted(library,key=lambda title: title.lower())

        for index in range(len(sorted_titles)):
            # get the book title at its positon
            title = sorted_titles[index]

            #get the author and year from the current title
            author = library[title]["author"]
            year = library[title]['year']

            # pull the title, author, and year from the book tuple
            print(f"{index + 1}. {title} by {author} ({year})")

def remove_books(library):
    '''
    removes any books that are in the library function if asked

    parameters: 
        Library: a dictionary containing book information

    returns:
        none
    '''
    title = input("Enter the book title you want to remove: ")

    if title in library: 
        # remove the book using its its title
        library.pop(title)
        print(f"{title} was removed from your library")
    else:
        print(f"{title} was not found in your library")

def search_book_title(library):
    '''
    search for a book title in the library

    parameters:
        library: a dictionary containing book info
    return:
        none
        '''
    book_title = input("Enter a title to search: ")

    # create a list to store matching book titles
    similar_titles = []

    for title in library:
        # check if the searched text appears in the title without case sensitivity
        if book_title.lower() in title.lower():
            # add the matching title to the list
            similar_titles.append(title)

    if len(similar_titles) == 0:
        print("No matching books were found")
    else: 
        print("\n==== Search Results ====")

        # show each matching book 
        for index in range(len(similar_titles)):
            title = similar_titles[index]

            # get the author and year from the current title
            author = library[title]["author"]
            year = library[title]["year"]

            # display matching book information 
            print(f"{index + 1}. {title} by {author} ({year})")


def older_books(library):
    '''
    show books published anytime before the year 2000
    
    parameters:
        library: a dictionary containing book infromation
    
    returns:
        none
    '''

    if len(library) == 0:
        print("Your library is empty. Add some books and try again")
    else:
        # creates a list of books published before year 2000
        classic_books = [title for title in library if library[title]["year"]<2000]

        # are there no classic books?
        if len(classic_books) == 0:
            print("You do not have any classic books stored")
        else:
            print("\n==== Classic Books In Your Library ====")

            # display each classic book 
            for title in classic_books:
                # get the author and year from the current title
                author = library[title]["author"]
                year = library[title]["year"]

                # display matching book information 
                print(f"{title} by {author} ({year})")

def author_stats(library):
    '''
    will display the number of books written by each author
    
    paramters:
        library: a dictionary containing book information
    
    returns:
        none
    '''
    if len(library) == 0:
        print("your library is empty")
    else:
        # create a dictionary to store the number of books for each author
        author_counts = {}

        # loop through each book title
        for title in library: 
            # get the author from the current book
            author = library [title]["author"]

            # check if th author already has a counter going
            if author in author_counts:
                # increase the author's book count
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        print("\n==== Books per author ====")

        # display each author and their number of books
        for author in author_counts:
            # display the author and the number of books they have in the library
            print(f"{author}: {author_counts[author]}")

def save_library(library):
    '''
    save the library dictionary to a json file

    parameters:
        library: a dictionary containing book information
    
    returns
        none
    '''
    # open the file for writing
    with open("library_data.json", "w") as file:
        # take the library dictionary and write it into the file
        json.dump(library,file,indent = 2)
    
    # confirmation message
    print("Library saved to library_data.json")

def load_library():
    '''
    load the library data from the json file

    paramters:
        none
    returns:
        the library dictionar
    '''
    try:
        # open tthe json file for reading
        with open("library_data.json", "r") as file:
            # load the saved json daata into python
            library = json.load(file)

    except (json.JSONDecodeError, OSError):
        # use empty dictionary if the file cannot be loaded
        library = {}

    return library

def main():
    '''
    runs the personal library manager

    parameters:
        none
    returns: 
        none
    '''
    # creates an empty dicitonary for book info
    library = load_library()

    # create a set to prevent duplicate book titles
    titles = set()

    display_menu()
    choice = input("Choose an option from the list:")
    while choice != "7":
        if choice == "1":
            add_or_update_book(library)
        elif choice == "2":
            remove_books(library)
        elif choice == "3":
            list_books(library)
        elif choice == "4":
            search_book_title(library)
        elif choice == "5":
            older_books(library)
        elif choice == "6":
            author_stats(library)
        else:
            print("What you chose is not on the list")

        # display menu after completing an action
        display_menu()

        # ask the user to enter another option after the action was complete
        choice = input("Choose an option from the list:")
    # save the data in the library before the program stops
    save_library(library)
    print("You chose to exit. Cya!")

if __name__ == "__main__":
    main()