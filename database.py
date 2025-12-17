# import psycopg2
# from psycopg2 import OperationalError

# DB_CONFIG = {
#     "dbname": "your_db_name",
#     "user": "postgres",
#     "password": "your_password",
#     "host": "localhost",
#     "port": 5432
# }

# def get_connection():
#     try:
#         conn = psycopg2.connect(**DB_CONFIG)
#         return conn
#     except OperationalError as e:
#         print("Ошибка подключения к базе данных:", e)
#         return None


# def create_table():
#     conn = get_connection()
#     if conn is None:
#         return

#     cursor = conn.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS students (
#             id SERIAL PRIMARY KEY,
#             full_name VARCHAR(100) NOT NULL,
#             age INT CHECK (age > 0),
#             email VARCHAR(100) UNIQUE
#         );
#     """)

#     conn.commit()
#     cursor.close()
#     conn.close()


# if __name__ == "__main__":
#     create_table()
#     print("Таблица успешно создана")

import sqlite3


# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS catalog (
id INTEGER PRIMARY KEY,
nazvaniye TEXT NOT NULL,
sena INTEGER NOT NULL,
pol TEXT NOT NULL,
style TEXT NOT NULL
)
''')
# cursor.execute('''INSERT INTO catalog (nazvaniye, sena, pol, style) VALUES
# ('Futbolka', 20, 'Unisex', 'Casual'),
# ('Jinsi', 50, 'Men', 'Casual'),
# ('Platye', 80, 'Women', 'Formal')
# ''')
cursor.execute('''SELECT * FROM catalog''')
catalog_items = cursor.fetchall()
print(catalog_items)
# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()



