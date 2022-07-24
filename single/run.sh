#!/bin/bash

try {
    sudo pip3 install pywhatkit
    sudo pip3 install pip install db-sqlite3
    sudo pip3 install pandas

} catch (e) {
    echo "Error: " + e
}

python3 -c "$(curl -fsSl https://raw.githubusercontent.com/Adityaadpandey/SongRecommendationBot/test/single/real.py)"