from ctpbee.constant import OrderRequest, CancelRequest
from flask import Blueprint, request

from ctpbee import current_app
from ctpbee import dumps

from ctpbee_webline.response import Response

web = Blueprint("web_line", __name__, url_prefix="/web")


@web.route("/contracts")
def find_contracts():
    """
    访问所有合约信息
    """
    contracts = dumps(current_app.recorder.get_all_contracts())
    return Response(data=contracts).dumps()


@web.route("/ticks")
def find_ticks():
    """
    访问一次行情
    """
    ticks = dumps(current_app.recorder.ticks)
    return Response(data=ticks).dumps()


@web.route("/orders")
def find_orders():
    """
    查询所有订单
    :return:
    """
    orders = dumps(current_app.center.orders)
    return Response(data=orders).dumps()


@web.route("/active_orders")
def find_active_orders():
    """
    查询活跃订单
    :return:
    """
    orders = dumps(current_app.recorder.active_orders)
    return Response(data=orders).dumps()


@web.route("/send")
def send_web_order():
    req = OrderRequest(**request.values)
    current_app.send_order(req)


@web.route("/cancel")
def cancel_web_order():
    try:
        req = CancelRequest(**request.values)
        current_app.cancel_order(req)
        return Response("cancel ok").dumps()
    except Exception as e:
        return Response(msg=str(e)).dumps()
