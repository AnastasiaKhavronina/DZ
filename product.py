import sqlite3

conn = sqlite3.connect('product.db')
c = conn.cursor()

c.execute('''CREATE TABLE Products (
                Name TEXT,
                Price REAL,
                Quantity INTEGER)''')

c.execute("INSERT INTO Products VALUES ('Хлеб', 35.00, 10)")
c.execute("INSERT INTO Products VALUES ('Молоко', 70.00, 5)")

conn.commit()
conn.close()