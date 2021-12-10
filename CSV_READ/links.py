import csv
from Class.Links import Links


def read_csv_links(path):
    with open(path, errors="ignore") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_links = []
        next(csv_reader)
        for row in csv_reader:
            link = Links(row[0], row[1], row[2])
            list_links.append(Links.return_api(link))
    return list_links
