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


@app.get('/todo/api/')
def get_all():
    db = Db()
    data = db.read_all()
    return jsonify(data)

@app.get('/todo/api/<id>')
def get_one(id):
    db = Db()
    result = db.read_one(id)
    if result == None:
        return jsonify('NULL'), 404
    return jsonify(result)


@app.post('/todo/api/')
def post_todo():
    data = request.get_json()
    if not "name" in data:
        return jsonify("bad data"), 400
    db = Db()
    result = db.new_todo(data['name'])
    print("RESULT: ", result)
    return jsonify({"saved": result}), 201

@app.put('/todo/api/<id>')
def update_task(id:int):
    data = request.get_json()
    if not "name" in data:
        return jsonify("bad data"), 400
    db = Db()
    result = db.update_one(id, data['name'])
    if result == None:
        return jsonify("NULL"), 400
    return jsonify(result), 200

@app.delete('/todo/api/<id>')
def delete_task(id:int):
    db = Db()
    result = db.delete_one(id)
    if result == None:
        return jsonify("NULL"), 404
    return jsonify(result), 200

@app.patch('/todo/api/<id>')
def upd_state(id):
    data = request.get_json()
    if not 'state' in data: return jsonify('NULL'), 404
    db = Db()
    result = db.update_state(id, data['state'])
    if result == None:
        return jsonify("NULL"), 404    
    return jsonify(result), 200