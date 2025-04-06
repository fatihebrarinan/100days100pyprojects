import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_route():
    return '<h1> Guess a number between o and 9 </h1> <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" 0 to 9 </img>'

random_number = random.randint(0,9)

@app.route('/<int:number>')
def guess_route(number):
    if number > random_number:
        return '<h1 style="color: blue" > Too High! </h1> <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" 0 to 9 </img>'
    elif number < random_number:
        return '<h1 style="color: red" > Too Low! </h1> <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" 0 to 9 </img>'
    else:
        return '<h1 style="color: green" > You Guessed Correctly!! </h1> <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" 0 to 9 </img>'
