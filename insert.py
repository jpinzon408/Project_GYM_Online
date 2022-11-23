import sqlite3 as sl
# INSERT DATABASE EXAMPLE
con = sl.connect('gymdata.db')
c = con.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,username TEXT,password TEXT,age INTEGER,workout TEXT)')

sql = 'INSERT INTO users(id, username, password, age) values(?, ?, ?, ?)'
data = [
    (1, 'Alice', 'hola123', 23),
    (2, 'Anatoly', 'qw12', 35),
    (3, 'Chris', 'as12', 30)
]
