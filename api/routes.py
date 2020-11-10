from flask import jsonify, request
from api import main
from api.service import book_service
from api.repository.book_entity import Book


@main.route('/')
def index():
    return 'Hello index finally!'


@main.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    book = Book(data['name'], data['author'], data['description'])
    book = book_service.create_book(book)
    return jsonify(book.serialize())


@main.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = Book(data['name'], data['author'], data['description'])
    book = book_service.update_book(book_id, book)
    return jsonify(book.serialize())


@main.route('/books/<int:book_id>', methods=['PATCH'])
def patch_book(book_id):
    data = request.get_json()
    book = Book(data.get('name'), data.get('author'), data.get('description'))
    book = book_service.update_book(book_id, book)
    return jsonify(book.serialize())


@main.route('/books/<int:book_id>')
def get_book(book_id):
    book = book_service.get_book(book_id)
    return jsonify(book.serialize())


@main.route('/books')
def get_all_books():
    books = book_service.get_all_books()
    return jsonify([book.serialize() for book in books])


@main.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book_service.delete_book(book_id)
    return jsonify(True)
