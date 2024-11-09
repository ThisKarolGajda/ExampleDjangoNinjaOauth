from ninja.errors import HttpError

class UnauthorizedException(HttpError):
    def __init__(self, message="Unauthorized"):
        super().__init__(status_code=401, message=message)
        self.message = message