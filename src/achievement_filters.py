def list_rarity_for_all_achievements(product_data):
    achievements = product_data['achievements']
    rarity_list = [e['achievement']['rarity']['percent'] for e in achievements]
    return rarity_list


def unlocks_achievements(product_data):
    rarity_list = list_rarity_for_all_achievements(product_data)
    return len(rarity_list) > 0 and max(rarity_list) > 0


def has_valid_achievements(product_data):
    return unlocks_achievements(product_data)
