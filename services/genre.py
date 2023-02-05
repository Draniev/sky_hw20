from dao.models.genre import Genre
from dao.universal_entity import UniversalDAO


class GenreService:
    def __init__(self, genre_dao: UniversalDAO):
        self.genre_dao = genre_dao

    def get_one(self, gid) -> Genre:
        return self.genre_dao.get_one(gid)

    def get_all(self) -> list[Genre]:
        return self.genre_dao.get_all()

