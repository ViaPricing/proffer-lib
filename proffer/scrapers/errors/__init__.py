class CustomError(Exception):
    """Base class for other exceptions"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class EmptyResponseError(CustomError):
    """Raised when the response is empty"""


class AuthorizationDenied(CustomError):
    """Raised when the user is not authorized to access a resource"""

class ProxyError(CustomError):
    """Raised when a proxy error occurs"""

