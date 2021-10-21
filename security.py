from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authentiate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """takes in payload (contents of jwt) extract id from payload, retrieve specific user"""
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)