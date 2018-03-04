import sqlite3


def create_table():
    conn = sqlite3.connect("data/lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("data/lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()


def fetch():
    conn = sqlite3.connect("data/lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("data/lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Store WHERE item = ?", (item,))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    conn = sqlite3.connect("data/lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE Store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
    conn.commit()
    conn.close()


print(fetch())
update("Mug", 20, 5.99)
print(fetch())

