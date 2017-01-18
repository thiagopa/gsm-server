#!flask/bin/python
"""
    Main Aplication to run service
    @author Thiago Pagonha
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from api.login import login_service

app = Flask(__name__)

@app.route('/')
def index():
    return 'Service is Running!'

app.register_blueprint(login_service)
CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
