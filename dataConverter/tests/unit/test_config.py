import pytest

from app import app as create_app
expected = b'<!doctype html>'

@pytest.fixture
def app():
    app = create_app
    app.config.update({
        'TESTING': True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()


def test_index(app,client):
    response = client.get('/')
    assert response.status_code == 200
    assert expected in response.data

def test_extract(app,client):
    response = client.get('/extract')
    assert response.status_code == 200
    assert expected in response.data

def test_style(app,client):
    response = client.get('/style')
    assert response.status_code == 200
    assert expected in response.data

def test_serve(app,client):
    response = client.get('/serve')
    assert response.status_code == 200
    assert expected in response.data

def test_query_page(app,client):
    response = client.get('/extract')
    assert response.status_code == 200
    assert expected in response.data