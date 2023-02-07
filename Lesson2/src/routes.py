from Lesson2.src import api
from Lesson2.src.resources.actors import ActorListApi
from Lesson2.src.resources.aggregations import AggregationApi
from Lesson2.src.resources.auth import AuthRegister, AuthLogin
from Lesson2.src.resources.films import FilmListApi
from Lesson2.src.resources.populate_db import PopulateDB
from Lesson2.src.resources.smoke import Smoke

api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
api.add_resource(ActorListApi, '/actors', '/actors/<uuid>', strict_slashes=False)
api.add_resource(AggregationApi, '/aggregations', strict_slashes=False)
api.add_resource(AuthRegister, '/register', strict_slashes=False)
api.add_resource(AuthLogin, '/login', strict_slashes=False)
api.add_resource(PopulateDB, '/populate_db', strict_slashes=False)
