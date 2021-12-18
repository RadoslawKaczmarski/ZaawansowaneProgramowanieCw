from flask_restful import Resource
from CSV_READ.movies import read_csv_movies
from CSV_READ.links import read_csv_links
from CSV_READ.ratings import read_csv_ratings
from CSV_READ.tags import read_csv_tags


class HelloWorld(Resource):
    def get(self):
        return "Hi you are in 'Hello World'"


class Movies(Resource):
    def get(self):
        return read_csv_movies('data/movies.csv')


class Links(Resource):
    def get(self):
        return read_csv_links('data/links.csv')


class Ratings(Resource):
    def get(self):
        return read_csv_ratings('data/ratings.csv')


class Tags(Resource):
    def get(self):
        return read_csv_tags('data/tags.csv')


