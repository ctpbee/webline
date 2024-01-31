from flask import jsonify


class Response:
    def __init__(
        self,
        data=None,
        message="",
        success=True,
        code=200,
    ):
        self.message = message
        self.data = data
        self.code = code
        self.success = success

    def dumps(self):
        return jsonify(
            {
                "message": self.message,
                "data": self.data,
                "code": self.code,
                "success": self.success,
            }
        )


class Success(Response):
    def __init__(
        self,
        data=None,
        message="",
        code=200,
    ):
        super().__init__(
            data=data,
            message=message,
            code=code,
            success=True,
        )


class Fail(Response):
    def __init__(self, data=None, message="", code=400):
        super().__init__(
            data=data,
            message=message,
            code=code,
            success=False,
        )
