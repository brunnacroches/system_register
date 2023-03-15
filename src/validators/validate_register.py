from cerberus import Validator
from ..error_handling.validation_error import ValidationError

def validate_register_user_request_body(request_body):
# Define o esquema de validação
    schema = {
        "name_user": {"type": "string", "required": True},
        "birth_date": {"type": "string", "required": True, "regex": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"}, 
        "street": {"type": "string", "required": True},
        "profession": {"type": "string", "required": True},
    }

    # Valida o body da requisição
    validator = Validator(schema)
    is_valid = validator.validate(request_body)

    if not is_valid:
        raise ValidationError({"message": "Invalid request body", "errors": validator.errors})

    return {
        "is_valid": is_valid,
        "error": validator.errors
    }
