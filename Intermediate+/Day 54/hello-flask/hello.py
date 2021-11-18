from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        text = function()
        return f"<b>{text}<b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        text = function()
        return f"<em>{text}<em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        text = function()
        return f"<u>{text}<u>"
    return wrapper_function


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media3.giphy.com/media/KPfkwDtE0fBKkJVYyN/200.webp">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye'


@app.route('/username/<name>/<int:num>')
def greet(name, num):
    return f"Hello {name}! You are {num} years old."


if __name__ == "__main__":
    app.run()
