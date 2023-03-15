from cerberus import Validator

def validate_search_user_request_body(request_body):
    search_by_name_schema = {
        "name_user": {"type": "string", "required": True, "empty": False},
    }
    # Valida o body da requisição
    validator = Validator(search_by_name_schema)
    is_valid = validator.validate(request_body)

    validation_response = {
        "is_valid": is_valid,
        "error": validator.errors
    }
    
    return validation_response
