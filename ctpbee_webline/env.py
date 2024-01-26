import random

SQLALCHEMY_DATABASE_URI = "sqlite:///web_line.db"

SECRET_KEY = random.sample("abcdefghijklmnopqrstuvwxyz.@%^#", 30)
