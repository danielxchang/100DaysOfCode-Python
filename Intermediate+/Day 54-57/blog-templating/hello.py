from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_object = Post(post['id'], post['body'], post['title'], post['subtitle'])
    post_objects.append(post_object)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/blog/<int:blog_id>')
def show_post(blog_id):
    return render_template('post.html', blog=post_objects[blog_id - 1])


if __name__ == "__main__":
    app.run(debug=True)
