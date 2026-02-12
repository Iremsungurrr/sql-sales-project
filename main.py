import sqlite3

# Küçük bir satış sistemi denemek için veritabanı oluşturdum
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Müşteri tablosu
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

# Ürün tablosu
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
)
""")

# Satış tablosu
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER
)
""")

# Örnek veriler ekliyorum
cursor.executemany(
    "INSERT INTO customers (name) VALUES (?)",
    [("Ahmet",), ("Ayşe",), ("Mehmet",)]
)

cursor.executemany(
    "INSERT INTO products (name, price) VALUES (?, ?)",
    [
        ("Laptop", 15000),
        ("Telefon", 8000),
        ("Kulaklık", 1500)
    ]
)

cursor.executemany(
    "INSERT INTO sales (customer_id, product_id, quantity) VALUES (?, ?, ?)",
    [
        (1, 1, 1),
        (2, 2, 2),
        (1, 3, 3),
        (3, 1, 1)
    ]
)

conn.commit()

# Toplam ciroyu hesaplamak istedim
cursor.execute("""
SELECT SUM(products.price * sales.quantity)
FROM sales
JOIN products ON sales.product_id = products.id
""")

toplam_ciro = cursor.fetchone()[0]

print("Toplam Ciro:", toplam_ciro)

conn.close()
