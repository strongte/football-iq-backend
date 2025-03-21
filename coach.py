# coach.py
from flask import Blueprint, jsonify
import json
import os

COACH_FILE = "coach_resources.json"
coach_routes = Blueprint('coach_routes', __name__)

# Ensure the file exists and load it
def load_resources():
    if not os.path.exists(COACH_FILE):
        with open(COACH_FILE, 'w') as f:
            json.dump({"resources": []}, f)
    with open(COACH_FILE, 'r') as f:
        return json.load(f)

@coach_routes.route('/resources', methods=['GET'])
def get_resources():
    data = load_resources()
    return jsonify(data['resources'])

@coach_routes.route('/resources/new', methods=['GET'])
def get_new_resources():
    data = load_resources()
    new_only = [item for item in data['resources'] if item.get('new') == True]
    return jsonify(new_only)

