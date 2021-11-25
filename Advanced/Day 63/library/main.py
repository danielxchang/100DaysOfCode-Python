from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


@app.route('/')
def home():
    return render_template("index.html", books=db.session.query(Books).all())


@app.route('/delete/<int:id>')
def delete(id):
    db.session.delete(Books.query.get(id))
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_book = Books(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit_rating(id):
    book_to_update = Books.query.filter_by(id=id).first()
    if request.method == "POST":
        book_to_update.rating = request.form['new-rating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", book=book_to_update)



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

