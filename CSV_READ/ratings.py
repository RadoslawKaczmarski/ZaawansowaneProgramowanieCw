import csv
from Class.Ratings import Ratings


def read_csv_ratings(path):
    with open(path, errors="ignore") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_ratings = []
        next(csv_reader)
        for row in csv_reader:
            rating = Ratings(row[0], row[1], row[2], row[3])
            list_ratings.append(Ratings.return_api(rating))
    return list_ratings
