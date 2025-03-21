# drills.py
from flask import Blueprint, jsonify
import json
import os

DRILLS_FILE = "drills.json"
drill_routes = Blueprint('drill_routes', __name__)

# Load drills data
def load_drills():
    if not os.path.exists(DRILLS_FILE):
        with open(DRILLS_FILE, 'w') as f:
            json.dump({"warmups": [], "conditioning": []}, f)
    with open(DRILLS_FILE, 'r') as f:
        return json.load(f)

@drill_routes.route('/warmups', methods=['GET'])
def get_warmups():
    drills = load_drills()
    return jsonify(drills.get("warmups", []))

@drill_routes.route('/conditioning', methods=['GET'])
def get_conditioning():
    drills = load_drills()
    return jsonify(drills.get("conditioning", []))

@drill_routes.route('/new', methods=['GET'])
def get_new_drills():
    drills = load_drills()
    new_drills = {
        "warmups": [d for d in drills.get("warmups", []) if d.get("new")],
        "conditioning": [d for d in drills.get("conditioning", []) if d.get("new")]
    }
    return jsonify(new_drills)

