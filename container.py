from dao.models.director import DirectorSchema, Director
from dao.models.genre import GenreSchema, Genre
from dao.models.movie import MovieSchema, Movie
from dao.universal_entity import UniversalDAO
from services.director import DirectorService
from services.genre import GenreService
from services.movie import MovieService
from setup_db import db
from dao.movie import MovieDAO
from dao.director import DirectorDAO
from dao.genre import GenreDAO


# genre_dao = GenreDAO(db.session)
# director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)    # т.к. тут еще фильтрацию надо, то 'экспериментальный' пока брать не будем

# Тут использую экспериментальный ДАО объект.
# Если уж нет разницы в запросах из БД,
# так что решил и два разных класса не делать
genre_dao = UniversalDAO(db.session, Genre)
director_dao = UniversalDAO(db.session, Director)
# movie_dao = UniversalDAO(db.session, Movie)

genre_service = GenreService(genre_dao)
director_service = DirectorService(director_dao)
movie_service = MovieService(movie_dao)


genre_schema = GenreSchema()
director_schema = DirectorSchema()
movie_schema = MovieSchema()

