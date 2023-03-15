import unittest
from ..controller.search_controller import SearchController

class TestSearchController(unittest.TestCase):
    def setUp(self):
        self.search_controller = SearchController()
        
    def tearDown(self):
        # Limpe todas as entradas do banco de dados aqui, se necessário
        pass
    
    def test_search_user_by_name(self):
        # Chamando o método search_user_by_name com o nome do usuário existente no banco de dados
        user_record = self.search_controller.search_user_by_name('John Doe')
        # Assegurando que o usuário retornado corresponde aos resultados esperados
        expected_result = {'name': 'John Doe', 'birth_date': 1990, 'street': '123 Main St', 'profession': 'Engineer'}
        self.assertDictEqual(user_record, expected_result)
        
    def test_register_user(self):
        # Inserindo um novo registro de usuário
        self.search_controller.register_user('Jane Smith', 1985, '456 Elm St', 'Doctor')
        # Recuperar o usuário do banco de dados e afirme que ele corresponde ao registro inserido
        user_record = self.search_controller.search_user_by_name('Jane Smith')
        expected_result = {'name': 'Jane Smith', 'birth_date': 1985, 'street': '456 Elm St', 'profession': 'Doctor'}
        self.assertDictEqual(user_record, expected_result)
