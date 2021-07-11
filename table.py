import sqlite3
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%D:%H:%M:%S")
print(current_time)

conn = sqlite3.connect("data.db")
c = conn.cursor()

def table():
    c.execute('CREATE TABLE IF NOT EXISTS RecordOne(song_name Real, time Text)')

def deploy():

    time = current_time
    song = input("ok! which song- ")
    c.execute('INSERT INTO RecordOne(song_name, time) VALUES (?,?)', (song, time))

table()
deploy()

conn.commit()
c.close()
conn.close()