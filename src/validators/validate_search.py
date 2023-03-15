from cerberus import Validator
from ..error_handling.validation_error import ValidationError

def validate_search_user_request_body(request_body):
    search_by_name_schema = {
        "name_user": {"type": "string", "required": True, "empty": False},
    }
    # Valida o body da requisição
    validator = Validator(search_by_name_schema, allow_unknown=False)
    is_valid = validator.validate(request_body)

    if not is_valid:
        raise ValidationError({"message": "Invalid request body", "errors": validator.errors})

    return {
        "is_valid": is_valid,
        "error": validator.errors
    }
