class CustomError(Exception):
    """Base class for other exceptions"""
    pass

class EmptyResponseError(CustomError):
    """Raised when the response is empty"""


class AuthorizationDenied(CustomError):
    """Raised when the user is not authorized to access a resource"""

