from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice


def get_random_cafe(cafe_db):
    cafes = cafe_db.query.all()
    random_cafe = choice(cafes)
    return random_cafe.to_dict()


def get_all(cafe_db):
    cafes = cafe_db.query.all()
    return [cafe.to_dict() for cafe in cafes]


def post_new_cafe(form, db, cafe):
    new_cafe = cafe(
        name=form.cafe.data,
        map_url=form.location_url.data,
        img_url=form.img_url.data,
        location=form.location.data,
        has_sockets=bool(form.has_sockets.data),
        has_toilet=bool(form.has_toilet.data),
        has_wifi=bool(form.has_wifi.data),
        can_take_calls=bool(form.can_take_calls.data),
        seats=form.seats.data,
        coffee_price=form.coffee_price.data
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={
        "success": "Successfully added to the new cafe."
    })


def delete_cafe(cafe_id, cafe_db, db):
    if cafe := cafe_db.query.get(cafe_id):
        db.session.delete(cafe)
        db.session.commit()

# --------------------Possible Future Features----------------------------#
# def update_price(cafe_id):
#     if cafe := Cafe.query.get(cafe_id):
#         cafe.coffee_price = request.args.get('new_price')
#         db.session.commit()

# def search_cafe():
#     location = request.args.get('loc')
#     if match := Cafe.query.filter_by(location=location.title()).first():
#         return jsonify(cafe=match.to_dict())
#
#     return jsonify(error={
#         "Not Found": "Sorry, we don't have a cafe at that location"
#     })
