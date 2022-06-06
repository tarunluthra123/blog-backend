import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "abc")
    DEBUG = os.environ.get("DEBUG") in ["True", "true", "1", 1]
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

    DB_NAME = os.environ.get("DB_NAME", "blogger")
    DB_USER = os.environ.get("DB_USER", "blogger")
    DB_PASSWORD = os.environ.get("DB_PASS", "blogger")
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", 3306)

    JWT_SECRET = os.environ.get("JWT_SECRET", "abcd")
