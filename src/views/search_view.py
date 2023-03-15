from cerberus import Validator
from ..controller.search_controller import SearchController
from ..validators.validate_search import validate_search_user_request_body

class SearchRegisterView:
    def search_user_view(self, request):
        # Valida o body da requisição
        validation_response = validate_search_user_request_body(request.json)
        if not validation_response["is_valid"]:
            return {"status_code": 400, "data": {"error": validation_response["error"]}}
            
        # Extrai os valores do usuário pelo nome do body da requisição
        body = request.json
        name_user = body["name_user"]

        # Chama o controlador para criar o livro
        search_user_controler = SearchController()
        search_user = search_user_controler.search_user_by_name(name_user)

        # Retorna os resultados
        return {
            "status_code": 200,
            "data": {
                "user": [user.to_dict() for user in search_user]
            },
            "success": True
        }
