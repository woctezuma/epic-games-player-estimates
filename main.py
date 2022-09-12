from src.data_filters import remove_broken_achievements, intersect_sandbox_ids
from src.data_utils import load_achievements, load_game_ratings, load_sandbox_ids_dict
from src.json_utils import save_json


def main():
    achievement_data = load_achievements()
    game_rating_data = load_game_ratings()
    sandbox_ids_dict = load_sandbox_ids_dict()

    achievement_data = remove_broken_achievements(achievement_data)

    sandbox_ids_for_tracker = {k: v for k, v in sandbox_ids_dict.items() if v in achievement_data}
    save_json(sandbox_ids_for_tracker, 'data/sandbox_ids_for_tracker.json')

    sandbox_ids = intersect_sandbox_ids(achievement_data, game_rating_data)

    trimmed_sandbox_ids = {k: v for k, v in sandbox_ids_dict.items() if v in sandbox_ids}
    save_json(trimmed_sandbox_ids, 'data/trimmed_sandbox_ids.json')

    return


if __name__ == '__main__':
    main()
