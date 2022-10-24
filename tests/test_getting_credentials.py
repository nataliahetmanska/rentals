import unittest
import getting_credentials



class KeyringDouble:
    def __init__(self):
        self.keyring_params = None

    def set_password(self, *args, **kwargs):
        self.keyring_params = kwargs

class TestGettingCredentials(unittest.TestCase):
    def test_save_credentials(self):
        username = 'username'
        password = '123'
        getting_credentials.keyring = KeyringDouble()
        expected_params = {'username': 'username', 'password': '123'}
        res = getting_credentials.save_credentials(username, password)
        self.assertEqual(getting_credentials.keyring.keyring_params, expected_params)


if __name__ == '__main__':
    unittest.main()
