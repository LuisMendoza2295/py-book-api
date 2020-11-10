from api.repository import session
from api.repository.book_entity import Book


def create_book(book):
    session.add(book)
    session.commit()
    return book


def update_book(book_id, book):
    curr_book = session.query(Book).filter_by(id=book_id).first()

    if book.name is not None:
        curr_book.name = book.name

    if book.author is not None:
        curr_book.author = book.author

    if book.description is not None:
        curr_book.description = book.description

    session.add(curr_book)
    session.commit()
    return curr_book


def get_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    return book


def get_all_books():
    books = session.query(Book).all()
    return books


def delete_book(book_id):
    curr_book = session.query(Book).filter_by(id=book_id).first()

    session.delete(curr_book)
    session.commit()
