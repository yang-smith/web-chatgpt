# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '')


    results = [
        {'id': 1, 'title': '问题1'},
        {'id': 2, 'title': '问题2'},
        {'id': 3, 'title': '问题3'},
    ]

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
