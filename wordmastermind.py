from flask import Flask, request, make_response
from database import db_session
from exceptions import WordNotFound

from services import word_service

app = Flask(__name__)

@app.errorhandler(WordNotFound)
def handle_word_not_found(e):
    return {'message': e.message}, 400

@app.after_request
def after_request_func(data):
    response = make_response(data)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route("/", methods=['POST'])
def word():
    json = request.get_json()
    if 'word' in json:
        return word_service.validateWordMaster(json['word'])
    else:
        return {'message': 'attribute word is required'}, 400

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

