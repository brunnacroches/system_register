# Importando as bibliotecas necessárias
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
     # Método construtor da classe
    def __init__(self) -> None:
        # Definindo a string de conexão com o banco de dados
        self.__connection_string = 'mysql+pymysql://root:spacedatabase@localhost:3306/system_register'
        # Criando o objeto 'engine' do SQLAlchemy 
        self.__engine = self.__create_database_engine()
        self.session = None

    # Método para criar o objeto 'engine' do SQLAlchemy
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    # Método para retornar o objeto 'engine' criado
    def get_engine(self):
        return self.__engine

    # Método especial __enter__ é chamado ao entrar em um bloco 'with'
    def __enter__(self):
        # Criando uma instância de sessionmaker vinculada ao 'engine
        session_make = sessionmaker(bind=self.__engine)
        # Criando uma sessão e atribuindo ao atributo 'session'
        self.session = session_make()
        return self

    # Método especial __exit__ é chamado ao sair do bloco 'with'
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Fechando a sessão atual
        self.session.close()