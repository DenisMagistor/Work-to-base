# Работа с SQLite 3
# Создать базу данных
# Создать для базы данных генератор данных {name: str, age: int, email: str}
# и желательно отсортировать прежде чем добавлять

from base_generator import generator_data

if __name__ == '__main__':
    import sqlite3

    with sqlite3.connect('base.db') as db:
        cursor = db.cursor()
        cursor.executemany('INSERT INTO user VALUES (?, ?, ?)', generator_data(need=10))
        