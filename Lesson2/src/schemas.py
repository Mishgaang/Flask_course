from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from Lesson2.src.models import Film, Actor


class FilmShema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        exclude = ['id']
        load_instance = True


class ActorShema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actor
        load_instance = True
