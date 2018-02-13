import sqlite3


class Book:
    database_path = "data/books.db"

    def create_table(self):
        con = sqlite3.connect(self.database_path)
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS "
            "`Book` (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT)"
        )
        con.commit()
        con.close()

    def fetch(self):
        con = sqlite3.connect(self.database_path)
        cur = con.cursor()
        data = cur.execute("SELECT * FROM `Book`").fetchall()
        con.close()
        return data

    def get(self, book):
        con = sqlite3.connect(self.database_path)
        cur = con.cursor()
        data = cur.execute("SELECT * FROM `Book` WHERE title=? OR author=? OR year=? OR isbn=?", book).fetchall()
        con.close()
        return data

    def add(self, book):
        con = sqlite3.connect(self.database_path)
        cur = con.cursor()
        cur.execute("INSERT INTO `Book` VALUES (NULL,?,?,?,?)", book)
        con.commit()
        con.close()

    def update(self, book_id, book):
        merged_book = tuple(j for i in (book, book_id) for j in (i if isinstance(i, tuple) else (i,)))

        con = sqlite3.connect(self.database_path)
        cur = con.cursor()
        cur.execute("UPDATE `Book` set title=?, author=?, year=?, isbn=? WHERE id=?", merged_book)
        con.commit()
        con.close()

    def delete(self, book_id):
        con = sqlite3.connect(self.database_path)
        cur = con.cursor()
        cur.execute("DELETE FROM `Book` where id=?", (book_id,))
        con.commit()
        con.close()


bookDao = Book()
bookDao.create_table()
