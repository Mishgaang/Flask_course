"""
SELECT QUERIES
"""
from Lesson2.src import db, app
from Lesson2.src.database import models

with app.app_context():
    films = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()

    harry_potter_and_ch_s = db.session.query(models.Film).filter(
        models.Film.title == 'Harry Potter and Chamber of Secrets'
    ).first()

    harry_potter_priz_az = db.session.query(models.Film).filter_by(
        title='Harry Potter and the Prizoner of Azkaban').first()

    and_statement_harry_potter = db.session.query(models.Film).filter(
        models.Film.title != 'Harry Potter and Chamber of Secrets',
        models.Film.rating >= 7.5
    ).all()

    phoenix = db.session.query(models.Film).filter(
        models.Film.title.like('%Phoenix%')
    ).all()

    harry_potter_sorted_by_length = db.session.query(models.Film).filter(
        ~models.Film.length.in_([146, 161])
    )[:2]

"""
QUERYING WITH JOINS
"""
with app.app_context():
    films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()

    a = db.session.query(models.Actor).first()

    print(a.films)