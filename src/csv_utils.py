def to_csv_row(values):
    return ','.join(str(v) for v in values)


def write_as_csv_row(values, f):
    line = to_csv_row(values)
    if len(line) > 0:
        f.write(f"{line}\n")
    return


def export_to_csv(data, fname, headers=[], fields=[]):
    with open(fname, "w", encoding="utf8") as f:
        write_as_csv_row(headers, f)
        for entry in data:
            values = [entry[k] for k in fields]
            write_as_csv_row(values, f)
