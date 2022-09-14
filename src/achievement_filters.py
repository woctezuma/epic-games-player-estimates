def list_all_unlock_percentages(achievement_data):
    return [e['achievement']['rarity']['percent'] for e in achievement_data['achievements']]


def has_valid_achievements(product_data):
    rarity_list = list_all_unlock_percentages(product_data)
    return len(rarity_list) > 0 and max(rarity_list) > 0
