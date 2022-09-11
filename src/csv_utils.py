def export_to_csv(data, fname, headers=[], fields=[]):
    with open(fname, "w", encoding="utf8") as f:
        if len(headers) > 0:
            line = ','.join(headers)
            f.write(f"{line}\n")
        for entry in data:
            line = ','.join(entry[k] for k in fields)
            f.write(f"{line}\n")
