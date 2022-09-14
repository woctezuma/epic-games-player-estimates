import json


def load_json(fname):
    with open(fname, 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


def save_json(data, fname, prettify=True):
    with open(fname, 'w', encoding='utf8') as f:
        if prettify:
            json.dump(data, f, indent=4, sort_keys=True)
        else:
            json.dump(data, f)
