from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.controller.register_controller import RegisterController
from src.infra.repository.register_repository import UsersRepository

class TestRegisterController(TestCase):

    @patch('src.controller.register_controller.UsersRepository')
    def test_register_user(self, mock_users_repo):
        # Arrange
        controller = RegisterController()
        mock_instance = mock_users_repo.return_value
        mock_instance.insert.return_value = 1

        # Act
        result = controller.register_user(
            name_user='Test',
            birth_date=946684800,  # Unix timestamp for 2000-01-01
            street='123 Main St.',
            profession='Developer')

        # Assert
        self.assertEqual(result, 1)
        mock_instance.insert.assert_called_once_with(
            name_user='Test',
            birth_date=946684800,
            street='123 Main St.',
            profession='Developer')
