import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_table():
    conn = psycopg2.connect("dbname='database1' user='vagrant' password='' host='192.168.33.10' port='5432'")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='vagrant' password='' host='192.168.33.10' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


def fetch():
    conn = psycopg2.connect("dbname='database1' user='vagrant' password='' host='192.168.33.10' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='database1' user='vagrant' password='' host='192.168.33.10' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM Store WHERE item = %s", (item,))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='vagrant' password='' host='192.168.33.10' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE Store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
update("Banana", 45, 2.99)
print(fetch())
