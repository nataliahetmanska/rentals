import unittest
import interaction_with_database as db


# ### TEST DOUBLES ### #
class KeyringDouble:
    def get_credential(self, *args, **kwargs):
        return CredentialDouble()


class CredentialDouble:
    def __init__(self):
        self.username = 'test_username'
        self.password = 'P4ssw0rd1'


class ConnectorDouble:
    def __init__(self):
        self._connection = None

    def connect(self, **kwargs):
        self._connection = ConnectionDouble()
        return self._connection


class ConnectionDouble:
    def __init__(self):
        self._cursor = None

    def cursor(self):
        self._cursor = CursorDouble()
        return self._cursor


class CursorDouble:
    def __init__(self):
        self.last_query = None

    def execute(self, query):
        self.last_query = query

    def fetchall(self):
        return []


# ### TESTS ### #
class TestInteractionWithDatabase(unittest.TestCase):
    """
    Here we demonstrate how setUp Method of unittest lib can be used
    to avoid repeating boilerplate code. setUp will be called before each test case, independently
    """
    def setUp(self):
        db.keyring = KeyringDouble()
        db.msc = ConnectorDouble()

    def test_select_data_passes_sql_code(self):
        """
        We have carefully prepared our test doubles to keep the objects they return as properties,
        so now we can call those properties in a chain and get to the latest sql query from execute method
        """
        sql = 'DROP TABLE USERS'
        db.select_data(sql)
        sql_passed = db.msc._connection._cursor.last_query
        self.assertEqual(sql_passed, sql)


if __name__ == '__main__':
    unittest.main()