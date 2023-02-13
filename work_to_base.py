# Get data from the DB
def work(data: list = []):
    import sqlite3

    with sqlite3.connect('base.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM user')
        
        fetch = cursor.fetchall()

        for row in fetch:
            data.append(row)
        
        return data