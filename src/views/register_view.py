from cerberus import Validator
from ..controller.register_controller import RegisterController
from ..validators.validate_register import validate_register_user_request_body
from ..error_handling.validation_error import ValidationError

class RegisterView:
    def register_user_view(self, request):
        # Valida o body da requisição
        try:
            validation_response = validate_register_user_request_body(request.json)
        except ValidationError as e:
            return {"status_code": 400, "data": e.message}

        # Extrai os valores do livro do body da requisição
        body = request.json
        name_user =  body["name_user"]
        birth_date = body["birth_date"]
        street = body["street"]
        profession = body["profession"]

        # Chama o controlador para criar o livro
        register_user_controler = RegisterController()
        register_user_controler.register_user(name_user, birth_date, street, profession)

        # Retorna os resultados
        return {
            "status_code": 200,
            "data": {
                "name_user": name_user,
                "birth_date": birth_date,
                "street": street,
                "profession": profession
            },
            "success": True
        }
