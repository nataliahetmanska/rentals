from new_customers_addresses import list_of_create_dates, new_addresses, new_customers
import unittest
from datetime import datetime
import random as rnd

class TestCustomersGenerator(unittest.TestCase):

    def test_list_of_create_dates_happy_path(self):
        num = 30
        result = list_of_create_dates(num)
        self.assertIsInstance(result, list)

    def test_correct_dates_in_list_of_create_dates(self):
        num = 30
        result = list_of_create_dates(num)
        for i in range(30):
            self.assertGreaterEqual(datetime.strptime(result[i], '%Y-%m-%d %H:%M:%S'), datetime(2022, 8, 30, 0, 0, 0))

    def test_generate_customers_happy_path(self):
        result = new_customers(30, list_of_create_dates(30))
        for i in range(30):
            self.assertIsInstance(result[i], tuple)

    def test_misprint_in_customers_names(self):
        result = new_customers(30, list_of_create_dates(30))
        for i in range(30):
            if i%28==0:
                self.assertTrue(result[i][1].islower())
            else:
                self.assertFalse(result[i][1].islower())






if __name__ == '__main__':
    unittest.main()