#!flask/bin/python
"""
    Login Services
    @author Thiago Pagonha
"""
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

login_service = Blueprint('login_service', __name__)

users = [{
    'email' : 'thiago.alves@gsoftware.com.br',
    'password' : '654321'
},{
    'email' : 'admin@gsoftware.com.br',
    'password' : '123456'
}]

@login_service.route('/api/login/', methods=['POST'])
@cross_origin()
def login():
    content = request.json

    if not content or not content['email'] or not content['password'] :
        return jsonify({'error': 'Faltam os dados de email e/ou senha'}), 400

    user = [u for u in users if u['email'].encode('utf-8') == content['email'] and u['password'].encode('utf-8') == content['password']]

    if user:
        return jsonify({'authToken' : '33DE383DFDEE8'}), 200
    else :
        return jsonify({'error': 'Email and/or password incorrect'}), 401
