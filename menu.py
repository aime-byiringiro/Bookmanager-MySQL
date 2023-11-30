import sys
import book_dao
from mysql_connector import connection

menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'delete a book',
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
    # To be added
}


# Function to search for all books in the database
def search_all_books():
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = book_dao.findAll()

    # Displaying the results
    print("The following are the ISBNs and titles of all books.")
    for item in results:
        print(item[0], item[1])
    print("The end of books.")

# Function to search for books by title


def search_by_title(title):
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = book_dao.findByTitle(title)

    # Displaying the results for books with the given title
    print("Search by Title:")
    # Format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    s_format = "%-10s %-1s %-50s"
    print(s_format % ("ISBN:", "|", "Title:"))

    # Prints book entries with the given title (0 or more results)
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item[0], "|", item[1]))
    print("---End of Search Results---")

# Function to search for books by ISBN


def search_by_ISBN(ISBN_num):
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = book_dao.findByISBN(ISBN_num)

    # Displaying the results for books with the given ISBN
    print("Search by ISBN")
    # Format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    s_format = "%-10s %-1s %-50s"
    print(s_format % ("ISBN:", "|", "Title:"))

    # Prints book entries with the given ISBN (0 or more results)
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item[0], "|", item[1]))
    print("---End of Search Results---")


# Function to search for books by publisher name
def search_by_Publisher(Publisher_name):
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = book_dao.findByPublisherName(Publisher_name)

    # Displaying the results for books with the given publisher name
    print("Search by Publisher Name")
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            # Print the ISBN, title, and publisher information
            print(item[0], "|", item[1], "|", item[2])
    print("---End of Search Results---")


# Function to search for books within a specified price range
def search_by_PriceRange(Min, Max):
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = book_dao.findByPriceRange(Min, Max)

    # Displaying the results for books within the specified price range
    print("Search by Price Range")
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            # Print the ISBN, title, and price information
            print(item[0], "|", item[1], "|", item[2])
    print("---End of Search Results---")


# Function to search for books published in a specific year
def search_by_Year(Year):
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = book_dao.findByYear(Year)

    # Displaying the results for books published in the specified year
    print("Search by Year")
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            # Print the ISBN and title information
            print(item[0], "|", item[1])
    print("---End of Search Results---")


# Function to search for books by title and publisher
def search_by_Title_Publisher(title, publisher):
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = book_dao.findByTitleAndPublisher(title, publisher)

    # Displaying the results for books with the given title and publisher
    print("Search by Title and Publisher")
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            # Print the ISBN, title, and publisher information
            print(item[0], "|", item[1], "|", item[2])
    print("---End of Search Results---")


# Function to print the main menu options
def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print(str(key) + '.', menu_options[key], end="  ")
    print()
    print("The end of top-level options")
    print()


def option1():
    # Displaying information for adding a publisher
    print()
    print("-----Add Publisher-----")
    print("Type Null for no entry")

    # Taking user input for name
    name = input("Enter Name: ")

    # Initializing phone variable and ensuring it is a valid 10-digit integer
    phone = " "
    while phone == " ":
        phone = input("Enter phone Number: ")
        if len(phone) != 10:
            phone = ""
            print("Error: Phone number length must be 10!")
        try:
            int(phone)
        except ValueError:
            phone = ""
            print("Error: Phone number must consist of integers!")

    # Initializing city variable and ensuring it is not longer than 20 characters
    city = " "
    while city == " ":
        city = input("Enter city: ")
        if len(city) > 20:
            city = ""
            print("Error: City name too long (max 20 characters)!")

    # Calling the addPublisher function with the provided information
    result = book_dao.addPublisher(name, phone, city)

    # Displaying the result of the operation
    print(result)


# Option2 Add Book
# •	The system shall allow user to add a new book (ISBN, title, year, published_by, previous edition and price).
def option2():
    # Displaying information for adding a book
    print()
    print("-------Add Book-------")
    print("Type NULL for no entry.")

    # Taking user input for ISBN number and ensuring it is a valid 10-digit integer
    ISBN_num = ""
    while ISBN_num == "":
        ISBN_num = input("Enter ISBN Number: ")
        if len(ISBN_num) != 10:
            ISBN_num = ""
            print("Error: ISBN number length must be 10!")
        try:
            int(ISBN_num)
        except ValueError:
            ISBN_num = ""
            print("Error: ISBN number must consist of integers!")

    # Taking user input for book title and ensuring it is not longer than 50 characters
    title = ""
    while title == "":
        title = input("Enter title: ")
        if len(title) > 50:
            title = ""
            print("Error: title name too long (max 50 characters)!")

    # Taking user input for the year and ensuring it is a valid 4-digit integer
    year = ""
    while year == "":
        year = input("Enter year: ")
        if len(year) != 4:
            year = ""
            print("Error: year is invalid")
        try:
            int(year)
        except ValueError:
            year = ""
            print("Error: year must consist of integers!")

    # Taking user input for the publisher and ensuring it is not longer than 25 characters
    published_by = ""
    while published_by == "":
        published_by = input("Enter published_by: ")
        if len(published_by) > 25:
            published_by = ""
            print("Error: published_by name is too long")

    # Taking user input for the previous edition and ensuring it is not longer than 25 characters
    previous_edition = ""
    while previous_edition == "":
        previous_edition = input("Enter ISBN previous_edition: ")
        if len(previous_edition) > 25:
            previous_edition = ""
            print("Error: previous_edition name is too long")

    # Taking user input for the price and ensuring it is a valid float
    price = ""
    while price == "":
        price = input("Enter price: ")
        try:
            float(price)
        except ValueError:
            price = ""
            print("Error: price must consist of integers!")

    # Calling the addBook function with the provided information
    result = book_dao.addBook(ISBN_num, title, year,
                              published_by, previous_edition, price)

    # Displaying the result of the operation
    print(result)


# The system shall allow the user to edit book information.
def option3():
    # Displaying information for editing a book
    print()
    print("-------Edit Book-------")
    print("Type NULL for no entry.")

    # Dictionary to store updated information
    updated = {}

    # Taking user input for the ISBN number and ensuring it is a valid 10-digit integer
    ISBN_num = ""
    while ISBN_num == "":
        ISBN_num = input("Enter ISBN Number of the book you want to Edit: ")
        if len(ISBN_num) != 10:
            ISBN_num = ""
            print("Error: ISBN number length must be 10!")
        try:
            int(ISBN_num)
        except ValueError:
            ISBN_num = ""
            print("Error: ISBN number must consist of integers!")

    # Checking if the ISBN exists in the database
    if book_dao.ISBN_checker(ISBN_num):
        # Asking the user if they want to edit each field
        title = ""
        if input("Do you want to change the title? y or n: ") == 'y':
            while title == "":
                title = input("Enter title: ")
                if len(title) > 50:
                    title = ""
                    print("Error: title name too long (max 50 characters)!")
                updated['title'] = title

        year = ""
        if input("Do you want to change the year? y or n: ") == 'y':
            while year == "":
                year = input("Enter year: ")
                if len(year) != 4:
                    year = ""
                    print("Error: year is invalid")
                try:
                    int(year)
                    updated['year'] = year
                except ValueError:
                    year = ""
                    print("Error: year must consist of integers!")

        published_by = ""
        if input("Do you want to change the published_by? y or n: ") == 'y':
            while published_by == "":
                published_by = input("Enter published_by: ")
                if len(published_by) > 25:
                    published_by = ""
                    print("Error: published_by name is too long")
                updated['published_by'] = published_by

        previous_edition = ""
        if input("Do you want to change the previous_edition? y or n: ") == 'y':
            while previous_edition == "":
                previous_edition = input("Enter previous_edition: ")
                if len(previous_edition) > 25:
                    previous_edition = ""
                    print("Error: previous_edition name is too long")
                updated['previous_edition'] = previous_edition

        price = ""
        if input("Do you want to change the price? y or n: ") == 'y':
            while price == "":
                price = input("Enter price: ")
                try:
                    float(price)
                    updated['price'] = price
                except ValueError:
                    price = ""
                    print("Error: price must consist of integers!")

        # Checking if any fields were edited
        if len(updated) == 0:
            print("You have not edited any field!")
        else:
            # Calling the editBook function with the provided information
            result = book_dao.editBook(ISBN_num, updated)
            print("Editing successful")
    else:
        print("ISBN you entered does not EXIST!")

# The system shall allow the user to delete a book.


def option4():
    # Displaying information for deleting a book
    print()
    print("-----Delete a Book")
    print("Type ISBN of the book you want to delete")

    # Taking user input for the ISBN number and ensuring it is a valid 10-digit integer
    ISBN_num = ""
    while ISBN_num == "":
        ISBN_num = input("Enter ISBN Number: ")
        if len(ISBN_num) != 10:
            ISBN_num = ""
            print("Error: You must enter 10 digits")
        try:
            int(ISBN_num)
        except ValueError:
            ISBN_num = ""
            print("Error: ISBN number must consist of only integers!")

    # Calling the deleteBook function with the provided ISBN number
    result = book_dao.deleteBook(ISBN_num)

    # Displaying the result of the operation
    print(result)

# The system shall allow the user to search for books based on various criteria.


def option5():
    # Displaying information for searching books
    print()
    print("----- Search Book ----------")
    print()
    print("""
    Type A to search ALL BOOK
    Type B to search by TITLE
    Type C to search by ISBN
    Type D to search by PUBLISHER
    Type E to search by PRICE RANGE
    Type F to search by YEAR
    Type G to search by TITLE AND PUBLISHER""")

    # Taking user input for the choice of search criteria
    choice = input("Type your choice LETTER: ")

    # Performing the search based on the user's choice
    if choice == "A":
        # Calling the function to search for all books
        search_all_books()
    elif choice == "B":
        # Taking user input for the title and calling the function to search by title
        Title = input("Type a valid Title of a book: ")
        search_by_title(Title)
    elif choice == "C":
        # Taking user input for the ISBN and calling the function to search by ISBN
        ISBN_num = input("Type a valid ISBN: ")
        search_by_ISBN(ISBN_num)
    elif choice == "D":
        # Taking user input for the publisher name and calling the function to search by publisher
        Publisher_name = input("Type the name of the publisher: ")
        search_by_Publisher(Publisher_name)
    elif choice == "E":
        # Taking user input for the price range and calling the function to search by price range
        Min = input("Type Min price: ")
        Max = input("Type Max price: ")
        search_by_PriceRange(Min, Max)
    elif choice == "F":
        # Taking user input for the year and calling the function to search by year
        year = input("Type the year: ")
        search_by_Year(year)
    elif choice == "G":
        # Taking user input for title and publisher and calling the function to search by title and publisher
        print("Choose by Title and Publisher: ")
        title = input("Type Title name: ")
        publisher_name = input("Type publisher name: ")
        search_by_Title_Publisher(title, publisher_name)
    else:
        # Handling invalid input
        print("Please type a valid Letter")









# The system shall allow the user to exit the program.
def option6():
    # Exiting the program
    exit()


if __name__ == '__main__':
    # Main loop for the program
    while True:
        # Display the main menu
        print_menu()

        # Initialize option variable
        option = ''

        try:
            # Take user input for the choice and convert it to an integer
            option = int(input('Enter your choice: '))

        except KeyboardInterrupt:
            # Handle keyboard interrupt (Ctrl+C) gracefully
            print('Interrupted')
            sys.exit(0)

        except:
            # Handle invalid input (non-integer)
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        # All book
        elif option == 2:
            option2()
        # Add a publisher
        elif option == 3:
            option3()
        # Edit a book
        elif option == 4:
            option4()
        # Delete a book
        elif option == 5:
            option5()
        # More options to be added
        elif option == 6:
            # Exit the program
            print('Thanks for using our database services! Bye')
            option6()
        else:
            # Handle invalid option
            print('Invalid option. Please enter a number between 1 and 6.')
