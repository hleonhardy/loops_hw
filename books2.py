#This program will show brighticorn's library.

#functions used:

def add_book(books):
    """Adds a new book and returns new title"""

    book = raw_input("Title: ")
    book = book.title()
    books.append(book)

    return book


def view_books(books):
    """views books"""

    for book in books:
        print book


def check_book(books):
    """checks books, returns title if found or None if not found"""

    book_to_check = raw_input("Please enter the book title you would like to check for: ")
    book_to_check = book_to_check.title()

    if book_to_check in books:
        return book_to_check
    
    else:
        return None


def get_command():
    """shows commands, returns the action"""
    print
    print "You can add/view/check/exit."
    command = raw_input("Action: ")
    command = command.lower()

    return command


def library():
    """main loop"""

    books = ["Thinner", "Cat's Cradle", "Candide"]

    print
    print "Brighticorn's Books"
    print "-------------------"
    print 

    use_library = True

    while use_library:

        command = get_command()

        if command == "add":
            book = add_book(books)
            print "Added: {}".format(book)
            

        elif command == "view":
            print "Here are your books: "
            print
            view_books(books)
            print 
            print "End of listing."
            

        elif command == "check":
            found = check_book(books)
            print "Found: {}".format(found)

        elif command == "exit":
            use_library = False

        else:
            print "I'm sorry, that's not an option." 



#running the code:

library()


