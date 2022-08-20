#!/bin/bash

sudo pip3 install pywhatkit
sudo pip3 install db-sqlite3
sudo pip3 install pandas

sudo python3 -c "$(curl -fsSl https://raw.githubusercontent.com/Adityaadpandey/SongRecommendationBot/test/single/real.py)"