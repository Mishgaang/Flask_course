from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from Lesson2.src.database.models import Actor


class ActorShema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actor
        load_instance = True
