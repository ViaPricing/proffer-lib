class EmptyResponseError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class AuthorizationDenied(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NetworkError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
