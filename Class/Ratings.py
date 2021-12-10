class Ratings:
    def __init__(self, userid: int, movieid: int, rating: str, timestamp:int) -> None:
        self.userid = userid
        self.movieid = movieid
        self.rating = rating
        self.timestamp = timestamp

    def return_api(self) -> dict:
        return {"User ID": self.userid,
                "Movie ID": self.movieid,
                "Tag": self.rating,
                "Timestamp": self.timestamp}
