from ctpbee import CtpbeeApi, CtpBee
from ctpbee.constant import *
from ctpbee_webline import WebLine


class Line(CtpbeeApi):
    def __init__(self, name):
        super().__init__(name)
        self.init = False

    def on_tick(self, tick: TickData) -> None:
        pass

    def on_position(self, position: PositionData) -> None:
        pass

    def on_contract(self, contract: ContractData):
        if contract.symbol == "rb2405":
            self.action.subscribe(contract.local_symbol)

    def on_init(self, init: bool):
        self.info("账户初始化成功回报")
        self.init = True


if __name__ == '__main__':
    web_line = WebLine()
    app = CtpBee("market", __name__, refresh=True).with_tools(web_line)
    example = Line("DailyCTA")
    app.add_extension(example)
    app.config.from_json("config.json")
    app.start(log_output=True)
