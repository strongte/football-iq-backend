from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
DATA_FILE = "football_data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"teams": [], "practices": [], "plays": []}, f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(load_data())

@app.route("/add-team", methods=["POST"])
def add_team():
    data = load_data()
    new_team = request.json
    data["teams"].append(new_team)
    save_data(data)
    return jsonify({"message": "Team added!", "team": new_team})

@app.route("/add-practice", methods=["POST"])
def add_practice():
    data = load_data()
    new_practice = request.json
    data["practices"].append(new_practice)
    save_data(data)
    return jsonify({"message": "Practice added!", "practice": new_practice})

@app.route("/add-play", methods=["POST"])
def add_play():
    data = load_data()
    new_play = request.json
    data["plays"].append(new_play)
    save_data(data)
    return jsonify({"message": "Play added!", "play": new_play})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
