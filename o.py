# import os
import pywhatkit

# def get_files(path):
#     for file in os.listdir(path):
#         if os.path.isfile(os.path.join(path, file)):
#             yield file

# for file in get_files(r'single'):
#     if file.endswith('.db'):
#         print(file)
# pywhatkit.playonyt('"1x1 glantis"')

import sqlite3
from datetime import datetime
import pandas as pd
import re

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

anything('data')