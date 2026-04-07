class Response:
    def __init__(self, success: bool, message: str, data=None):
        self.success = success
        self.message = message
        self.data = data

    @staticmethod
    def ok(data=None, message="OK"):
        return Response(True, message, data)

    @staticmethod
    def fail(message="ERROR"):
        return Response(False, message, None)