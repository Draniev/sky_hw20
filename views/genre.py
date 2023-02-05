from flask_restx import Resource, Namespace
from container import genre_schema, genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    # Получение списка всех жанров
    def get(self):
        genres = genre_service.get_all()
        return genre_schema.dump(genres, many=True), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    # Получение жанра по ID
    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200
