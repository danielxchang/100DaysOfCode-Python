from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    name = "Daniel Chang"
    year = date.today().year
    return render_template("index.html", num=random_number, name=name, year=year)


@app.route("/guess/<name>")
def guess(name):
    gender = requests.get(url=f"https://api.genderize.io?name={name}").json()['gender']
    age = requests.get(url=f"https://api.agify.io?name={name}").json()['age']
    return render_template("prediction.html", name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
