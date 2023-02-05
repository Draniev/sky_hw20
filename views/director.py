from flask_restx import Resource, Namespace
from container import director_service, director_schema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    # Получение всех режисcёров
    def get(self):
        directors = director_service.get_all()
        return director_schema.dump(directors, many=True), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    # Получение режисcёра по ID
    def get(self, did: int):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200
