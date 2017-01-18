#!flask/bin/python
"""
    Main Aplication to run service
    @author Thiago Pagonha
"""
from flask import Flask, request
from flask_cors import CORS
from api.login import login_service

app = Flask(__name__)
app.register_blueprint(login_service)
CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
