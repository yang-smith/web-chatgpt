import pytest
import json
from app import create_app, db

def test_chart(test_app, test_database, mocker):
    # Mock the create_chat_completion function
    expected_message = "Test message"
    mocker.patch('app.utils.openai_utils.create_chat_completion', return_value={
        'choices': [{'message': {'content': expected_message}}]
    })

    response = test_app.get('/api/chart?content=test')
    assert response.status_code == 200
    assert response.get_json()['message'] == expected_message
