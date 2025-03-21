# rules.py
from flask import Blueprint, jsonify
import json
import os

RULES_FILE = "rules_and_officiating.json"
rules_routes = Blueprint('rules_routes', __name__)

# Load or create rule content
def load_rules():
    if not os.path.exists(RULES_FILE):
        with open(RULES_FILE, 'w') as f:
            json.dump({"rules": []}, f)
    with open(RULES_FILE, 'r') as f:
        return json.load(f)

@rules_routes.route('/rules', methods=['GET'])
def get_rules():
    rules = load_rules()
    return jsonify(rules['rules'])

@rules_routes.route('/rules/new', methods=['GET'])
def get_new_rules():
    rules = load_rules()
    new_items = [r for r in rules['rules'] if r.get("new")]
    return jsonify(new_items)

