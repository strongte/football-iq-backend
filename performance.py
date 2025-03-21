# performance.py
from flask import Blueprint, jsonify, request
import json
import os

PERF_FILE = "performance_data.json"
performance_routes = Blueprint('performance_routes', __name__)

# Ensure file exists
if not os.path.exists(PERF_FILE):
    with open(PERF_FILE, 'w') as f:
        json.dump({"results": []}, f)

# Load performance data
def load_data():
    with open(PERF_FILE, 'r') as f:
        return json.load(f)

# Save performance data
def save_data(data):
    with open(PERF_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@performance_routes.route('/performance', methods=['GET'])
def get_all_results():
    data = load_data()
    return jsonify(data['results'])

@performance_routes.route('/performance', methods=['POST'])
def add_result():
    new_entry = request.get_json()
    data = load_data()
    data['results'].append(new_entry)
    save_data(data)
    return jsonify({"message": "Result added", "status": "success"})

@performance_routes.route('/performance/<player_id>', methods=['GET'])
def get_player_results(player_id):
    data = load_data()
    results = [r for r in data['results'] if r.get("player_id") == player_id]
    return jsonify(results)

