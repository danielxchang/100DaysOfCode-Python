from flask import Flask, render_template, request
import requests
from datetime import date, timedelta
from random import randrange
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
GMAIL_SMTP = "smtp.gmail.com"

my_email = os.environ.get("TEST_EMAIL")
password = os.environ.get("TEST_PW")

author = "Daniel Chang"

app = Flask(__name__)


def random_date():
    start_date = date(2020, 1, 1)
    end_date = date(2021, 10, 15)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = randrange(days_between_dates)
    rand_date = start_date + timedelta(days=random_number_of_days)
    return rand_date.strftime("%B %d, %Y")


def send_email(data):
    with smtplib.SMTP(GMAIL_SMTP, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        email_content = f"Name: {data['name']}\n" \
                        f"Email: {data['email']}\n" \
                        f"Phone Number: {data['phone']}\n" \
                        f"Message: {data['message']}"

        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: New Message\n\n{email_content}"
        )


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts, author=author)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if (method := request.method) == "POST":
        send_email(request.form)
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:id>')
def show_post(id):
    post = all_posts[id - 1]
    return render_template("post.html", post=post, author=author)


# @app.route('/form-entry', methods=['POST'])
# def receive_data():
#     data = request.form
#     return "<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    all_posts = requests.get(url="https://api.npoint.io/bf30b23b4bbc4d01728a").json()
    for post in all_posts:
        post['photo'] = "assets/img/" + post['title'].split()[-1].lower() + '.jpg'
        post['date'] = random_date()
    app.run(debug=True)