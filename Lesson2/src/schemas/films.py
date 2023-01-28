from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from Lesson2.src.database.models import Film


class FilmShema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        exclude = ['id']
        load_instance = True