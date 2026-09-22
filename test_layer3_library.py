import json
import Layer3_library as layer3


def test_display_menu(capsys):
    # call the menu function
    layer3.display_menu()

    # capture what was printed
    captured = capsys.readouterr()

    # make sure the menu options were displayed
    assert "Personal Library Manager" in captured.out
    assert "1. Add a title" in captured.out
    assert "7. Exit" in captured.out


def test_add_new_book(monkeypatch, capsys):
    # create an empty library
    library = {}

    # simulate the user's inputs
    inputs = iter(["Dune", "Frank Herbert", "1965"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    # add the book
    layer3.add_or_update_book(library)

    # capture what was printed
    captured = capsys.readouterr()

    # make sure the book was stored correctly
    assert "Dune" in library
    assert library["Dune"]["author"] == "Frank Herbert"
    assert library["Dune"]["year"] == 1965
    assert '"Dune" was added' in captured.out


def test_update_existing_book(monkeypatch, capsys):
    # create a library containing Dune
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }

    # simulate updated information
    inputs = iter(["Dune", "Frank Herbert", "1966"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    # update the book
    layer3.add_or_update_book(library)

    # capture what was printed
    captured = capsys.readouterr()

    # make sure Dune was updated instead of duplicated
    assert len(library) == 1
    assert library["Dune"]["year"] == 1966
    assert '"Dune" was updated' in captured.out


def test_list_books_empty(capsys):
    # create an empty library
    library = {}

    # display the library
    layer3.list_books(library)

    # capture what was printed
    captured = capsys.readouterr()

    # make sure the empty message appears
    assert "Your library is empty" in captured.out


def test_list_books(capsys):
    # create a library with books out of alphabetical order
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

    # display the books
    layer3.list_books(library)

    # capture what was printed
    captured = capsys.readouterr()

    # make sure both books and their information appear
    assert "1984 by George Orwell (1949)" in captured.out
    assert "Dune by Frank Herbert (1965)" in captured.out


def test_remove_existing_book(monkeypatch, capsys):
    # create a library containing Dune
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }

    # simulate the title the user wants to remove
    monkeypatch.setattr("builtins.input", lambda prompt: "Dune")

    # remove the book
    layer3.remove_books(library)

    # capture what was printed
    captured = capsys.readouterr()

    # make sure Dune was removed
    assert "Dune" not in library
    assert "Dune was removed from your library" in captured.out


def test_remove_missing_book(monkeypatch, capsys):
    # create an empty library
    library = {}

    # simulate searching for a book that does not exist
    monkeypatch.setattr("builtins.input", lambda prompt: "Dune")

    # try to remove the book
    layer3.remove_books(library)

    # capture what was printed
    captured = capsys.readouterr()

    # make sure the program reports that the book was not found
    assert "Dune was not found in your library" in captured.out


def test_partial_case_insensitive_search(monkeypatch, capsys):
    # create a library containing Dune
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }

    # simulate a partial lowercase search
    monkeypatch.setattr("builtins.input", lambda prompt: "dun")

    # search the library
    layer3.search_book_title(library)

    # capture what was printed
    captured = capsys.readouterr()

    # make sure Dune was found
    assert "Dune by Frank Herbert (1965)" in captured.out


def test_search_no_results(monkeypatch, capsys):
    # create a library containing Dune
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }

    # simulate a search that does not match anything
    monkeypatch.setattr("builtins.input", lambda prompt: "xyz")

    # search the library
    layer3.search_book_title(library)

    # capture what was printed
    captured = capsys.readouterr()

    # make sure the no-results message appears
    assert "No matching books were found" in captured.out


def test_older_books(capsys):
    # create a library with one classic and one newer book
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        },
        "The Hunger Games": {
            "author": "Suzanne Collins",
            "year": 2008
        }
    }

    # display classic books
    layer3.older_books(library)

    # capture what was printed
    captured = capsys.readouterr()

    # make sure only the classic book appears
    assert "Dune by Frank Herbert (1965)" in captured.out
    assert "The Hunger Games" not in captured.out


def test_author_stats(capsys):
    # create multiple books by the same author
    library = {
        "1984": {
            "author": "George Orwell",
            "year": 1949
        },
        "Animal Farm": {
            "author": "George Orwell",
            "year": 1945
        },
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }

    # display author statistics
    layer3.author_stats(library)

    # capture what was printed
    captured = capsys.readouterr()

    # make sure the author counts are correct
    assert "George Orwell: 2" in captured.out
    assert "Frank Herbert: 1" in captured.out


def test_save_library(tmp_path, monkeypatch):
    # make pytest use a temporary folder
    monkeypatch.chdir(tmp_path)

    # create a library to save
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }

    # save the library
    layer3.save_library(library)

    # make sure the JSON file was created
    file_path = tmp_path / "library_data.json"
    assert file_path.exists()

    # open the saved JSON file
    with open(file_path, "r") as file:
        saved_data = json.load(file)

    # make sure the saved information is correct
    assert saved_data == library


def test_load_library(tmp_path, monkeypatch):
    # make pytest use a temporary folder
    monkeypatch.chdir(tmp_path)

    # create valid JSON data
    data = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }

    # create the JSON file
    with open("library_data.json", "w") as file:
        json.dump(data, file)

    # load the library
    library = layer3.load_library()

    # make sure the saved data was loaded
    assert library == data


def test_load_missing_file(tmp_path, monkeypatch):
    # make pytest use an empty temporary folder
    monkeypatch.chdir(tmp_path)

    # try to load when no JSON file exists
    library = layer3.load_library()

    # make sure an empty dictionary is returned
    assert library == {}


def test_load_corrupted_json(tmp_path, monkeypatch):
    # make pytest use a temporary folder
    monkeypatch.chdir(tmp_path)

    # create a corrupted JSON file
    with open("library_data.json", "w") as file:
        file.write("this is not valid json")

    # try to load the corrupted file
    library = layer3.load_library()

    # make sure the program uses an empty dictionary
    assert library == {}


def test_load_wrong_data_type(tmp_path, monkeypatch):
    # make pytest use a temporary folder
    monkeypatch.chdir(tmp_path)

    # save a list instead of a dictionary
    with open("library_data.json", "w") as file:
        json.dump(["Dune", "1984"], file)

    # load the file
    library = layer3.load_library()

    # make sure invalid data becomes an empty dictionary
    assert library == {}


def test_main_exit(monkeypatch, tmp_path, capsys):
    # make pytest use a temporary folder
    monkeypatch.chdir(tmp_path)

    # simulate choosing exit immediately
    monkeypatch.setattr("builtins.input", lambda prompt: "7")

    # run the program
    layer3.main()

    # capture what was printed
    captured = capsys.readouterr()

    # make sure startup and exit messages appear
    assert "Loaded 0 books from library_data.json" in captured.out
    assert "Library saved to library_data.json" in captured.out
    assert "You chose to exit. Cya!" in captured.out

    # make sure exiting created the JSON file
    assert (tmp_path / "library_data.json").exists()