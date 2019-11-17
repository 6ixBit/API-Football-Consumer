# API-Football-Consumer

Scripted in Python, powered by MongoDB.

# About
This script grabs data from an API (https://www.api-football.com/), sorts it and then writes it to a mongo database. The Mongo cluster is currenlty being used to host the statistics of every Premier League player registered in the 19/20 Premier league season. Stats such as shots, goals, assits, player info are all stored.

# Setup

1. Install Python 3 on your machine. https://www.python.org/downloads/
2. Install virtual env on your machine (pip3 install venv)
3. Setup venv run (python -m venv venv) in app directory
4. Activate virtual environment (source venv/bin/activate)
5. Install packages (pip install -package-). Replace -package- with pymongo and run it. Do the same for requests and pprint
  
 # Run
 Run the grab_data.py script by typing (python grab_data.py) in your terminal.  
 
