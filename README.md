# Player_DB

Scripted in Python, powered by MongoDB.

# About
This application grabs data from an API, it sorts it and then writes it to my mongo database which is currenlty being used to host the stats of every Premier League player in the 19/20 football season. Stats such as shots, goals, assits, player info are all stored.

# Setup

1. Install Python 3 on your machine. https://www.python.org/downloads/
2. Install virtual env on your machine (pip3 install venv)
3. Setup venv (python -m venv venv) in app directory
4. Activate virtual environment (source venv/bin/activate)
5. Install packages (pip install -package-). Replace -package- with pymongo and run it. Do the same for requests, pymongo and pprint
  
 # Run
 Run the grab_data.py script by typing (python3 grab_data.py) in your terminal.  
 
