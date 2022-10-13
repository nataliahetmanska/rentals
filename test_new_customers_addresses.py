import new_customers_addresses
import unittest
import datetime
from unittest import mock
import random
from datetime import date

class TestCustomersGenerator(unittest.TestCase):

    def test_list_of_create_dates_happy_path(self):
        num = 1
        new_customers_addresses.random.choice = random_choice

        result = new_customers_addresses.generate_list_of_create_dates(num)
        date1 = str(datetime.datetime(2022, 8, 30))

        res = []
        res.append(date1)
        print(res)
        self.assertEqual(result, res)


    def test_generate_new_addresses(self):
        new_customers_addresses.Faker.postcode = post_code
        new_customers_addresses.Faker.street_name = streetname
        new_customers_addresses.Faker.building_number = building_num

        country_value = 1
        last_address_id = 1
        city_id = 1
        num = 10

        list_of_create_date = ['2022-09-03 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-04 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-08 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-17 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-22 00:00:00', '2022-09-26 00:00:00']

        expected_result = [(2, 'K Dýmači 83', '', 1, '198 69', '2022-09-03 00:00:00'),
                           (3, 'K Dýmači 83', '', 1, '198 69', '2022-09-04 00:00:00'),
                           (4, 'K Dýmači 83', '', 1, '198 69', '2022-09-04 00:00:00'),
                           (5, 'K Dýmači 83', '', 1, '198 69', '2022-09-05 00:00:00'),
                           (6, 'K Dýmači 83', '', 1, '198 69', '2022-09-08 00:00:00'),
                           (7, 'K Dýmači 83', '', 1, '198 69', '2022-09-09 00:00:00'),
                           (8, 'K Dýmači 83', '', 1, '198 69', '2022-09-17 00:00:00'),
                           (9, 'K Dýmači 83', '', 1, '198 69', '2022-09-18 00:00:00'),
                           (10, 'K Dýmači 83', '', 1, '198 69', '2022-09-22 00:00:00'),
                           (11, 'K Dýmači 83', '', 1, '198 69', '2022-09-26 00:00:00')]
        
        result = new_customers_addresses.generate_new_addresses(num, list_of_create_date, last_address_id, country_value, city_id)
        self.assertEqual(result, expected_result)

    def test_generate_new_customers(self):
        new_customers_addresses.Faker.name = fake_name
        new_customers_addresses.Faker.domain_name = fake_domain_name
        new_customers_addresses.Faker.date_of_birth = fake_birth_date
        ids_addresses = [23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
        last_customer_id = 1
        num = 10
        list_of_create_date = ['2022-09-03 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-04 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-08 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-17 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-22 00:00:00', '2022-09-26 00:00:00']
        expected_result = [(2, 'michael', 'ramp', 23, 'ramp@rivas.com', '1993-08-01', '2022-09-03 00:00:00',
                            '2022-09-03 00:00:00'),
                           (3, 'Michael', 'Ramp', 24, 'michael.ramp@rivas.com', '1993-08-01', '2022-09-04 00:00:00',
                            '2022-09-04 00:00:00'),
                           (4, 'Michael', 'Ramp', 25, 'michael.ramp@rivas.com', '1993-08-01', '2022-09-04 00:00:00',
                            '2022-09-04 00:00:00'),
                           (5, 'Michael', 'Ramp', 26, 'michael.ramp@rivas.com', '1993-08-01', '2022-09-05 00:00:00',
                            '2022-09-05 00:00:00'),
                           (6, 'Michael', 'Ramp', 27, 'ramp@rivas.com', '1993-08-01', '2022-09-08 00:00:00',
                            '2022-09-08 00:00:00'),
                           (7, 'Michael', 'Ramp', 28, 'michael.ramp@rivas.com', '1993-08-01', '2022-09-09 00:00:00',
                            '2022-09-09 00:00:00'),
                           (8, 'Michael', 'Ramp', 29, 'michael.ramp@rivas.com', '1993-08-01', '2022-09-17 00:00:00',
                            '2022-09-17 00:00:00'),
                           (9, 'michael', 'ramp', 30, 'michael.ramp@rivas.com', '1993-08-01', '2022-09-18 00:00:00',
                            '2022-09-18 00:00:00'),
                           (10, 'Michael', 'Ramp', 31, 'ramp@rivas.com', '1993-08-01', '2022-09-22 00:00:00',
                            '2022-09-22 00:00:00'),
                           (11, 'Michael', 'Ramp', 32, 'micramp@rivas.com', '1993-08-01', '2022-09-26 00:00:00',
                            '2022-09-26 00:00:00')]
        result = new_customers_addresses.generate_new_customers(num, list_of_create_date, last_customer_id, ids_addresses)
        self.assertEqual(expected_result, result)





def random_choice(x):
    return x[:1][0]

def post_code(x):
    return '198 69'

def streetname(x):
    return 'K Dýmači'

def building_num(x):
    return '83'

def fake_name(x):
    return 'Michael Ramp'

def fake_domain_name(x):
    return 'rivas.com'

def fake_birth_date(x,y,z,t):
    return str(date(1993, 8, 1))

if __name__ == '__main__':
    unittest.main()
