books = {"most_recent_price": 0, "most_recent_isbn": ""}


def insert(isbn, price):

    if isbn in books.keys():
        books["most_recent_isbn"] = isbn

    else:
        books[isbn] = price
        books["most_recent_price"] = price
        books["most_recent_isbn"] = isbn


def lookup(isbn):
    if isbn in books.keys():
        books["most_recent_isbn"] = isbn
        return books[isbn]

    else:
        return -1


def erase(isbn):
    if isbn in books.keys():
        del books[isbn]
        return True
    else:
        return False