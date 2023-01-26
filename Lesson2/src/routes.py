from datetime import datetime

from flask_restful import Resource
from flask import request


# from Lesson2.src import db
# from Lesson2.src.models import Film


class Smoke(Resource):
    def get(self):
        return {'message': 'OK'}, 200


class FilmListApi(Resource):
    def get(self, uuid=None):
        from Lesson2.src import db
        from Lesson2.src.models import Film
        if not uuid:
            films = db.session.query(Film).all()
            return [f.to_dict() for f in films], 200
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        return film.to_dict(), 200

    def post(self):
        from Lesson2.src import db
        from Lesson2.src.models import Film
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data'}, 400
        try:
            film = Film(
                title=film_json['title'],
                release_date=datetime.strptime(film_json['release_date'], '%B %d, %Y'),
                distributed_by=film_json['distributed_by'],
                description=film_json.get('description'),
                length=film_json.get('length'),
                rating=film_json.get('rating')
            )
            db.session.add(film)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Create successfuly'}, 201

    def put(self, uuid):
        from Lesson2.src import db
        from Lesson2.src.models import Film
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data'}, 400
        try:
            db.session.query(Film).filter_by(uuid=uuid).update(
                dict(
                    title=film_json['title'],
                    release_date=datetime.strptime(film_json['release_date'], '%B %d, %Y'),
                    distributed_by=film_json['distributed_by'],
                    description=film_json.get('description'),
                    length=film_json.get('length'),
                    rating=film_json.get('rating')
                )
            )
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Updated successfuly'}, 200

    def patch(self, uuid):
        from Lesson2.src import db
        from Lesson2.src.models import Film
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        film_json = request.json
        for key in film_json.keys():
            film[key] = film_json[key]

        db.session.add(film)
        db.session.commit()
        return {'message': 'Updated successfuly'}, 200

    def delete(self, uuid):
        from Lesson2.src import db
        from Lesson2.src.models import Film
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        db.session.delete(film)
        db.session.commit()
        return '', 204
