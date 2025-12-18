import sqlite3

def start_db(): # Создаем и подключаемся к базе данных
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    return connection, cursor # возвращает кортеж (connection - подключение к бд, cursor - работа с бд)

def create_catalog_table(): # Создаем таблицу catalog, если ее нет
    connection, cursor = start_db()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS catalog (
    id INTEGER PRIMARY KEY,
    nazvaniye TEXT NOT NULL,
    sena INTEGER NOT NULL,
    pol TEXT NOT NULL,
    style TEXT NOT NULL,
    picture TEXT
    )
    ''')
    finalize_db(connection)
def insert_sample_data_catalog(): # Вводит данные в таблицу catalog
    connection, cursor = start_db()
    cursor.execute('''INSERT INTO catalog (nazvaniye, sena, pol, style) VALUES
    ('Futbolka', 20, 'Unisex', 'Casual'),
    ('Jinsi', 50, 'Men', 'Casual'),
    ('Platye', 80, 'Women', 'Formal')
    ''')
def select_catalog_by_gender(gender):
    connection, cursor = start_db()
    cursor.execute(
    "SELECT nazvaniye, sena, pol, style FROM catalog WHERE pol = ?",
    (gender,)
    )
    items = cursor.fetchall()
    finalize_db(connection)
    return items

def select_by_style(style):
    connection, cursor = start_db()
    cursor.execute(
        "SELECT nazvaniye, sena FROM catalog WHERE style = ?",
        (style,)
    )
    items = cursor.fetchall()
    finalize_db(connection)
    return items

def select_catalog(): # Выводит данные из таблицы catalog
    connection, cursor = start_db()
    cursor.execute('''SELECT * FROM catalog''')
    catalog_items = cursor.fetchall()
    finalize_db(connection)
    return catalog_items

def finalize_db(connection): # Сохраняет и закрывает базу данных
    connection.commit()
    connection.close()



