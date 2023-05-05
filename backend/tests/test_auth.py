import json
import pytest
from app.models.user import User

def test_register(test_app, test_database):
    response = test_app.post('/api/register',
                             data=json.dumps({"username": "testuser", "password": "testpassword"}),
                             content_type='application/json')
    assert response.status_code == 201
    user = User.query.filter_by(username='testuser').first()
    assert user is not None

def test_login(test_app, test_database):
    # 先创建一个测试用户
    user = User(username="testuser")
    user.set_password("testpassword")
    test_database.session.add(user)
    test_database.session.commit()

    response = test_app.post('/api/login',
                             data=json.dumps({"username": "testuser", "password": "testpassword"}),
                             content_type='application/json')
    assert response.status_code == 200
    assert 'token' in json.loads(response.data)
