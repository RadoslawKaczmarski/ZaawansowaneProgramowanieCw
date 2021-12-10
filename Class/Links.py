class Links:
    def __init__(self, movieid: int, imdbld: int, tmdbld: int) -> None:
        self.movieid = movieid
        self.imdbld = imdbld
        self.tmdbld = tmdbld

    def return_api(self) -> dict:
        return {"ID": self.movieid,
                "Tytul": self.imdbld,
                "Geners": self.tmdbld}
