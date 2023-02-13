# CREATE BS
def base():
    import sqlite3

    with sqlite3.connect('base.db') as bd:
        bd.execute('''CREATE TABLE IF NOT EXISTS user(name TEXT, email TEXT, age INTEGER);''')