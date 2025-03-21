# main.py
from flask import Flask
from team import team_routes
from drills import drill_routes
from coach import coach_routes
from rules import rules_routes

app = Flask(__name__)

# Register route blueprints
app.register_blueprint(team_routes, url_prefix="/teams")
app.register_blueprint(drill_routes, url_prefix="/drills")
app.register_blueprint(coach_routes, url_prefix="/coach")
app.register_blueprint(rules_routes, url_prefix="/coach")

@app.route("/")
def index():
    return {"message": "Football IQ backend is running!", "status": "success"}

if __name__ == "__main__":
    app.run(debug=True)
