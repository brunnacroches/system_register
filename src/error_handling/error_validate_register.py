from ..validators.validate_register import validate_register_user_request_body

class ValidationError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.message = message
        self.errors = errors
