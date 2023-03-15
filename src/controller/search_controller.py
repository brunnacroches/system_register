from ..infra.repository.register_repository import UsersRepository
from ..controller.register_controller import RegisterController

class SearchController(RegisterController):
    def __init__(self):
        self.db_repository = UsersRepository()

    def search_user_by_name(self, name_user:str):
        return self.db_repository.search_user_by_name(name_user)
