from flask import Blueprint

from ctpbee import current_app
from ctpbee import send_order, cancel_order

web = Blueprint("web_line", __name__, url_prefix="/web")


@web.route("/contracts")
def find_contracts():
    contract = current_app.recorder.get_all_contracts()
    return contract


@web.route("/orders")
def find_orders():
    orders = current_app.center.orders
    return orders


@web.route("/active_orders")
def find_active_orders():
    orders = current_app.recorder.active_orders
    return orders


@web.route("/send")
def send_web_order():
    pass


@web.route("/cancel")
def cancel_web_order():
    pass
