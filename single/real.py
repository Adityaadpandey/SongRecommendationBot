import pywhatkit
import time
import sqlite3
from datetime import datetime
import pandas as pd
import re
import os

def take_com():
    number = input('ok! which song or singer----')
    number = str(number)


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


def data_entry(number):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    now = datetime.now()

    current_time = now.strftime("%D:%H:%M:%S")
    print("Current Time =", current_time)

    time = current_time
    c.execute("INSERT INTO RecordONE (song_name, time) VALUES(?, ?)", (number, time))
    conn.commit()
    c.close()
    conn.close()


def try1():
    # import excel
    number = input('ok! which song or singer----')
    data_entry(number)
    pywhatkit.playonyt(number)


def try2():
    anything('data')

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def data_on():
    for file in get_files(r'./'):
        if file =='data.db':
            
            while True:
                print("1.play music \n2.play music from database \n3.exit\n")
                var = int(input("Enter your choice: "))
                if var == 1:
                    try1()
                    time.sleep(5)
                    # try:
                    #     try1()
                    #     time.sleep(5)
                    # except:
                    #     print("")
                elif var == 2:
                    anything('data')
                    time.sleep(5)
                    # try:
                    #     anything('data')
                    #     time.sleep(5)
                    # except:
                    #     print("Database is empty or do not exist")
                elif var == 3:
                    exit()
        else:
            print("Database is not exist")
            while True:
                print("1.play music  \n2.exit\n")
                var = int(input("Enter your choice: "))
                if var == 1:
                    try1()
                    time.sleep(5)
                elif var == 2:
                    exit()

data_on()