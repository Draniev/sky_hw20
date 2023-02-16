from flask import request
from flask_restx import Resource, Namespace
from container import genre_schema, genre_service
from utils import admin_required, auth_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    # Получение списка всех жанров
    @auth_required
    def get(self):
        genres = genre_service.get_all()
        return genre_schema.dump(genres, many=True), 200

    @admin_required
    def post(self):
        genre_data = request.json
        genre = genre_service.create(genre_data)
        return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    # Получение жанра по ID
    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200

    # Изменение одного
    @admin_required
    def put(self, gid):
        genre_data = request.json
        genre_data['id'] = gid
        genre = genre_service.update(genre_data)
        if genre:
            return "", 200
        else:
            return "Нечего тут обновлять!", 404

    # Удаление
    @admin_required
    def delete(self, gid):
        genre = genre_service.delete(gid)
        if genre:
            return "", 204
        else:
            return "Тут и так пусто", 404