import csv
from Class.Tags import Tags


def read_csv_tags(path):
    with open(path, errors="ignore") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_tags = []
        next(csv_reader)
        for row in csv_reader:
            tag = Tags(row[0], row[1], row[2], row[3])
            list_tags.append(Tags.return_api(tag))
    return list_tags
