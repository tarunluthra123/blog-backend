import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "abc")
    DEBUG = os.environ.get("DEBUG") in ["True", "true", "1", 1]
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

    DB_URL = os.environ.get("DB_URL")
    DB_NAME = os.environ.get("POSTGRES_DB", "blogger")
    DB_USER = os.environ.get("POSTGRES_USER", "blogger")
    DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "blogger")
    DB_HOST = os.environ.get("POSTGRES_HOST", "localhost")
    DB_PORT = os.environ.get("POSTGRES_PORT", 5432)

    JWT_SECRET = os.environ.get("JWT_SECRET", "abcd")
    RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
