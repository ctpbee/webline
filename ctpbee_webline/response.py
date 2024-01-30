from flask import jsonify


class Response:
    def __init__(self, msg="", data=None):
        self.msg = msg
        self.data = data
        self.status = 200

    def dumps(self):
        return jsonify({"msg": self.msg, "data": self.data, "status": self.status})
