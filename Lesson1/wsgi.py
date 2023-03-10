from flask import Flask, render_template

app = Flask(__name__)


def get_films():
    return [
        {
            'id': 1,
            'title': 'Harry Potter and the Philossopher\'s Stone',
            'release_date': 'November 4, 2001'
        },
        {
            'id': 2,
            'title': 'Harry Potter Chamber of Secrets',
            'release_date': 'November 3, 2002'
        }
    ]


@app.route('/')
@app.route('/hello')
def index():
    films = get_films()
    return render_template('hello.html.jinja2', films=films, title='Hello')


@app.route('/about')
def about():
    return render_template('about.html.jinja2', title='About')


@app.route('/<string:name>')
def greeting(name: str):
    return f'Hello, {name.capitalize()}'


if __name__ == '__main__':
    app.run(port=5003)
