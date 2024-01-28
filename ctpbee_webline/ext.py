from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

model = SQLAlchemy()
jwt = JWTManager()
socketio = SocketIO()
