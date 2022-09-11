from src.json_utils import load_json

DATA_FOLDER_NAME = 'data'
ACHIEVEMENT_FNAME = 'achievements.json'
GAME_RATING_FNAME = 'game_ratings.json'


def load_achievements():
    return load_json(f"{DATA_FOLDER_NAME}/{ACHIEVEMENT_FNAME}")


def load_game_ratings():
    return load_json(f"{DATA_FOLDER_NAME}/{GAME_RATING_FNAME}")
