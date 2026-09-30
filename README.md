Joke API CLI

A beginner Python command-line tool that fetches a random joke from a public API and saves it as a CSV file.

What I Learned

Python variables

Dictionaries

JSON data

API requests

CSV files

Git and GitHub

How It Works

The program:

Sends a request to JokeAPI.

Receives the response as JSON.

Checks the type of joke.

Processes the joke data.

Prints the joke in the terminal.

Saves the result to joke.csv.

Requirements

Python 3 and the requests library.

Install requests:

pip install requests

Run
python main.py

Project Structure
joke-api-cli/
├── main.py
├── README.md
└── .gitignore

API

This project uses JokeAPI to retrieve public joke data.

Future Improvements

Add JSON output

Allow users to choose a joke category

Save multiple jokes

Add better error handling

Author

My first Python API mini-project.