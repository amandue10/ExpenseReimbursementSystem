class FailedLogin(Exception):
    def __init__(self, message: str):
        self.message = message


class NoNegativeValues(Exception):
    def __init__(self, message: str):
        self.message = message


class NoNonNumericValues(Exception):
    def __init__(self, message: str):
        self.message = message
