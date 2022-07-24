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
    # df.loc[df['song_name'] == 'song_name']
    df2 = df.to_string(index=False)

# Using BlankIndex to print DataFrame without index 
    blankIndex=[''] * len(df)
    df.index=blankIndex

    # Using hide_index()
    df.style.hide_index()
    print(df)
    test = df.sample()
    # print(test)
    test = str(test)
    a = test.replace("song_name", "")
    print(a)
    # test.replace(int, "")

    # pattern = r'[0-9]'
    # ab = re.sub(pattern, '', a)
    # abc = ab.replace(" ", "")
    # abc = str(abc)
    # print(abc)
    pywhatkit.playonyt(a)

# c.execute('CREATE TABLE IF NOT EXISTS RecordONE (song_name REAL, time TEXT)')
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
    # while True:
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
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS RecordONE (song_name REAL, time TEXT)')
                print("Database is not exist")
                while True:
                    print("1.play music  \n2.exit\n")
                    var = int(input("Enter your choice: "))
                    if var == 1:
                        try1()
                        time.sleep(5)
                        for file in get_files(r'./'):
                            if file =='data.db':
                                print("Database exist")
                                while True:
                                    print("1.play music  \n2.play music from database \n3.exit\n")
                                    var1 = int(input("Enter your choice: "))
                                    if var1 == 1:
                                        try1()
                                        time.sleep(5)
                                        # try:
                                        #     try1()
                                        #     time.sleep(5)
                                        # except:
                                        #     print("")
                                    elif var1 == 2:
                                        anything('data')
                                        time.sleep(5)
                                        # try:
                                        #     anything('data')
                                        #     time.sleep(5)
                                        # except:
                                        #     print("Database is empty or do not exist")
                                    elif var1 == 3:
                                        exit()
                    elif var == 2:
                        exit()
                
            
data_on()