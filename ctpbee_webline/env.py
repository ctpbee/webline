import random

SQLALCHEMY_DATABASE_URI = "sqlite:///web_line.db"
SECRET_KEY = "".join(random.sample("abcdefghijklmnopqrstuvwxyz.@%^#", 30))
JWT_SECRET_KEY = "".join(random.sample("abcdefghijklmnopqrstuvwxyz.@%^#", 30))
