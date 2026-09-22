# import the Layer 2 program so its functions can be tested
import Layer2_library


def test_display_menu(capsys):
    '''
    test that all menu options are displayed

    parameters:
        capsys: captures printed output from the function

    returns:
        none
    '''
    # call the function that displays the menu
    Layer2_library.display_menu()

    # capture everything that was printed
    captured = capsys.readouterr()

    # check that important menu options appear
    assert "Personal Library Manager" in captured.out
    assert "1. Add a title" in captured.out
    assert "5. Look at your classic books" in captured.out
    assert "6. Exit" in captured.out


def test_add_book(monkeypatch):
    '''
    test that a book tuple is added to the library

    parameters:
        monkeypatch: simulates user input

    returns:
        none
    '''
    # create an empty library
    library = []

    # create an empty set for unique titles
    titles = set()

    # create the inputs the user would enter
    user_inputs = iter(["Dune", "Frank Herbert", "1965"])

    # replace input with the test values
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(user_inputs)
    )

    # call the add book function
    Layer2_library.add_book(library, titles)

    # check that the complete book tuple was added
    assert ("Dune", "Frank Herbert", 1965) in library

    # check that the title was added to the set
    assert "Dune" in titles


def test_add_duplicate_book(monkeypatch, capsys):
    '''
    test that a duplicate book title cannot be added

    parameters:
        monkeypatch: simulates user input
        capsys: captures printed output

    returns:
        none
    '''
    # create a library that already contains Dune
    library = [("Dune", "Frank Herbert", 1965)]

    # create a set that already contains Dune
    titles = {"Dune"}

    # simulate the user entering Dune again
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: "Dune"
    )

    # try to add the duplicate title
    Layer2_library.add_book(library, titles)

    # capture the printed output
    captured = capsys.readouterr()

    # check that the duplicate message was displayed
    assert "Dune is already in your library" in captured.out

    # check that another Dune was not added
    assert len(library) == 1


def test_list_books_alphabetical(capsys):
    '''
    test that books are displayed in alphabetical order

    parameters:
        capsys: captures printed output

    returns:
        none
    '''
    # create a library in a non-alphabetical order
    library = [
        ("The Hobbit", "J.R.R. Tolkien", 1937),
        ("animal farm", "George Orwell", 1945),
        ("Dune", "Frank Herbert", 1965)
    ]

    # display all books
    Layer2_library.list_books(library)

    # capture the printed output
    captured = capsys.readouterr()

    # store the location of each title in the output
    animal_position = captured.out.find("animal farm")
    dune_position = captured.out.find("Dune")
    hobbit_position = captured.out.find("The Hobbit")

    # check that the titles appear in alphabetical order
    assert animal_position < dune_position < hobbit_position


def test_list_books_empty(capsys):
    '''
    test listing books when the library is empty

    parameters:
        capsys: captures printed output

    returns:
        none
    '''
    # create an empty library
    library = []

    # try to display the books
    Layer2_library.list_books(library)

    # capture the printed output
    captured = capsys.readouterr()

    # check that the empty library message appears
    assert "Your library is empty" in captured.out


def test_remove_existing_book(monkeypatch):
    '''
    test removing a book from both the library and title set

    parameters:
        monkeypatch: simulates user input

    returns:
        none
    '''
    # create a library containing Dune
    library = [
        ("Dune", "Frank Herbert", 1965),
        ("1984", "George Orwell", 1949)
    ]

    # create the matching set of book titles
    titles = {"Dune", "1984"}

    # simulate the user choosing Dune
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: "Dune"
    )

    # remove Dune
    Layer2_library.remove_books(library, titles)

    # check that the complete Dune tuple was removed
    assert ("Dune", "Frank Herbert", 1965) not in library

    # check that Dune was also removed from the title set
    assert "Dune" not in titles


def test_remove_missing_book(monkeypatch, capsys):
    '''
    test removing a title that is not in the library

    parameters:
        monkeypatch: simulates user input
        capsys: captures printed output

    returns:
        none
    '''
    # create a library without Dune
    library = [("1984", "George Orwell", 1949)]

    # create the matching title set
    titles = {"1984"}

    # simulate the user trying to remove Dune
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: "Dune"
    )

    # try to remove Dune
    Layer2_library.remove_books(library, titles)

    # capture the printed output
    captured = capsys.readouterr()

    # check that the missing title message appears
    assert "Dune was not found in your library" in captured.out

    # check that the original book was not removed
    assert len(library) == 1

    # check that the title set was not changed
    assert titles == {"1984"}


def test_search_existing_book(monkeypatch, capsys):
    '''
    test searching for a book that exists

    parameters:
        monkeypatch: simulates user input
        capsys: captures printed output

    returns:
        none
    '''
    # create a library containing Dune
    library = [
        ("Dune", "Frank Herbert", 1965),
        ("1984", "George Orwell", 1949)
    ]

    # simulate the user searching for Dune
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: "Dune"
    )

    # search the library
    Layer2_library.search_book_title(library)

    # capture the printed output
    captured = capsys.readouterr()

    # check that the matching book information appears
    assert "Dune by Frank Herbert (1965) was found" in captured.out


def test_search_missing_book(monkeypatch, capsys):
    '''
    test searching for a book that does not exist

    parameters:
        monkeypatch: simulates user input
        capsys: captures printed output

    returns:
        none
    '''
    # create a library without Harry Potter
    library = [("Dune", "Frank Herbert", 1965)]

    # simulate the user searching for Harry Potter
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: "Harry Potter"
    )

    # search the library
    Layer2_library.search_book_title(library)

    # capture the printed output
    captured = capsys.readouterr()

    # check that the missing title message appears
    assert "Harry Potter was not found in your library" in captured.out


def test_older_books_found(capsys):
    '''
    test that books published before 2000 are displayed

    parameters:
        capsys: captures printed output

    returns:
        none
    '''
    # create a library with classic and newer books
    library = [
        ("Dune", "Frank Herbert", 1965),
        ("The Hunger Games", "Suzanne Collins", 2008),
        ("1984", "George Orwell", 1949)
    ]

    # display the classic books
    Layer2_library.older_books(library)

    # capture the printed output
    captured = capsys.readouterr()

    # check that books before 2000 appear
    assert "Dune by Frank Herbert (1965)" in captured.out
    assert "1984 by George Orwell (1949)" in captured.out

    # check that the newer book does not appear
    assert "The Hunger Games" not in captured.out


def test_older_books_none_found(capsys):
    '''
    test a library that contains no books published before 2000

    parameters:
        capsys: captures printed output

    returns:
        none
    '''
    # create a library containing only newer books
    library = [
        ("The Hunger Games", "Suzanne Collins", 2008),
        ("The Silent Patient", "Alex Michaelides", 2019)
    ]

    # search for classic books
    Layer2_library.older_books(library)

    # capture the printed output
    captured = capsys.readouterr()

    # check that the no classic books message appears
    assert "You do not have any classic books stored" in captured.out


def test_older_books_empty_library(capsys):
    '''
    test the classic book option with an empty library

    parameters:
        capsys: captures printed output

    returns:
        none
    '''
    # create an empty library
    library = []

    # try to display classic books
    Layer2_library.older_books(library)

    # capture the printed output
    captured = capsys.readouterr()

    # check that the empty library message appears
    assert "Your library is empty" in captured.out


def test_main_exit(monkeypatch, capsys):
    '''
    test that the main program exits when option 6 is selected

    parameters:
        monkeypatch: simulates user input
        capsys: captures printed output

    returns:
        none
    '''
    # simulate the user immediately choosing option 6
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: "6"
    )

    # run the main function
    Layer2_library.main()

    # capture the printed output
    captured = capsys.readouterr()

    # check that the exit message appears
    assert "You chose to exit. Cya!" in captured.out