class Book:
    def __init__(self, book_dao):
        self.book_dao = book_dao

    def show_books(self):
        for book in self.book_dao.fetch():
            yield book

    def search_book(self, book_values):
        for book in self.book_dao.get(book_values):
            yield book

    def add_book(self, book_values):
        self.book_dao.add(book_values)

    def update_book(self, book_id, book_values):
        self.book_dao.update(book_id, book_values)

    def delete_book(self, book_id):
        self.book_dao.delete(book_id)