from flask import jsonify


class Response:
    def __init__(self, msg="", data=None):
        self.msg = msg
        self.data = data

    def dumps(self):
        return jsonify({"msg": self.msg, "data": self.data})
