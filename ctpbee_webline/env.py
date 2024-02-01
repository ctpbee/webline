from datetime import timedelta

SQLALCHEMY_DATABASE_URI = "sqlite:///web_line.db"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=999)  # Set expire time to 30 minutes
