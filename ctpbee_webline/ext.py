from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

model = SQLAlchemy()
jwt = JWTManager()
socketio = SocketIO(cors_allowed_origins="*")
