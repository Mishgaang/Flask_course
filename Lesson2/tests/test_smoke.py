import http

from Lesson2.src import app


def test_smoke():
    client = app.test_client()
    resp = client.get('/smoke')

    assert resp.status_code == http.HTTPStatus.OK