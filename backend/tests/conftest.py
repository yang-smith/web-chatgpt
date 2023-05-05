import pytest
from app import create_app, db

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def test_database(test_app):
    db.create_all()
    yield db
    db.drop_all()
