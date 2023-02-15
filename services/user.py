import hashlib
import time
import jwt

from dao.models.user import User
from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_SECRET_KEY


def get_hash(password):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),  # Convert the password to bytes
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ).decode("utf-8", "ignore")


def generate_jwt(user_data: dict) -> dict[str:str]:
    time_utc = int(time.time())
    time_30min = time_utc + 1800            # Добавляем 30 минут для текущего времени
    time_100d = time_utc + 3600 * 24 * 100  # Добавляем 100 дней для текущего времени

    user_data['exp'] = time_30min
    access_token = jwt.encode(user_data, JWT_SECRET_KEY, algorithm='HS256')
    user_data['exp'] = time_100d
    refresh_token = jwt.encode(user_data, JWT_SECRET_KEY, algorithm='HS256')

    return {'access_token': access_token, 'refresh_token': refresh_token}


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_one(self, uid: int) -> User | None:
        return self.user_dao.get_one(uid)

    def get_all(self) -> list[User]:
        return self.user_dao.get_all()

    def get_by_name(self, username: str) -> User | None:
        return self.user_dao.get_one_by_username(username)

    def create(self, user_data: dict) -> User:
        # На вход получаем пароль в открытом виде, но сохраняем хэш
        user_data['password'] = get_hash(user_data['password'])
        return self.user_dao.create(user_data)

    def update(self, user_data: User) -> User | None:
        user_id = user_data['id']
        user = self.user_dao.get_one(user_id)
        keys_4_update = user_data.keys()

        if user:
            if 'username' in keys_4_update:
                user.username = user_id['username']
            if 'password' in keys_4_update:
                # На вход получаем пароль в открытом виде, но сохраняем хэш
                user.password = get_hash(user_data['password'])
            if 'role' in keys_4_update:
                user.role = user_data['role']

            return self.user_dao.update(user)

        else:
            return None

    def delete(self, uid: int) -> User | None:
        return self.user_dao.delete(uid)
