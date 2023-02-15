from dao.models.genre import Genre
from dao.universal_entity import UniversalDAO


class GenreService:
    def __init__(self, genre_dao: UniversalDAO):
        self.genre_dao = genre_dao

    def get_one(self, gid) -> Genre:
        return self.genre_dao.get_one(gid)

    def get_all(self) -> list[Genre]:
        return self.genre_dao.get_all()

    def create(self, genre_data: dict) -> Genre:
        return self.genre_dao.create(genre_data)

    def update(self, genre_data: dict) -> Genre:
        genre = self.genre_dao.get_one(genre_data['id'])
        keys_4_update = genre_data.keys()

        if 'name' in keys_4_update:
            genre.name = genre_data['name']

        return self.genre_dao.update(genre)

    def delete(self, gid: int) -> Genre:
        return self.genre_dao.delete(gid)
