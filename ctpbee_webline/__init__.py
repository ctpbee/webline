import warnings
from threading import Thread

from flask import Flask
from flask_cors import CORS
from ctpbee import Tool, dumps
from ctpbee.constant import ToolRegisterType, TickData, AccountData, OrderData, TradeData
from ctpbee.level import tool_register
from ctpbee_webline.route import web
from ctpbee_webline.ext import model, jwt, socketio


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(blueprint=web)
    app.config.from_pyfile("env.py")
    model.init_app(app)
    jwt.init_app(app)
    socketio.init_app(app)
    return app


class WebLine(Tool):
    def __init__(self, local=False, port=7960, secret_key: str = "secret_key", jwt_secret_key="jwt_secret_key"):
        """
        :param local:判断以何种方式启动
        :param port: 端口
        :param secret_key: FLASK_SECRET_KEY
        :param jwt_secret_key: JWT_SECRET_KEY
        """
        super().__init__("web_line")
        self.local = local
        self.port = port
        if secret_key == "secret_key":
            warnings.warn("当前secret_key为默认值, 为了安全着想, 请传入secret_key覆盖默认值")
        if jwt_secret_key == "jwt_secret_key":
            warnings.warn("当前jwt_secret_key为默认值, 为了安全着想, 请传入jwt_secret_key覆盖默认值")
        self.secret_key = secret_key
        self.jwt_secret_key = jwt_secret_key
        self.thread = Thread(target=self.run, daemon=True)
        self.thread.start()

    def run(self):
        app = create_app()
        app.config["SECRET_KEY"] = self.secret_key
        app.config["JWT_SECRET_KEY"] = self.jwt_secret_key
        host = "127.0.0.1" if self.local else "0.0.0.0"
        socketio.run(app, host, self.port, allow_unsafe_werkzeug=True)

    @tool_register(ToolRegisterType.TICK)
    def on_tick(self, tick: TickData):
        socketio.emit("tick", dumps(tick))

    @tool_register(ToolRegisterType.ACCOUNT)
    def on_account(self, account: AccountData):
        socketio.emit("account", dumps(account))

    @tool_register(ToolRegisterType.ORDER)
    def on_order(self, order: OrderData):
        socketio.emit("order", dumps(order))

    @tool_register(ToolRegisterType.TRADE)
    def on_trade(self, trade: TradeData):
        socketio.emit("trade", dumps(trade))
