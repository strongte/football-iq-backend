# first_aid.py
from flask import Blueprint, jsonify, request
import json
import os

FIRST_AID_FILE = "first_aid.json"
first_aid_routes = Blueprint('first_aid_routes', __name__)

# Ensure file exists
if not os.path.exists(FIRST_AID_FILE):
    with open(FIRST_AID_FILE, 'w') as f:
        json.dump({"topics": []}, f)

# Load first aid data
def load_data():
    with open(FIRST_AID_FILE, 'r') as f:
        return json.load(f)

# Save first aid data
def save_data(data):
    with open(FIRST_AID_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@first_aid_routes.route('/first-aid', methods=['GET'])
def get_all_topics():
    data = load_data()
    return jsonify(data['topics'])

@first_aid_routes.route('/first-aid/<injury_id>', methods=['GET'])
def get_topic(injury_id):
    data = load_data()
    topic = next((item for item in data['topics'] if item.get("id") == injury_id), None)
    if topic:
        return jsonify(topic)
    return jsonify({"message": "Topic not found"}), 404

@first_aid_routes.route('/first-aid', methods=['POST'])
def add_topic():
    new_topic = request.get_json()
    data = load_data()
    data['topics'].append(new_topic)
    save_data(data)
    return jsonify({"message": "First aid topic added", "status": "success"})

