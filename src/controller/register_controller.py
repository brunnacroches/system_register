from ..infra.repository.register_repository import UsersRepository


class RegisterController:
    def __init__(self):
        self.db_repository = UsersRepository()

    def register_user(self, name_user:str, birth_date:int, street:str, profession:str):
        self.db_repository.insert(name_user, birth_date, street, profession)