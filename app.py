import json
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
app = Flask(__name__)
from model import Db  # noqa

load_dotenv()


@app.get("/")
def home():
    return "Home"


@app.get('/todo/api/<id>')
def get_one(id):
    result = Db.read_one(id)
    if result == None:
        return jsonify('NULL'), 404
    return jsonify(result)


@app.get('/todo/api')
def get_all():
    data = Db.read_all()
    return jsonify(data)


@app.post('/todo/api')
def post_todo():
    data = request.get_json()
    if not "name" in data:
        return jsonify("bad data"), 400
    result: bool = Db.new_todo(data['name'])
    print("RESULT: ", result)
    return jsonify({"saved": result}), 201


@app.put('/todo/api/<id>')
def put(id):
    data = request.get_json()
    if not "name" in data:
        return jsonify("bad data"), 400
    result = Db.update_one(id, data['name'])
    if result == None:
        return jsonify("NULL"), 400
    return jsonify(result), 200


@app.delete('/todo/api/<id>')
def delete_task(id: int):
    result = Db.delete_one(id)
    if result == None:
        return jsonify("NULL"), 404
    return jsonify(result), 200
