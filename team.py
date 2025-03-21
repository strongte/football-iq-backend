# team.py
from flask import Blueprint, request, jsonify
import json
import os

team_routes = Blueprint('team_routes', __name__)

DATA_FILE = "team_data.json"

# Ensure the data file exists
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({"teams": []}, f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@team_routes.route('/', methods=['GET'])
def get_teams():
    data = load_data()
    return jsonify(data['teams'])

@team_routes.route('/<int:team_id>', methods=['GET'])
def get_team(team_id):
    data = load_data()
    for team in data['teams']:
        if team['id'] == team_id:
            return jsonify(team)
    return jsonify({"error": "Team not found"}), 404

@team_routes.route('/', methods=['POST'])
def add_team():
    data = load_data()
    new_team = request.json
    new_team['id'] = len(data['teams']) + 1
    new_team['players'] = new_team.get('players', [])
    new_team['coaches'] = new_team.get('coaches', [])
    data['teams'].append(new_team)
    save_data(data)
    return jsonify({"message": "Team added successfully", "team": new_team}), 201

@team_routes.route('/<int:team_id>/player', methods=['POST'])
def add_player(team_id):
    data = load_data()
    new_player = request.json
    for team in data['teams']:
        if team['id'] == team_id:
            new_player['id'] = len(team['players']) + 1
            team['players'].append(new_player)
            save_data(data)
            return jsonify({"message": "Player added successfully", "player": new_player}), 201
    return jsonify({"error": "Team not found"}), 404

