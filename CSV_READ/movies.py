import csv
from Class.Movies import Movies


def read_csv_movies(path):
    with open(path, errors="ignore") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_movie = []
        next(csv_reader)
        for row in csv_reader:
            movie = Movies(row[0], row[1], row[2])
            list_movie.append(Movies.return_api(movie))
    return list_movie
