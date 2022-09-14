from src.data_filters import remove_broken_achievements, intersect_sandbox_ids
from src.data_utils import load_achievements, load_game_ratings, load_sandbox_ids_dict


def main():
    achievement_data = load_achievements()
    game_rating_data = load_game_ratings()
    sandbox_ids_dict = load_sandbox_ids_dict()

    achievement_data = remove_broken_achievements(achievement_data)

    achievement_data = intersect_sandbox_ids(achievement_data, game_rating_data)

    return


if __name__ == '__main__':
    main()
