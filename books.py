#This program will show brighticorn's library.

print
print "Brighticorn's Books"
print "-------------------"
print 


books = ["Thinner", "Cat's Cradle", "Candide"]


use_library = True

while use_library:

    print "You can add/view/check/exit."
    command = raw_input("Action: ")
    command = command.lower()
    #print "Action: {}".format(command)
    print


    if command == "add":
        new_book = raw_input("Please enter the title of the book you would like to add: ")
        new_book = new_book.title()
        books.append(new_book)
        
        print "Added: {}".format(new_book)


    elif command == "view":
        print "Here are your books: "
        print
        
        for book in books:
            print book
        
        print
        print "End of listing."


    elif command == "check":
        check_book = raw_input("Please enter the book title you would like to check for: ")
        check_book = check_book.title()
        
        found = False

        for book in books:
            if check_book in book:
                print "Found: {}".format(book)
                found = True

        if found == False:
            print "I'm sorry, we could not find any titles matching '{}.'".format(check_book) 



    elif command == "exit":
        print "Goodbye!"

        use_library = False


    else:
        print "Sorry, that's not an option."



