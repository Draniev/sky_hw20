import hashlib

from dao.models.user import User
from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


def get_hash(password):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),  # Convert the password to bytes
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ).decode("utf-8", "ignore")


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
