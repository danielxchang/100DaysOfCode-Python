from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)
outcomes = {
    'You found me!': ('https://media.giphy.com/media/26tknCqiJrBQG6bxC/giphy.gif', 'green'),
    'Too low, try again!': ('https://media.giphy.com/media/XJLEXP9xEJRevqXxnR/giphy.gif', 'red'),
    'Too high, try again!': ('https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif', 'blue')
}


def result_decorator(function):
    def wrapper(**kwargs):
        message = function(**kwargs)
        gif, color = outcomes[message]
        return f"<h1 style='color: {color}'>{message}</h1>" \
               f"<img src={gif} width=500>"
    return wrapper


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/glJdAXojfP3wPEg84a/giphy.gif" width=500>'


@app.route('/<int:guess>')
@result_decorator
def guess_number(guess):
    if random_number == guess:
        return "You found me!"
    elif random_number > guess:
        return "Too low, try again!"
    else:
        return "Too high, try again!"


if __name__ == "__main__":
    app.run(debug=True)
