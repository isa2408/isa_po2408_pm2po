import sqlite3

def start_db():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    return connection, cursor

def finalize_db(connection):
    connection.commit()
    connection.close()

# 1. Товары
def create_catalog_table():
    connection, cursor = start_db()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS catalog (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        gender TEXT NOT NULL,
        style TEXT NOT NULL,
        image TEXT
    )
    ''')
    finalize_db(connection)

# 2. Категории
def create_categories_table():
    connection, cursor = start_db()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        season TEXT
    )
    ''')
    finalize_db(connection)

# 3. Бренды
def create_brands_table():
    connection, cursor = start_db()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS brands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country TEXT,
        founded_year INTEGER
    )
    ''')
    finalize_db(connection)

# 4. Размеры
def create_sizes_table():
    connection, cursor = start_db()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sizes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        size TEXT NOT NULL,
        description TEXT,
        gender TEXT
    )
    ''')
    finalize_db(connection)

# 5. Цвета
def create_colors_table():
    connection, cursor = start_db()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS colors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        hex_code TEXT,
        is_basic INTEGER
    )
    ''')
    finalize_db(connection)

def create_all_tables():
    create_catalog_table()
    create_categories_table()
    create_brands_table()
    create_sizes_table()
    create_colors_table()

if name == "main":
    create_all_tables()
    print("Все таблицы успешно созданы")