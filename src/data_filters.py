from src.achievement_filters import has_valid_achievements


def remove_broken_achievements(achievement_data, verbose=True):
    if verbose:
        print(f'#products = {len(achievement_data)} with achievements')

    filtered_data = {k: v for k, v in achievement_data.items() if has_valid_achievements(v)}

    if verbose:
        print(f'#products = {len(filtered_data)} with functional achievements')

    return filtered_data


def intersect_sandbox_ids(achievement_data, game_rating_data, verbose=True):
    filtered_data = {k: v for k, v in achievement_data.items() if k in game_rating_data}
    if verbose:
        print(f'#products = {len(filtered_data)} after intersection with ratings')

    return filtered_data
