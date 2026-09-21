from unittest.mock import patch

# import the Layer 1 library program
import Layer1_library


def test_display_menu(capsys):
    '''
    test that the menu displays the correct options
    '''

    # call the menu function
    Layer1_library.display_menu()

    # capture the printed output
    captured = capsys.readouterr()

    # check that the menu title is displayed
    assert "Personal Library Manager" in captured.out

    # check that the add option is displayed
    assert "1. Add a title" in captured.out

    # check that the remove option is displayed
    assert "2. Remove a book" in captured.out

    # check that the list option is displayed
    assert "3. List all book titles" in captured.out

    # check that the search option is displayed
    assert "4. Search a book title" in captured.out

    # check that the exit option is displayed
    assert "5. Exit" in captured.out


def test_add_book():
    '''
    test that a book is added to the library
    '''

    # create an empty library
    library = []

    # simulate the user entering Dune
    with patch("builtins.input", return_value="Dune"):
        Layer1_library.add_book(library)

    # check that Dune was added
    assert "Dune" in library


def test_list_books_with_books(capsys):
    '''
    test that stored books are displayed
    '''

    # create a library with two books
    library = ["Dune", "1984"]

    # call the list function
    Layer1_library.list_books(library)

    # capture the printed output
    captured = capsys.readouterr()

    # check that both books are displayed
    assert "1. Dune" in captured.out
    assert "2. 1984" in captured.out


def test_list_books_empty(capsys):
    '''
    test what happens when the library is empty
    '''

    # create an empty library
    library = []

    # call the list function
    Layer1_library.list_books(library)

    # capture the printed output
    captured = capsys.readouterr()

    # check that the empty library message is displayed
    assert "Your library is empty" in captured.out


def test_remove_existing_book():
    '''
    test removing a book that exists
    '''

    # create a library that contains Dune
    library = ["Dune", "1984"]

    # simulate the user choosing Dune to remove
    with patch("builtins.input", return_value="Dune"):
        Layer1_library.remove_books(library)

    # check that Dune was removed
    assert "Dune" not in library


def test_remove_missing_book(capsys):
    '''
    test removing a book that does not exist
    '''

    # create a library that does not contain Dune
    library = ["1984"]

    # simulate the user trying to remove Dune
    with patch("builtins.input", return_value="Dune"):
        Layer1_library.remove_books(library)

    # capture the printed output
    captured = capsys.readouterr()

    # check that the correct message is displayed
    assert "Dune was not found in your library. Try again :(" in captured.out

    # check that the original library was not changed
    assert library == ["1984"]


def test_search_existing_book(capsys):
    '''
    test searching for a book that exists
    '''

    # create a library that contains Dune
    library = ["Dune", "1984"]

    # simulate the user searching for Dune
    with patch("builtins.input", return_value="Dune"):
        Layer1_library.search_book_title(library)

    # capture the printed output
    captured = capsys.readouterr()

    # check that the program confirms the book was found
    assert "we found the book Dune in your library" in captured.out


def test_search_missing_book(capsys):
    '''
    test searching for a book that does not exist
    '''

    # create a library that does not contain Dune
    library = ["1984"]

    # simulate the user searching for Dune
    with patch("builtins.input", return_value="Dune"):
        Layer1_library.search_book_title(library)

    # capture the printed output
    captured = capsys.readouterr()

    # check that the correct message is displayed
    assert "Dune was not found in your library" in captured.out