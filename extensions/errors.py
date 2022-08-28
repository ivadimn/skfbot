class DataError(Exception):

    def __init__(self, msg: str):
        super().__init__(msg)
        self.msg = msg


class NotCurrencyError(Exception):

    def __init__(self, msg: str):
        super().__init__(msg)
        self.msg = msg


class AmbiguousCurrencyError(Exception):

    def __init__(self, msg: str):
        super().__init__(msg)
        self.msg = msg