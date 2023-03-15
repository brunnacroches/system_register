from src.infra.configs.connection import DBConnectionHandler
from src.infra.entities.register_user import Users

class UsersRepository:
    def select(self):
        with DBConnectionHandler() as db: # acessando tudo que tem dentro do DBConnectionHandler
            data = db.session.query(Users).all()
            return data # esse retorno ajuda a pegar tudo que tem dentro do self do DBConnectionHandler

    # fechar a classe
    def insert(self, name_user: str, birth_date, profession: str, street: str):
        with DBConnectionHandler() as db:
            data_insert = Users(
                name_user=name_user,
                birth_date=birth_date,
                profession=profession,
                street=street,
            )
            db.session.add(data_insert)
            db.session.commit()
            # elemento para criar elementos em si

    def delete(self, name_user):
        with DBConnectionHandler() as db:
            db.session.query(Users).filter(Users.name_user == name_user).delete()
            db.session.commit()

    def update(self, name_user, profession):
        with DBConnectionHandler() as db:
            db.session.query(Users).filter(Users.name_user == name_user).update({"profession": 'Programmer'})
            db.session.commit()

    def search_user_by_name(self, name_user:str):
        with DBConnectionHandler() as db:
            result = db.session.query(Users).filter_by(name_user=name_user).all()
        return result
