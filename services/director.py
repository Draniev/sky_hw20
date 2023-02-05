from dao.models.director import Director
from dao.universal_entity import UniversalDAO


class DirectorService:
    def __init__(self, director_dao: UniversalDAO):
        self.director_dao = director_dao

    def get_one(self, did: int) -> Director:
        return self.director_dao.get_one(did)

    def get_all(self) -> list[Director]:
        return self.director_dao.get_all()
