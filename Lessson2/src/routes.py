from flask_restful import Resource
from flask import request
from typing import List


class Smoke(Resource):
    def get(self):
        return {'message': 'OK'}, 200


def get_all_films():
    return [
        {
            'id': '1',
            'title': 'Harry Potter and the Philossopher\'s Stone',
            'release_date': 'November 4, 2001'
        },
        {
            'id': 2,
            'title': 'Harry Potter Chamber of Secrets',
            'release_date': 'November 3, 2002'
        }
    ]


def get_film_by_uid(uid: str) -> dict:
    films = get_all_films()
    film = list(filter(lambda f: f[id] == uid, films))
    return film[0] if film else []


def create_film(film_json: dict) -> List[dict]:
    films = get_all_films()
    films.append(film_json)
    return films


class FilmListApi(Resource):
    def get(self, uid=None):
        if not uid:
            films = get_all_films()
            return films, 200
        film = get_film_by_uid(uid)
        if not film:
            return '', 404
        return film, 200

    def post(self):
        film_json = request.json
        return create_film(film_json), 201

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
