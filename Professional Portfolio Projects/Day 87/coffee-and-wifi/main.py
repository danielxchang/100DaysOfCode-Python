from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL
from cafe_api import *
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    img_url = StringField('Cafe Image Link (URL)', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    seats = StringField('Number of Seats', validators=[DataRequired()])
    has_toilet = BooleanField('Has Toilet?', default=True, validators=[DataRequired()])
    has_wifi = BooleanField('Has Wifi?', default=True, validators=[DataRequired()])
    has_sockets = BooleanField('Has Sockets?', default=True, validators=[DataRequired()])
    can_take_calls = BooleanField('Can Take Calls?', default=True, validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        post_new_cafe(form, db, Cafe)
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    column_headers = ["Cafe Name", "Cafe Image", "Map URL", "Location", "Seats", "Toilet?", "Wifi?",
                      "Sockets?", "Take Calls?", "Coffee Price"]
    return render_template('cafes.html', cafes=get_all(Cafe), list=list, column_names=column_headers)


@app.route('/cafe/<int:cafe_id>')
def show_cafe(cafe_id):
    column_headers = ["Location", "Seats", "Toilet?", "Wifi?",
                      "Sockets?", "Take Calls?", "Coffee Price"]
    return render_template('selected_cafe.html', cafe=Cafe.query.get(cafe_id).to_dict(), list=list, enumerate=enumerate,
                           column_names=column_headers)


@app.route('/delete/<int:cafe_id>')
def delete(cafe_id):
    delete_cafe(cafe_id, Cafe, db)
    return redirect(url_for("cafes"))


@app.route('/random')
def get_random():
    cafe = get_random_cafe(Cafe)
    return redirect(url_for("show_cafe", cafe_id=cafe['id']))


if __name__ == '__main__':
    app.run(debug=True)
