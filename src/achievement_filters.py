def is_valid_product(product_data):
    return product_data['totalAchievements'] > 0 and product_data['totalProductXP'] >= 1000


def list_rarity_for_all_achievements(product_data):
    achievements = product_data['achievements']
    rarity_list = [e['achievement']['rarity']['percent'] for e in achievements]
    return rarity_list


def unlocks_achievements(product_data):
    rarity_list = list_rarity_for_all_achievements(product_data)
    return len(rarity_list) > 0 and max(rarity_list) > 0


def get_base_game_data(product_data):
    achievement_sets = product_data['achievementSets']
    base_sets = [e for e in achievement_sets if e['isBase']]
    game_data = base_sets[0]
    return game_data


def is_valid_base_game(game_data):
    return game_data['totalAchievements'] > 0 and game_data['totalXP'] == 1000


def tracks_players(game_data):
    return game_data['numProgressed'] > 0


def has_valid_achievements(product_data):
    product_flag = is_valid_product(product_data) and unlocks_achievements(product_data)

    game_data = get_base_game_data(product_data)
    game_flag = is_valid_base_game(game_data) and tracks_players(game_data)

    # NB: it seems to be sufficient to only check unlocks_achievements(), as can be observed with the assertion below:
    if unlocks_achievements(product_data):
        assert is_valid_product(product_data) and game_flag

    return product_flag and game_flag
