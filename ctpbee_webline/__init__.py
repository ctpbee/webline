from threading import Thread

from flask import Flask
from ctpbee import Tool
from ctpbee.constant import ToolRegisterType, TickData, AccountData, OrderData, TradeData
from ctpbee.level import tool_register
from ctpbee_webline.route import web
from ctpbee_webline.ext import model, jwt


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=web)
    app.config.from_pyfile("env.py")
    model.init_app(app)
    jwt.init_app(app)
    return app


class WebLine(Tool):
    def __init__(self, local=False, port=7960):
        super().__init__("web_line")
        self.local = local
        self.port = port
        self.flask_app = create_app()
        self.thread = Thread(target=self.run, daemon=True)
        self.thread.start()

    def run(self):
        host = "127.0.0.1" if self.local else "0.0.0.0"
        self.flask_app.run(host=host, port=self.port)

    @tool_register(ToolRegisterType.TICK)
    def on_tick(self, tick: TickData):
        pass

    @tool_register(ToolRegisterType.ACCOUNT)
    def on_account(self, account: AccountData):
        pass

    @tool_register(ToolRegisterType.ORDER)
    def on_order(self, order: OrderData):
        pass

    @tool_register(ToolRegisterType.TRADE)
    def on_trade(self, trade: TradeData):
        pass
