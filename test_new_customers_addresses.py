from new_customers_addresses import *
import unittest
from datetime import datetime
import random as rnd

class TestCustomersGenerator(unittest.TestCase):

    def test_list_of_create_dates_happy_path(self):
        num = 30
        result = generate_list_of_create_dates(num)
        self.assertIsInstance(result, list)

    def test_correct_dates_in_list_of_create_dates(self):
        num = 30
        result = generate_list_of_create_dates(num)
        for i in range(30):
            self.assertGreaterEqual(datetime.strptime(result[i], '%Y-%m-%d %H:%M:%S'), datetime(2022, 8, 30, 0, 0, 0))

    def test_generate_customers_happy_path(self):
        result = generate_new_customers(30, generate_list_of_create_dates(30))
        for i in range(30):
            self.assertIsInstance(result[i], tuple)
            
    def test_length_of_tuple_containing_customers_information(self):
        result = generate_new_customers(30, generate_list_of_create_dates(30))
        for i in range(30):
            self.assertEqual(len(result[i]), 8)

    def test_misprint_in_customers_names(self):
        result = generate_new_customers(30, generate_list_of_create_dates(30))
        for i in range(30):
            if i%28==0:
                self.assertTrue(result[i][1].islower())
            
    def test_customers_age(self):
        result = generate_new_customers(30, generate_list_of_create_dates(30))
        for i in range(30):
            birth_date = datetime.strptime(result[i][5], '%Y-%m-%d')
            create_date = datetime.strptime(result[i][6], '%Y-%m-%d %H:%M:%S')
            self.assertGreaterEqual(create_date.year - birth_date.year - ((create_date.month, create_date.day) < (birth_date.month, birth_date.day)), 18)

    def test_generate_addresses_happy_path(self):
        result = generate_new_addresses(30, generate_list_of_create_dates(30))
        for i in range(30):
            self.assertIsInstance(result[i], tuple)

    def test_length_of_tuple_containing_addresses(self):
        result = generate_new_addresses(30, generate_list_of_create_dates(30))
        for i in range(30):
            self.assertEqual(len(result[i]), 6)




if __name__ == '__main__':
    unittest.main()
