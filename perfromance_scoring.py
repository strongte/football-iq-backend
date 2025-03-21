# performance_scoring.py

def score_player(player):
    """
    Accepts a player dict with raw metrics and returns a performance index score (1–100).
    We use basic thresholds based on youth athlete averages.
    """
    weights = {
        "40_time": -5.0,  # Lower is better
        "vertical_jump": 2.5,
        "long_jump": 2.0,
        "cone_agility": -4.0,  # Lower is better
        "seated_med_ball_throw": 3.0
    }

    base_score = 50
    total = base_score

    if "40_time" in player:
        total += weights["40_time"] * (6.0 - player["40_time"])

    if "vertical_jump" in player:
        total += weights["vertical_jump"] * (player["vertical_jump"] - 16)

    if "long_jump" in player:
        total += weights["long_jump"] * (player["long_jump"] - 6.0)

    if "cone_agility" in player:
        total += weights["cone_agility"] * (6.0 - player["cone_agility"])

    if "seated_med_ball_throw" in player:
        total += weights["seated_med_ball_throw"] * (player["seated_med_ball_throw"] - 15)

    return max(0, min(100, round(total)))

