class Movies:
    def __init__(self, movieid: int, title: str, genres: str) -> None:
        self.movieid = movieid
        self.title = title
        self.genres = genres

    def return_api(self) -> dict:
        return {"ID": self.movieid,
                "Tytul": self.title,
                "Geners": self.genres}
