from Lesson2 import config
from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from Lesson2.src.routes import Smoke, FilmListApi


app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html.jinja2')


@app.route('/greeting', methods=['POST'])
def greeting():
    name = request.form.get('name')
    if not name:
        return 'Please, enter the name', 400
    return render_template('greeting.html.jinja2', name=name)


from Lesson2.src import models, routes