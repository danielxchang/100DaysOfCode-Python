from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("TMDB_API_KEY")

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


class RateMovieForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Done')


class FindMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(), Length(max=250)])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    for i, movie in enumerate(movies):
        ranking = len(movies) - i
        movie.ranking = ranking
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def rate_movie(id):
    selected_movie = Movie.query.get(id)
    edit_form = RateMovieForm()
    if edit_form.validate_on_submit():
        selected_movie.review = edit_form.review.data
        selected_movie.rating = edit_form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=selected_movie, form=edit_form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get('id')
    db.session.delete(Movie.query.get(movie_id))
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    movie_form = FindMovieForm()
    if movie_form.validate_on_submit():
        parameters = {
            'api_key': API_KEY,
            'query': movie_form.title.data
        }
        response = requests.get(url="https://api.themoviedb.org/3/search/movie", params=parameters)
        match_data = response.json()
        matches = match_data['results']
        return render_template("select.html", matches=matches)
    return render_template("add.html", form=movie_form)


@app.route("/get-selected-movie")
def get_movie_data():
    parameters = {
        'api_key': API_KEY,
    }
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{request.args.get('id')}", params=parameters)
    movie_data = response.json()
    new_movie = Movie(
        title=movie_data['title'],
        year=int(movie_data['release_date'].split('-')[0]),
        description=movie_data['overview'],
        rating=0,
        ranking=0,
        review="Not entered yet.",
        img_url="https://image.tmdb.org/t/p/w500" + movie_data['poster_path']
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("rate_movie", id=new_movie.id))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
