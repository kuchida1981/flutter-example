import os


class base:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class development(base):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

class production(base):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
