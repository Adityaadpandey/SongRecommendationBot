import sqlite3
from datetime import datetime


def table():
    c.execute('CREATE TABLE IF NOT EXISTS RecordOne(song_name Real, time Text)')

def deploy(song):
    
    now = datetime.now()
    current_time = now.strftime("%D:%H:%M:%S")
    print(current_time)
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    time = current_time
    
    c.execute('INSERT INTO RecordOne(song_name, time) VALUES (?,?)', (song, time))
    conn.commit()
    c.close()
    conn.close()

#table()
#deploy()

