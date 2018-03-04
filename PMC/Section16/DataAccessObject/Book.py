import sqlite3


class Book:
    def __init__(self):
        database_path = "data/books.db"
        self.con = sqlite3.connect(database_path)
        self.cur = self.con.cursor()

    def __enter__(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS "
            "`Book` (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT)"
        )
        self.con.commit()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.con.close()

    def fetch(self):
        data = self.cur.execute("SELECT * FROM `Book`").fetchall()
        return data

    def get(self, book):
        data = self.cur.execute("SELECT * FROM `Book` WHERE title=? OR author=? OR year=? OR isbn=?", book).fetchall()
        return data

    def add(self, book):
        self.cur.execute("INSERT INTO `Book` VALUES (NULL,?,?,?,?)", book)
        self.con.commit()

    def update(self, book_id, book):
        merged_book = tuple(j for i in (book, book_id) for j in (i if isinstance(i, tuple) else (i,)))

        self.cur.execute("UPDATE `Book` set title=?, author=?, year=?, isbn=? WHERE id=?", merged_book)
        self.con.commit()

    def delete(self, book_id):
        self.cur.execute("DELETE FROM `Book` where id=?", (book_id,))
        self.con.commit()

