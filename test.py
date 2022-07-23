import sqlite3
# from datetime import datetime
import pandas as pd

def create_table():
    conn = sqlite3.connect('data1.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS RecordONE (song_name REAL)')



def data_entry(number):
    conn = sqlite3.connect('data1.db')
    c = conn.cursor()
    # time = current_time
    c.execute("INSERT INTO RecordONE (song_name) VALUES(?)", (number))
    conn.commit()
create_table()
df = pd.read_csv('data1.csv')


for i in range(1000000):
    a = df.iloc[i]
    data_entry(a)
    print(a)