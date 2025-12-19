import sqlite3
from tkinter import INSERT

def drop_tables():
    connection, cursor = start_db()
    cursor.execute('DROP TABLE IF EXISTS catalog')
    finalize_db(connection)

def start_db(): # Создаем и подключаемся к базе данных
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    return connection, cursor # возвращает кортеж (connection - подключение к бд, cursor - работа с бд)

def create_catalog_table(): # Создаем таблицу catalog, если ее нет
    connection, cursor = start_db()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS catalog (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nazvaniye TEXT NOT NULL,
        sena INTEGER NOT NULL,
        pol TEXT NOT NULL,
        style TEXT NOT NULL,
        image TEXT
    )
    ''')
    finalize_db(connection)

def insert_sample_data_catalog(): # Вводит данные в таблицу catalog
    connection, cursor = start_db()
    cursor.execute('''INSERT INTO catalog (nazvaniye, sena, pol, style, image) VALUES
        ('t-shirt', 20, 'Unisex', 'Casual', 'https://a.lmcdn.ru/img600x866/R/T/RTLACV897801_20665420_1_v1.jpg'),
        ('jeans', 50, 'Men', 'Casual', 'https://xcdn.next.co.uk/common/items/default/default/itemimages/3_4Ratio/product/lge/W34945s.jpg'),
        ('skirt', 80, 'Women', 'Formal', 'https://cdn-images.farfetch-contents.com/20/85/14/33/20851433_50703613_1000.jpg')
        ''')
    finalize_db(connection)

def select_catalog_by_gender(gender):
    connection, cursor = start_db()
    cursor.execute(
    "SELECT nazvaniye, sena, pol, style, image FROM catalog WHERE pol = ?",
    (gender,)
    )
    items = cursor.fetchall()
    finalize_db(connection)
    return items

def select_by_style(style):
    connection, cursor = start_db()
    cursor.execute(
        "SELECT nazvaniye, sena, image FROM catalog WHERE style = ?",
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

if __name__ == "__main__":
    drop_tables()
    create_catalog_table()
    insert_sample_data_catalog()
