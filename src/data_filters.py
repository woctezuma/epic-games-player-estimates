from src.achievement_filters import has_valid_achievements


def remove_broken_achievements(achievement_data, verbose=True):
    if verbose:
        print(f'#products = {len(achievement_data)} with achievements')

    filtered_data = {k: v for k, v in achievement_data.items() if has_valid_achievements(v)}

    if verbose:
        print(f'#products = {len(filtered_data)} with functional achievements')

    return filtered_data


def intersect_sandbox_ids(achievement_data, game_rating_data, verbose=True):
    sandbox_ids = set(achievement_data.keys()).intersection(game_rating_data.keys())
    if verbose:
        print(f'#products = {len(sandbox_ids)} after intersection with ratings')

    return sandbox_ids
