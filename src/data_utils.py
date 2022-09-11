from src.json_utils import load_json

DATA_FOLDER_NAME = 'data'
ACHIEVEMENT_FNAME = 'achievements.json'
GAME_RATING_FNAME = 'game_ratings.json'
SANDBOX_IDS_FNAME = 'sandbox_ids.json'


def load_achievements():
    return load_json(f"{DATA_FOLDER_NAME}/{ACHIEVEMENT_FNAME}")


def load_game_ratings():
    return load_json(f"{DATA_FOLDER_NAME}/{GAME_RATING_FNAME}")


def load_sandbox_ids_dict():
    return load_json(f"{DATA_FOLDER_NAME}/{SANDBOX_IDS_FNAME}")
