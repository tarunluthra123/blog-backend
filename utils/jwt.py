import jwt

from blog.config import Config


def generate_token(payload):
    return jwt.encode(payload, Config.JWT_SECRET, algorithm="HS256")
