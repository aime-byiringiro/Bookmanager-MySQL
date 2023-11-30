
import mysql.connector
from mysql_connector import connection

# Function to retrieve all books from the database


def findAll():
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"
    cursor.execute(query)
    results = cursor.fetchall()
    return results

# Function to check if a book with the given ISBN exists in the database


def ISBN_checker(ISBN_num):
    cursor = connection.cursor()
    query = "SELECT ISBN FROM Book WHERE ISBN = " + ISBN_num
    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except mysql.connector.errors as err:
        results = err
    return results

# Option1
# Function to add a publisher to the database


def addPublisher(name, phone, city):
    cursor = connection.cursor()
    query = "insert into Publisher values ('" + \
        name + " ', '" + phone + " ', '" + city + " ')"
    try:
        cursor.execute(query)
        connection.commit()
    except mysql.connector.errors.IntegrityError:
        cursor.close()
        return "Duplicate entry: publisher <" + name + "> already exists!"
    cursor.close()
    return "Publisher <" + name + "> added successfully"

# Option2_Add
# Function to add a book to the database


def addBook(ISBN_num, title, year, published_by, previous_edition, price):
    cursor = connection.cursor()
    if previous_edition == "NULL" and published_by == "NULL":
        query = "insert into Book values('" + ISBN_num + "', '" + \
            title + "', '" + year + "', NULL, NULL, '" + price + "')"
    elif previous_edition == "NULL":
        query = "insert into Book values('" + ISBN_num + "', '" + title + \
            "', '" + year + "', '" + published_by + "', NULL, '" + price + "')"
    elif published_by == "NULL":
        query = "insert into Book values('" + ISBN_num + "', '" + title + \
            "', '" + year + "', NULL, '" + previous_edition + "', '" + price + "')"
    else:
        query = "insert into Book values('" + ISBN_num + "', '" + title + "', '" + year + \
            "', '" + published_by + "', '" + previous_edition + "', '" + price + "')"

    try:
        cursor.execute(query)
        connection.commit()
    except mysql.connector.errors.IntegrityError as err:
        cursor.close()
        return ("Error: {}".format(err))
    except mysql.connector.errors:
        return ("Something is invalid about the values you entered.")
    cursor.close()
    return "Book <" + ISBN_num + "> added successfully"


# Option3
# Function to edit a book in the database based on ISBN number and updated information
def editBook(ISBN_num, updated):
    cursor = connection.cursor()
    query = "UPDATE BOOK SET "

    # Check each field in the 'updated' dictionary and build the query accordingly
    if 'title' in updated:
        title = updated['title']
        query += "title = "
        if title == "NULL":
            query += "NULL"
        else:
            query += "'" + title + "'"
        updated.pop('title')
        if len(updated) != 0:
            query += ", "

    if 'year' in updated:
        year = updated['year']
        query += "year = "
        if year == "NULL":
            query += "NULL"
        else:
            query += "'" + year + "'"
        updated.pop('year')
        if len(updated) != 0:
            query += ", "

    if 'published_by' in updated:
        published_by = updated['published_by']
        query += "published_by = "
        if published_by == "NULL":
            query += "NULL"
        else:
            query += "'" + published_by + "'"
        updated.pop('published_by')
        if len(updated) != 0:
            query += ", "

    if 'previous_edition' in updated:
        previous_edition = updated['previous_edition']
        query += "previous_edition = "
        if previous_edition == "NULL":
            query += "NULL"
        else:
            query += "'" + previous_edition + "'"
        updated.pop('previous_edition')
        if len(updated) != 0:
            query += ", "

    if 'price' in updated:
        price = updated['price']
        query += "price = "
        if price == "NULL":
            query += "NULL"
        else:
            query += "'" + price + "'"
        updated.pop('price')
        if len(updated) != 0:
            query += ", "

    query += " WHERE ISBN = '" + ISBN_num + "'"

    try:
        cursor.execute(query)
        connection.commit()
    except Exception as err:
        cursor.close()
        return ("Error: {}".format(err))

    cursor.close()
    return "Book <" + ISBN_num + "> edited successfully"


# Option4
# Function to delete a book from the database based on ISBN number
def deleteBook(ISBN_num):
    cursor = connection.cursor()
    query = "DELETE FROM Book WHERE ISBN = %s"

    try:
        cursor.execute(query, (ISBN_num,))
        affected_rows = cursor.rowcount
        if affected_rows == 0:
            return "The ISBN does not exist in the database"

        connection.commit()
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()

    return f"Book <{ISBN_num}> deleted successfully"

# Option5
# Function to find books by title


def findByTitle(title):
    # returns all tuples in Book with specified title attribute
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.title='" + title + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

# Function to find books by ISBN number


def findByISBN(ISBN_num):
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.ISBN='" + ISBN_num + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

# Function to find books by publisher name


def findByPublisherName(Name):
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title, Book.published_by from bookmanager.Book where Book.published_by='" + Name + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

# Function to find books within a specified price range


def findByPriceRange(Min, Max):
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title, Book.price from Bookmanager.Book where " + \
        Min + "<= Book.price and " + Max + ">= Book.price ORDER BY Book.price"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

# Function to find books published in a specific year


def findByYear(Year):
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from Bookmanager.Book where year = " + Year
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

# Function to find books by title and publisher


def findByTitleAndPublisher(Title, Publisher):
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title, Book.published_by from Bookmanager.Book where Book.title = '" + \
        Title + "' and Book.published_by = '" + Publisher + "' ;"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results
