import sqlite3
from datetime import datetime
import random
import pandas as pd
import pywhatkit
import re


def create_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS RecordONE (song_name REAL)')


def data_entry(number):
    conn = sqlite3.connect('data1.db')
    c = conn.cursor()
    # time = current_time
    c.execute("INSERT INTO RecordONE (song_name) VALUES(?)", (number))
    conn.commit()


# create_table()
# data_entry(num1)


# c.close()
# conn.close()


def anything(s):
    d = s+'.db'
    conn = sqlite3.connect(d)
    c = conn.cursor()

    now = datetime.now()

    current_time = now.strftime("%D:%H:%M:%S")
    # print("Current Time =", current_time)
    db = sqlite3.connect(d)
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






