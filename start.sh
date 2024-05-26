#!/bin/sh

git clone https://github.com/CallPrep/assignment-summer-intern-2024.git
# Run chroma in the background
chroma run &

# Wait for 10 seconds
sleep 5

git clone https://github.com/CallPrep/assignment-summer-intern-2024.git

mkdir clean_data
mkdir files

python clean_data.py 

python setup_the_db.py
# Run fastapi with app.py
fastapi run app.py --port 5000