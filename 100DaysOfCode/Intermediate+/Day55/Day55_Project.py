from flask import Flask
import random as rand


app = Flask(__name__)

def check_guess(func):
    def wrapper(**kwargs):
        users_guess = int(kwargs["guess"])
        if users_guess == number_to_guess:
            return "<h1>You Found Me!</h1>" \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt="">" 
        elif users_guess > number_to_guess:
            return "<h1>Too high, Try Again</h1>" \
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt="">" 
        else:
            return "<h1>Too Low, Try Again</h1>" \
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt="">" 
    return wrapper


@app.route("/")
def home_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt="">"

@app.route('/<guess>')
@check_guess
def user_guess(guess):
    return guess

if __name__ == '__main__':
    number_to_guess = rand.randint(0,9)
    print(number_to_guess)
    app.run(debug=True)