#!flask/bin/python
"""
    Login Services
    @author Thiago Pagonha
"""
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

login_service = Blueprint('login_service', __name__)

@login_service.route('/api/login/', methods=['POST'])
@cross_origin()
def login():
    content = request.json
    print(content)

    if not content or not content['email'] or not content['password'] :
        return jsonify({'error': 'Missing request data: email and/or password'}), 400

    if content['email'] == 'thiago.alves@gsoftware.com.br' and content['password'] == '654321':
        return jsonify({'authToken' : '33DE383DFDEE8'}), 200
    else :
        return jsonify({'error': 'Email and/or password incorrect'}), 401
