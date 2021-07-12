import sqlite3
from datetime import datetime
import random
import pandas as pd
import pywhatkit
import re


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS RecordONE (song_name REAL, time TEXT)')


def data_entry(number):
    time = current_time
    c.execute("INSERT INTO RecordONE (song_name, time) VALUES(?, ?)", (number, time))
    conn.commit()


# create_table()
# data_entry(num1)


# c.close()
# conn.close()


def anything():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    now = datetime.now()

    current_time = now.strftime("%D:%H:%M:%S")
    # print("Current Time =", current_time)
    db = sqlite3.connect("data.db")
    data = pd.read_sql_query("SELECT song_name FROM RecordONE", db)

    # print(data)
    df = pd.DataFrame(data)
    test = df.sample()
    # print(test)
    test = str(test)
    a = test.replace("song_name", "")

    # test.replace(int, "")

    pattern = r'[0-9]'
    ab = re.sub(pattern, '', a)
    abc = ab.replace(" ", "")
    abc = str(abc)
    print(abc)
    pywhatkit.playonyt(abc)






