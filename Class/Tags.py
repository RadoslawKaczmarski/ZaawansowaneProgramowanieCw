class Tags:
    def __init__(self, userid: int, movieid: int, tag: str, timestamp:int) -> None:
        self.userid = userid
        self.movieid = movieid
        self.tag = tag
        self.timestamp = timestamp

    def return_api(self) -> dict:
        return {"User ID": self.userid,
                "Movie ID": self.movieid,
                "Tag": self.tag,
                "Timestamp": self.timestamp}
