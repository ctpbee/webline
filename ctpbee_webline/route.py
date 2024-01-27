from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, unset_jwt_cookies
from ctpbee import current_app
from ctpbee import dumps
from ctpbee.constant import OrderRequest, CancelRequest
from ctpbee_webline.response import Response
from ctpbee_webline.model import Admin
from ctpbee_webline.ext import model

web = Blueprint("web_line", __name__, url_prefix="/web")


@web.route("/contracts")
@jwt_required()
def find_contracts():
    """
    访问所有合约信息
    """
    contracts = dumps(current_app.recorder.get_all_contracts())
    return Response(data=contracts).dumps()


@web.route("/ticks")
@jwt_required()
def find_ticks():
    """
    访问一次行情
    """
    ticks = dumps(current_app.recorder.ticks)
    return Response(data=ticks).dumps()


@web.route("/orders")
@jwt_required()
def find_orders():
    """
    查询所有订单
    :return:
    """
    orders = dumps(current_app.center.orders)
    return Response(data=orders).dumps()


@web.route("/active_orders")
@jwt_required()
def find_active_orders():
    """
    查询活跃订单
    :return:
    """
    orders = dumps(current_app.recorder.active_orders)
    return Response(data=orders).dumps()


@web.route("/send")
@jwt_required()
def send_web_order():
    req = OrderRequest(**request.values)
    current_app.send_order(req)


@web.route("/cancel")
@jwt_required()
def cancel_web_order():
    try:
        req = CancelRequest(**request.values)
        current_app.cancel_order(req)
        return Response("cancel ok").dumps()
    except Exception as e:
        return Response(msg=str(e)).dumps()


@web.route("/login", methods=["POST"])
def login():
    username = request.values.get("username")
    password = request.values.get("password")
    if username is None or password is None:
        return Response(msg="请确认用户名或者密码不为空").dumps()
    admin = Admin.query.filter(Admin.username == username, Admin.pwd == password).first()
    if admin:
        token = create_access_token(admin.username)
        return Response(msg="登录成功", data={"token": token}).dumps()
    else:
        return Response(msg="请确认用户存在或者密码正确").dumps()


@web.route("/change_password", methods=["POST"])
@jwt_required()
def change_password():
    username = request.values.get("username")
    password = request.values.get("password")
    if username is None or password is None:
        return Response(msg="请确认用户名或者密码不为空").dumps()
    admin = Admin.query.filter(Admin.username == username).first()
    if admin:
        admin.pwd = password
        model.session.add(admin)
        model.session.commit()
        return Response(msg="登录成功", data={"token": create_access_token(admin.username)}).dumps()
    else:
        return Response(msg="请确认用户存在或者密码正确").dumps()


@web.route("/logout")
@jwt_required()
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return Response(msg="注销成功").dumps()
