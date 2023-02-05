from flask_sqlalchemy import SQLAlchemy
from dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session: SQLAlchemy().session):
        self.session = session

    def get_one(self, mid: int) -> Movie | None:
        return self.session.query(Movie).get(mid)

    def get_all(self, filter_args: dict | None) -> list[Movie]:
        match filter_args:
            case {'director_id': director_id, 'genre_id': genre_id}:
                movies = self.session.query(Movie) \
                    .filter(Movie.director_id == director_id) \
                    .filter(Movie.genre_id == genre_id) \
                    .all()
            case {'director_id': director_id}:
                movies = self.session.query(Movie).filter(Movie.director_id == director_id).all()
            case {'genre_id': genre_id}:
                movies = self.session.query(Movie).filter(Movie.genre_id == genre_id).all()
            case {'year': year}:
                movies = self.session.query(Movie).filter(Movie.year == year).all()
            case _:
                movies = self.session.query(Movie).all()
        return movies

    def create(self, movie_data) -> Movie:
        movie = Movie(**movie_data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie: Movie) -> Movie:
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid: int) -> Movie | None:
        movie = self.get_one(mid)
        if movie:
            self.session.delete(movie)
            self.session.commit()
            return movie
        else:
            return None
