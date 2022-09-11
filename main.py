from src.achievement_filters import has_valid_achievements
from src.data_utils import load_achievements, load_game_ratings, load_sandbox_ids_dict
from src.json_utils import save_json


def intersect_sandbox_ids(achievement_data, game_rating_data):
    sandbox_ids = set(achievement_data.keys())
    print(len(sandbox_ids))

    sandbox_ids = [id for id in sandbox_ids if has_valid_achievements(achievement_data[id])]
    print(len(sandbox_ids))

    sandbox_ids = set(sandbox_ids).intersection(game_rating_data.keys())
    print(len(sandbox_ids))

    return sandbox_ids


def main():
    achievement_data = load_achievements()
    game_rating_data = load_game_ratings()
    sandbox_ids_dict = load_sandbox_ids_dict()

    sandbox_ids = intersect_sandbox_ids(achievement_data, game_rating_data)

    trimmed_sandbox_ids = {k: v for k, v in sandbox_ids_dict.items() if v in sandbox_ids}
    save_json(trimmed_sandbox_ids, 'data/trimmed_sandbox_ids.json')

    return


if __name__ == '__main__':
    main()
