import main
import unittest
from datetime import datetime


class TestRentalGenerator(unittest.TestCase):

    def test_generate_rentals_happy_path(self):
        main.rnd.sample = generate_sample
        main.return_offset_fun = return_offset_stub
        latest_date = datetime.strptime("2022-08-30", '%Y-%m-%d')
        available = set(range(100, 200))

        month = 30
        daily_rent_wage = [1 for _ in range(month)]
        daily_rent_number = 10
        result = main.generate_rentals(available, latest_date, daily_rent_number, daily_rent_wage)

        expected_result = [
            [{'rental_date': '2022-08-30 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-01 00:00:00'},
             {'rental_date': '2022-08-30 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-01 00:00:00'},
             {'rental_date': '2022-08-30 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-01 00:00:00'},
             {'rental_date': '2022-08-30 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-01 00:00:00'},
             {'rental_date': '2022-08-30 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-01 00:00:00'},
             {'rental_date': '2022-08-30 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-01 00:00:00'},
             {'rental_date': '2022-08-30 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-01 00:00:00'},
             {'rental_date': '2022-08-30 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-01 00:00:00'},
             {'rental_date': '2022-08-30 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-01 00:00:00'},
             {'rental_date': '2022-08-30 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-01 00:00:00'}],
            [{'rental_date': '2022-08-31 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-02 00:00:00'},
             {'rental_date': '2022-08-31 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-02 00:00:00'},
             {'rental_date': '2022-08-31 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-02 00:00:00'},
             {'rental_date': '2022-08-31 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-02 00:00:00'},
             {'rental_date': '2022-08-31 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-02 00:00:00'},
             {'rental_date': '2022-08-31 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-02 00:00:00'},
             {'rental_date': '2022-08-31 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-02 00:00:00'},
             {'rental_date': '2022-08-31 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-02 00:00:00'},
             {'rental_date': '2022-08-31 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-02 00:00:00'},
             {'rental_date': '2022-08-31 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-02 00:00:00'}],
            [{'rental_date': '2022-09-01 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-03 00:00:00'},
             {'rental_date': '2022-09-01 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-03 00:00:00'},
             {'rental_date': '2022-09-01 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-03 00:00:00'},
             {'rental_date': '2022-09-01 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-03 00:00:00'},
             {'rental_date': '2022-09-01 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-03 00:00:00'},
             {'rental_date': '2022-09-01 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-03 00:00:00'},
             {'rental_date': '2022-09-01 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-03 00:00:00'},
             {'rental_date': '2022-09-01 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-03 00:00:00'},
             {'rental_date': '2022-09-01 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-03 00:00:00'},
             {'rental_date': '2022-09-01 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-03 00:00:00'}],
            [{'rental_date': '2022-09-02 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-04 00:00:00'},
             {'rental_date': '2022-09-02 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-04 00:00:00'},
             {'rental_date': '2022-09-02 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-04 00:00:00'},
             {'rental_date': '2022-09-02 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-04 00:00:00'},
             {'rental_date': '2022-09-02 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-04 00:00:00'},
             {'rental_date': '2022-09-02 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-04 00:00:00'},
             {'rental_date': '2022-09-02 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-04 00:00:00'},
             {'rental_date': '2022-09-02 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-04 00:00:00'},
             {'rental_date': '2022-09-02 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-04 00:00:00'},
             {'rental_date': '2022-09-02 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-04 00:00:00'}],
            [{'rental_date': '2022-09-03 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-05 00:00:00'},
             {'rental_date': '2022-09-03 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-05 00:00:00'},
             {'rental_date': '2022-09-03 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-05 00:00:00'},
             {'rental_date': '2022-09-03 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-05 00:00:00'},
             {'rental_date': '2022-09-03 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-05 00:00:00'},
             {'rental_date': '2022-09-03 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-05 00:00:00'},
             {'rental_date': '2022-09-03 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-05 00:00:00'},
             {'rental_date': '2022-09-03 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-05 00:00:00'},
             {'rental_date': '2022-09-03 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-05 00:00:00'},
             {'rental_date': '2022-09-03 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-05 00:00:00'}],
            [{'rental_date': '2022-09-04 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-06 00:00:00'},
             {'rental_date': '2022-09-04 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-06 00:00:00'},
             {'rental_date': '2022-09-04 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-06 00:00:00'},
             {'rental_date': '2022-09-04 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-06 00:00:00'},
             {'rental_date': '2022-09-04 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-06 00:00:00'},
             {'rental_date': '2022-09-04 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-06 00:00:00'},
             {'rental_date': '2022-09-04 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-06 00:00:00'},
             {'rental_date': '2022-09-04 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-06 00:00:00'},
             {'rental_date': '2022-09-04 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-06 00:00:00'},
             {'rental_date': '2022-09-04 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-06 00:00:00'}],
            [{'rental_date': '2022-09-05 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-07 00:00:00'},
             {'rental_date': '2022-09-05 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-07 00:00:00'},
             {'rental_date': '2022-09-05 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-07 00:00:00'},
             {'rental_date': '2022-09-05 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-07 00:00:00'},
             {'rental_date': '2022-09-05 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-07 00:00:00'},
             {'rental_date': '2022-09-05 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-07 00:00:00'},
             {'rental_date': '2022-09-05 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-07 00:00:00'},
             {'rental_date': '2022-09-05 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-07 00:00:00'},
             {'rental_date': '2022-09-05 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-07 00:00:00'},
             {'rental_date': '2022-09-05 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-07 00:00:00'}],
            [{'rental_date': '2022-09-06 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-08 00:00:00'},
             {'rental_date': '2022-09-06 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-08 00:00:00'},
             {'rental_date': '2022-09-06 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-08 00:00:00'},
             {'rental_date': '2022-09-06 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-08 00:00:00'},
             {'rental_date': '2022-09-06 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-08 00:00:00'},
             {'rental_date': '2022-09-06 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-08 00:00:00'},
             {'rental_date': '2022-09-06 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-08 00:00:00'},
             {'rental_date': '2022-09-06 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-08 00:00:00'},
             {'rental_date': '2022-09-06 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-08 00:00:00'},
             {'rental_date': '2022-09-06 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-08 00:00:00'}],
            [{'rental_date': '2022-09-07 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-09 00:00:00'},
             {'rental_date': '2022-09-07 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-09 00:00:00'},
             {'rental_date': '2022-09-07 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-09 00:00:00'},
             {'rental_date': '2022-09-07 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-09 00:00:00'},
             {'rental_date': '2022-09-07 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-09 00:00:00'},
             {'rental_date': '2022-09-07 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-09 00:00:00'},
             {'rental_date': '2022-09-07 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-09 00:00:00'},
             {'rental_date': '2022-09-07 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-09 00:00:00'},
             {'rental_date': '2022-09-07 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-09 00:00:00'},
             {'rental_date': '2022-09-07 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-09 00:00:00'}],
            [{'rental_date': '2022-09-08 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-10 00:00:00'},
             {'rental_date': '2022-09-08 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-10 00:00:00'},
             {'rental_date': '2022-09-08 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-10 00:00:00'},
             {'rental_date': '2022-09-08 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-10 00:00:00'},
             {'rental_date': '2022-09-08 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-10 00:00:00'},
             {'rental_date': '2022-09-08 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-10 00:00:00'},
             {'rental_date': '2022-09-08 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-10 00:00:00'},
             {'rental_date': '2022-09-08 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-10 00:00:00'},
             {'rental_date': '2022-09-08 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-10 00:00:00'},
             {'rental_date': '2022-09-08 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-10 00:00:00'}],
            [{'rental_date': '2022-09-09 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-11 00:00:00'},
             {'rental_date': '2022-09-09 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-11 00:00:00'},
             {'rental_date': '2022-09-09 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-11 00:00:00'},
             {'rental_date': '2022-09-09 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-11 00:00:00'},
             {'rental_date': '2022-09-09 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-11 00:00:00'},
             {'rental_date': '2022-09-09 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-11 00:00:00'},
             {'rental_date': '2022-09-09 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-11 00:00:00'},
             {'rental_date': '2022-09-09 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-11 00:00:00'},
             {'rental_date': '2022-09-09 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-11 00:00:00'},
             {'rental_date': '2022-09-09 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-11 00:00:00'}],
            [{'rental_date': '2022-09-10 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-12 00:00:00'},
             {'rental_date': '2022-09-10 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-12 00:00:00'},
             {'rental_date': '2022-09-10 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-12 00:00:00'},
             {'rental_date': '2022-09-10 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-12 00:00:00'},
             {'rental_date': '2022-09-10 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-12 00:00:00'},
             {'rental_date': '2022-09-10 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-12 00:00:00'},
             {'rental_date': '2022-09-10 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-12 00:00:00'},
             {'rental_date': '2022-09-10 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-12 00:00:00'},
             {'rental_date': '2022-09-10 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-12 00:00:00'},
             {'rental_date': '2022-09-10 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-12 00:00:00'}],
            [{'rental_date': '2022-09-11 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-13 00:00:00'},
             {'rental_date': '2022-09-11 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-13 00:00:00'},
             {'rental_date': '2022-09-11 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-13 00:00:00'},
             {'rental_date': '2022-09-11 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-13 00:00:00'},
             {'rental_date': '2022-09-11 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-13 00:00:00'},
             {'rental_date': '2022-09-11 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-13 00:00:00'},
             {'rental_date': '2022-09-11 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-13 00:00:00'},
             {'rental_date': '2022-09-11 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-13 00:00:00'},
             {'rental_date': '2022-09-11 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-13 00:00:00'},
             {'rental_date': '2022-09-11 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-13 00:00:00'}],
            [{'rental_date': '2022-09-12 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-14 00:00:00'},
             {'rental_date': '2022-09-12 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-14 00:00:00'},
             {'rental_date': '2022-09-12 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-14 00:00:00'},
             {'rental_date': '2022-09-12 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-14 00:00:00'},
             {'rental_date': '2022-09-12 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-14 00:00:00'},
             {'rental_date': '2022-09-12 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-14 00:00:00'},
             {'rental_date': '2022-09-12 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-14 00:00:00'},
             {'rental_date': '2022-09-12 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-14 00:00:00'},
             {'rental_date': '2022-09-12 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-14 00:00:00'},
             {'rental_date': '2022-09-12 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-14 00:00:00'}],
            [{'rental_date': '2022-09-13 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-15 00:00:00'},
             {'rental_date': '2022-09-13 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-15 00:00:00'},
             {'rental_date': '2022-09-13 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-15 00:00:00'},
             {'rental_date': '2022-09-13 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-15 00:00:00'},
             {'rental_date': '2022-09-13 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-15 00:00:00'},
             {'rental_date': '2022-09-13 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-15 00:00:00'},
             {'rental_date': '2022-09-13 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-15 00:00:00'},
             {'rental_date': '2022-09-13 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-15 00:00:00'},
             {'rental_date': '2022-09-13 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-15 00:00:00'},
             {'rental_date': '2022-09-13 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-15 00:00:00'}],
            [{'rental_date': '2022-09-14 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-16 00:00:00'},
             {'rental_date': '2022-09-14 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-16 00:00:00'},
             {'rental_date': '2022-09-14 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-16 00:00:00'},
             {'rental_date': '2022-09-14 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-16 00:00:00'},
             {'rental_date': '2022-09-14 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-16 00:00:00'},
             {'rental_date': '2022-09-14 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-16 00:00:00'},
             {'rental_date': '2022-09-14 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-16 00:00:00'},
             {'rental_date': '2022-09-14 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-16 00:00:00'},
             {'rental_date': '2022-09-14 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-16 00:00:00'},
             {'rental_date': '2022-09-14 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-16 00:00:00'}],
            [{'rental_date': '2022-09-15 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-17 00:00:00'},
             {'rental_date': '2022-09-15 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-17 00:00:00'},
             {'rental_date': '2022-09-15 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-17 00:00:00'},
             {'rental_date': '2022-09-15 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-17 00:00:00'},
             {'rental_date': '2022-09-15 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-17 00:00:00'},
             {'rental_date': '2022-09-15 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-17 00:00:00'},
             {'rental_date': '2022-09-15 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-17 00:00:00'},
             {'rental_date': '2022-09-15 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-17 00:00:00'},
             {'rental_date': '2022-09-15 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-17 00:00:00'},
             {'rental_date': '2022-09-15 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-17 00:00:00'}],
            [{'rental_date': '2022-09-16 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-18 00:00:00'},
             {'rental_date': '2022-09-16 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-18 00:00:00'},
             {'rental_date': '2022-09-16 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-18 00:00:00'},
             {'rental_date': '2022-09-16 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-18 00:00:00'},
             {'rental_date': '2022-09-16 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-18 00:00:00'},
             {'rental_date': '2022-09-16 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-18 00:00:00'},
             {'rental_date': '2022-09-16 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-18 00:00:00'},
             {'rental_date': '2022-09-16 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-18 00:00:00'},
             {'rental_date': '2022-09-16 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-18 00:00:00'},
             {'rental_date': '2022-09-16 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-18 00:00:00'}],
            [{'rental_date': '2022-09-17 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-19 00:00:00'},
             {'rental_date': '2022-09-17 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-19 00:00:00'},
             {'rental_date': '2022-09-17 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-19 00:00:00'},
             {'rental_date': '2022-09-17 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-19 00:00:00'},
             {'rental_date': '2022-09-17 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-19 00:00:00'},
             {'rental_date': '2022-09-17 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-19 00:00:00'},
             {'rental_date': '2022-09-17 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-19 00:00:00'},
             {'rental_date': '2022-09-17 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-19 00:00:00'},
             {'rental_date': '2022-09-17 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-19 00:00:00'},
             {'rental_date': '2022-09-17 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-19 00:00:00'}],
            [{'rental_date': '2022-09-18 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-20 00:00:00'},
             {'rental_date': '2022-09-18 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-20 00:00:00'},
             {'rental_date': '2022-09-18 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-20 00:00:00'},
             {'rental_date': '2022-09-18 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-20 00:00:00'},
             {'rental_date': '2022-09-18 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-20 00:00:00'},
             {'rental_date': '2022-09-18 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-20 00:00:00'},
             {'rental_date': '2022-09-18 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-20 00:00:00'},
             {'rental_date': '2022-09-18 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-20 00:00:00'},
             {'rental_date': '2022-09-18 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-20 00:00:00'},
             {'rental_date': '2022-09-18 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-20 00:00:00'}],
            [{'rental_date': '2022-09-19 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-21 00:00:00'},
             {'rental_date': '2022-09-19 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-21 00:00:00'},
             {'rental_date': '2022-09-19 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-21 00:00:00'},
             {'rental_date': '2022-09-19 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-21 00:00:00'},
             {'rental_date': '2022-09-19 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-21 00:00:00'},
             {'rental_date': '2022-09-19 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-21 00:00:00'},
             {'rental_date': '2022-09-19 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-21 00:00:00'},
             {'rental_date': '2022-09-19 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-21 00:00:00'},
             {'rental_date': '2022-09-19 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-21 00:00:00'},
             {'rental_date': '2022-09-19 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-21 00:00:00'}],
            [{'rental_date': '2022-09-20 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-22 00:00:00'},
             {'rental_date': '2022-09-20 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-22 00:00:00'},
             {'rental_date': '2022-09-20 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-22 00:00:00'},
             {'rental_date': '2022-09-20 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-22 00:00:00'},
             {'rental_date': '2022-09-20 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-22 00:00:00'},
             {'rental_date': '2022-09-20 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-22 00:00:00'},
             {'rental_date': '2022-09-20 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-22 00:00:00'},
             {'rental_date': '2022-09-20 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-22 00:00:00'},
             {'rental_date': '2022-09-20 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-22 00:00:00'},
             {'rental_date': '2022-09-20 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-22 00:00:00'}],
            [{'rental_date': '2022-09-21 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-23 00:00:00'},
             {'rental_date': '2022-09-21 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-23 00:00:00'},
             {'rental_date': '2022-09-21 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-23 00:00:00'},
             {'rental_date': '2022-09-21 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-23 00:00:00'},
             {'rental_date': '2022-09-21 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-23 00:00:00'},
             {'rental_date': '2022-09-21 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-23 00:00:00'},
             {'rental_date': '2022-09-21 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-23 00:00:00'},
             {'rental_date': '2022-09-21 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-23 00:00:00'},
             {'rental_date': '2022-09-21 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-23 00:00:00'},
             {'rental_date': '2022-09-21 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-23 00:00:00'}],
            [{'rental_date': '2022-09-22 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-24 00:00:00'},
             {'rental_date': '2022-09-22 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-24 00:00:00'},
             {'rental_date': '2022-09-22 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-24 00:00:00'},
             {'rental_date': '2022-09-22 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-24 00:00:00'},
             {'rental_date': '2022-09-22 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-24 00:00:00'},
             {'rental_date': '2022-09-22 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-24 00:00:00'},
             {'rental_date': '2022-09-22 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-24 00:00:00'},
             {'rental_date': '2022-09-22 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-24 00:00:00'},
             {'rental_date': '2022-09-22 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-24 00:00:00'},
             {'rental_date': '2022-09-22 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-24 00:00:00'}],
            [{'rental_date': '2022-09-23 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-25 00:00:00'},
             {'rental_date': '2022-09-23 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-25 00:00:00'},
             {'rental_date': '2022-09-23 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-25 00:00:00'},
             {'rental_date': '2022-09-23 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-25 00:00:00'},
             {'rental_date': '2022-09-23 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-25 00:00:00'},
             {'rental_date': '2022-09-23 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-25 00:00:00'},
             {'rental_date': '2022-09-23 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-25 00:00:00'},
             {'rental_date': '2022-09-23 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-25 00:00:00'},
             {'rental_date': '2022-09-23 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-25 00:00:00'},
             {'rental_date': '2022-09-23 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-25 00:00:00'}],
            [{'rental_date': '2022-09-24 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-26 00:00:00'},
             {'rental_date': '2022-09-24 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-26 00:00:00'},
             {'rental_date': '2022-09-24 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-26 00:00:00'},
             {'rental_date': '2022-09-24 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-26 00:00:00'},
             {'rental_date': '2022-09-24 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-26 00:00:00'},
             {'rental_date': '2022-09-24 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-26 00:00:00'},
             {'rental_date': '2022-09-24 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-26 00:00:00'},
             {'rental_date': '2022-09-24 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-26 00:00:00'},
             {'rental_date': '2022-09-24 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-26 00:00:00'},
             {'rental_date': '2022-09-24 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-26 00:00:00'}],
            [{'rental_date': '2022-09-25 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-27 00:00:00'},
             {'rental_date': '2022-09-25 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-27 00:00:00'},
             {'rental_date': '2022-09-25 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-27 00:00:00'},
             {'rental_date': '2022-09-25 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-27 00:00:00'},
             {'rental_date': '2022-09-25 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-27 00:00:00'},
             {'rental_date': '2022-09-25 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-27 00:00:00'},
             {'rental_date': '2022-09-25 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-27 00:00:00'},
             {'rental_date': '2022-09-25 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-27 00:00:00'},
             {'rental_date': '2022-09-25 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-27 00:00:00'},
             {'rental_date': '2022-09-25 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-27 00:00:00'}],
            [{'rental_date': '2022-09-26 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-28 00:00:00'},
             {'rental_date': '2022-09-26 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-28 00:00:00'},
             {'rental_date': '2022-09-26 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-28 00:00:00'},
             {'rental_date': '2022-09-26 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-28 00:00:00'},
             {'rental_date': '2022-09-26 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-28 00:00:00'},
             {'rental_date': '2022-09-26 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-28 00:00:00'},
             {'rental_date': '2022-09-26 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-28 00:00:00'},
             {'rental_date': '2022-09-26 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-28 00:00:00'},
             {'rental_date': '2022-09-26 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-28 00:00:00'},
             {'rental_date': '2022-09-26 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-28 00:00:00'}],
            [{'rental_date': '2022-09-27 00:00:00', 'car_id': 100, 'offset': 2, 'return_date': '2022-09-29 00:00:00'},
             {'rental_date': '2022-09-27 00:00:00', 'car_id': 101, 'offset': 2, 'return_date': '2022-09-29 00:00:00'},
             {'rental_date': '2022-09-27 00:00:00', 'car_id': 102, 'offset': 2, 'return_date': '2022-09-29 00:00:00'},
             {'rental_date': '2022-09-27 00:00:00', 'car_id': 103, 'offset': 2, 'return_date': '2022-09-29 00:00:00'},
             {'rental_date': '2022-09-27 00:00:00', 'car_id': 104, 'offset': 2, 'return_date': '2022-09-29 00:00:00'},
             {'rental_date': '2022-09-27 00:00:00', 'car_id': 105, 'offset': 2, 'return_date': '2022-09-29 00:00:00'},
             {'rental_date': '2022-09-27 00:00:00', 'car_id': 106, 'offset': 2, 'return_date': '2022-09-29 00:00:00'},
             {'rental_date': '2022-09-27 00:00:00', 'car_id': 107, 'offset': 2, 'return_date': '2022-09-29 00:00:00'},
             {'rental_date': '2022-09-27 00:00:00', 'car_id': 108, 'offset': 2, 'return_date': '2022-09-29 00:00:00'},
             {'rental_date': '2022-09-27 00:00:00', 'car_id': 109, 'offset': 2, 'return_date': '2022-09-29 00:00:00'}],
            [{'rental_date': '2022-09-28 00:00:00', 'car_id': 110, 'offset': 2, 'return_date': '2022-09-30 00:00:00'},
             {'rental_date': '2022-09-28 00:00:00', 'car_id': 111, 'offset': 2, 'return_date': '2022-09-30 00:00:00'},
             {'rental_date': '2022-09-28 00:00:00', 'car_id': 112, 'offset': 2, 'return_date': '2022-09-30 00:00:00'},
             {'rental_date': '2022-09-28 00:00:00', 'car_id': 113, 'offset': 2, 'return_date': '2022-09-30 00:00:00'},
             {'rental_date': '2022-09-28 00:00:00', 'car_id': 114, 'offset': 2, 'return_date': '2022-09-30 00:00:00'},
             {'rental_date': '2022-09-28 00:00:00', 'car_id': 115, 'offset': 2, 'return_date': '2022-09-30 00:00:00'},
             {'rental_date': '2022-09-28 00:00:00', 'car_id': 116, 'offset': 2, 'return_date': '2022-09-30 00:00:00'},
             {'rental_date': '2022-09-28 00:00:00', 'car_id': 117, 'offset': 2, 'return_date': '2022-09-30 00:00:00'},
             {'rental_date': '2022-09-28 00:00:00', 'car_id': 118, 'offset': 2, 'return_date': '2022-09-30 00:00:00'},
             {'rental_date': '2022-09-28 00:00:00', 'car_id': 119, 'offset': 2, 'return_date': '2022-09-30 00:00:00'}]]

        self.assertEqual(result, expected_result)

    def test_generating_with_no_rentals(self):
        main.rnd.sample = generate_sample
        main.return_offset_fun = return_offset_stub
        latest_date = datetime.strptime("2022-08-30", '%Y-%m-%d')
        available = set(range(100, 200))

        month = 30
        daily_rent_wage = [1 for _ in range(month)]
        daily_rent_number = 0
        result = main.generate_rentals(available, latest_date, daily_rent_number, daily_rent_wage)
        expected_result = [[] for _ in range(month)]
        self.assertEqual(result, expected_result)

    def test_generating_with_negative_daily_rentals(self):
        main.rnd.sample = generate_sample
        main.return_offset_fun = return_offset_stub
        latest_date = datetime.strptime("2022-08-30", '%Y-%m-%d')
        available = set(range(100, 200))
        month = 30
        daily_rent_wage = [1 for _ in range(month)]
        daily_rent_number = -2

        self.assertRaises(ValueError, main.generate_rentals, available, latest_date, daily_rent_number, daily_rent_wage)

    def test_generating_with_negative_daily_rent_wages(self):
        main.rnd.sample = generate_sample
        main.return_offset_fun = return_offset_stub
        latest_date = datetime.strptime("2022-08-30", '%Y-%m-%d')
        available = set(range(100, 200))

        month = 30
        daily_rent_wage = [-1 for _ in range(month)]
        daily_rent_number = 10
        self.assertRaises(ValueError, main.generate_rentals, available, latest_date, daily_rent_number, daily_rent_wage)

    def test_if_the_same_car_is_not_rented_twice_at_the_same_time(self):
        main.rnd.sample = generate_sample
        main.return_offset_fun = return_offset_stub
        latest_date = datetime.strptime("2022-08-30", '%Y-%m-%d')
        available = set(range(100, 200))

        month = 30
        daily_rent_wage = [1 for _ in range(month)]
        daily_rent_number = 90

        result = main.generate_rentals(available, latest_date, daily_rent_number, daily_rent_wage)

        rented = []
        for i in result[5]:
            rented.append(i["car_id"])

        rented_with_no_duplicates = list(set(rented))
        self.assertEqual(len(rented), len(rented_with_no_duplicates))

    def test_insert_data_happy_path(self):
        main.rnd.sample = generate_sample
        main.return_offset_fun = return_offset_stub
        latest_date = datetime.strptime("2022-08-30", '%Y-%m-%d')
        available = set(range(100, 200))
        month = 30
        daily_rent_wage = [1 for _ in range(month)]
        daily_rent_number = 10

        rental_list = main.generate_rentals(available, latest_date, daily_rent_number, daily_rent_wage)
        main.rnd.choices = return_cust_id
        main.rnd.randint = return_staff_id
        latest_index_from_db = 101
        cust_id = set(range(1, 201))
        number_of_rentals_per_person = [1 for _ in range(len(cust_id))]
        create_dates = [datetime.strptime('2022-01-08 00:00:00', '%Y-%m-%d %H:%M:%S') for _ in range(len(cust_id))]
        customers = list(zip(cust_id, number_of_rentals_per_person, create_dates))

        new_cust_id = set(range(201, 251))
        new_number_of_rentals_per_person = [0 for _ in range(len(new_cust_id))]
        new_create_dates = [datetime.strptime('2022-09-30 00:00:00', '%Y-%m-%d %H:%M:%S') for _ in
                            range(len(new_cust_id))]
        new_customers = list(zip(new_cust_id, new_create_dates, new_number_of_rentals_per_person))

        rental_rates = {rate: 119 for rate in range(100, 100 + len(available))}
        result = main.insert_data(rental_list, latest_index_from_db, customers, new_customers, rental_rates)

        expected_result = [(101, 119, 201, 100, 1, '2022-08-30 00:00:00', '2022-09-01 00:00:00', '2022-09-06 00:00:00',
                            '2022-08-30 00:00:00'), (
                               102, 119, 201, 101, 1, '2022-08-30 00:00:00', '2022-09-01 00:00:00',
                               '2022-09-06 00:00:00',
                               '2022-08-30 00:00:00'), (
                               103, 119, 201, 102, 1, '2022-08-30 00:00:00', '2022-09-01 00:00:00',
                               '2022-09-06 00:00:00',
                               '2022-08-30 00:00:00'), (
                               104, 119, 201, 103, 1, '2022-08-30 00:00:00', '2022-09-01 00:00:00',
                               '2022-09-06 00:00:00',
                               '2022-08-30 00:00:00'), (
                               105, 119, 201, 104, 1, '2022-08-30 00:00:00', '2022-09-01 00:00:00',
                               '2022-09-06 00:00:00',
                               '2022-08-30 00:00:00'), (
                               106, 119, 201, 105, 1, '2022-08-30 00:00:00', '2022-09-01 00:00:00',
                               '2022-09-06 00:00:00',
                               '2022-08-30 00:00:00'), (
                               107, 119, 201, 106, 1, '2022-08-30 00:00:00', '2022-09-01 00:00:00',
                               '2022-09-06 00:00:00',
                               '2022-08-30 00:00:00'), (
                               108, 119, 201, 107, 1, '2022-08-30 00:00:00', '2022-09-01 00:00:00',
                               '2022-09-06 00:00:00',
                               '2022-08-30 00:00:00'), (
                               109, 119, 201, 108, 1, '2022-08-30 00:00:00', '2022-09-01 00:00:00',
                               '2022-09-06 00:00:00',
                               '2022-08-30 00:00:00'), (
                               110, 119, 201, 109, 1, '2022-08-30 00:00:00', '2022-09-01 00:00:00',
                               '2022-09-06 00:00:00',
                               '2022-08-30 00:00:00'), (
                               111, 119, 201, 110, 1, '2022-08-31 00:00:00', '2022-09-02 00:00:00',
                               '2022-09-07 00:00:00',
                               '2022-08-31 00:00:00'), (
                               112, 119, 201, 111, 1, '2022-08-31 00:00:00', '2022-09-02 00:00:00',
                               '2022-09-07 00:00:00',
                               '2022-08-31 00:00:00'), (
                               113, 119, 201, 112, 1, '2022-08-31 00:00:00', '2022-09-02 00:00:00',
                               '2022-09-07 00:00:00',
                               '2022-08-31 00:00:00'), (
                               114, 119, 201, 113, 1, '2022-08-31 00:00:00', '2022-09-02 00:00:00',
                               '2022-09-07 00:00:00',
                               '2022-08-31 00:00:00'), (
                               115, 119, 201, 114, 1, '2022-08-31 00:00:00', '2022-09-02 00:00:00',
                               '2022-09-07 00:00:00',
                               '2022-08-31 00:00:00'), (
                               116, 119, 201, 115, 1, '2022-08-31 00:00:00', '2022-09-02 00:00:00',
                               '2022-09-07 00:00:00',
                               '2022-08-31 00:00:00'), (
                               117, 119, 201, 116, 1, '2022-08-31 00:00:00', '2022-09-02 00:00:00',
                               '2022-09-07 00:00:00',
                               '2022-08-31 00:00:00'), (
                               118, 119, 201, 117, 1, '2022-08-31 00:00:00', '2022-09-02 00:00:00',
                               '2022-09-07 00:00:00',
                               '2022-08-31 00:00:00'), (
                               119, 119, 201, 118, 1, '2022-08-31 00:00:00', '2022-09-02 00:00:00',
                               '2022-09-07 00:00:00',
                               '2022-08-31 00:00:00'), (
                               120, 119, 201, 119, 1, '2022-08-31 00:00:00', '2022-09-02 00:00:00',
                               '2022-09-07 00:00:00',
                               '2022-08-31 00:00:00'), (
                               121, 119, 201, 100, 1, '2022-09-01 00:00:00', '2022-09-03 00:00:00',
                               '2022-09-08 00:00:00',
                               '2022-09-01 00:00:00'), (
                               122, 119, 201, 101, 1, '2022-09-01 00:00:00', '2022-09-03 00:00:00',
                               '2022-09-08 00:00:00',
                               '2022-09-01 00:00:00'), (
                               123, 119, 201, 102, 1, '2022-09-01 00:00:00', '2022-09-03 00:00:00',
                               '2022-09-08 00:00:00',
                               '2022-09-01 00:00:00'), (
                               124, 119, 201, 103, 1, '2022-09-01 00:00:00', '2022-09-03 00:00:00',
                               '2022-09-08 00:00:00',
                               '2022-09-01 00:00:00'), (
                               125, 119, 201, 104, 1, '2022-09-01 00:00:00', '2022-09-03 00:00:00',
                               '2022-09-08 00:00:00',
                               '2022-09-01 00:00:00'), (
                               126, 119, 201, 105, 1, '2022-09-01 00:00:00', '2022-09-03 00:00:00',
                               '2022-09-08 00:00:00',
                               '2022-09-01 00:00:00'), (
                               127, 119, 201, 106, 1, '2022-09-01 00:00:00', '2022-09-03 00:00:00',
                               '2022-09-08 00:00:00',
                               '2022-09-01 00:00:00'), (
                               128, 119, 201, 107, 1, '2022-09-01 00:00:00', '2022-09-03 00:00:00',
                               '2022-09-08 00:00:00',
                               '2022-09-01 00:00:00'), (
                               129, 119, 201, 108, 1, '2022-09-01 00:00:00', '2022-09-03 00:00:00',
                               '2022-09-08 00:00:00',
                               '2022-09-01 00:00:00'), (
                               130, 119, 201, 109, 1, '2022-09-01 00:00:00', '2022-09-03 00:00:00',
                               '2022-09-08 00:00:00',
                               '2022-09-01 00:00:00'), (
                               131, 119, 201, 110, 1, '2022-09-02 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-09 00:00:00',
                               '2022-09-02 00:00:00'), (
                               132, 119, 201, 111, 1, '2022-09-02 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-09 00:00:00',
                               '2022-09-02 00:00:00'), (
                               133, 119, 201, 112, 1, '2022-09-02 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-09 00:00:00',
                               '2022-09-02 00:00:00'), (
                               134, 119, 201, 113, 1, '2022-09-02 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-09 00:00:00',
                               '2022-09-02 00:00:00'), (
                               135, 119, 201, 114, 1, '2022-09-02 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-09 00:00:00',
                               '2022-09-02 00:00:00'), (
                               136, 119, 201, 115, 1, '2022-09-02 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-09 00:00:00',
                               '2022-09-02 00:00:00'), (
                               137, 119, 201, 116, 1, '2022-09-02 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-09 00:00:00',
                               '2022-09-02 00:00:00'), (
                               138, 119, 201, 117, 1, '2022-09-02 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-09 00:00:00',
                               '2022-09-02 00:00:00'), (
                               139, 119, 201, 118, 1, '2022-09-02 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-09 00:00:00',
                               '2022-09-02 00:00:00'), (
                               140, 119, 201, 119, 1, '2022-09-02 00:00:00', '2022-09-04 00:00:00',
                               '2022-09-09 00:00:00',
                               '2022-09-02 00:00:00'), (
                               141, 119, 201, 100, 1, '2022-09-03 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-10 00:00:00',
                               '2022-09-03 00:00:00'), (
                               142, 119, 201, 101, 1, '2022-09-03 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-10 00:00:00',
                               '2022-09-03 00:00:00'), (
                               143, 119, 201, 102, 1, '2022-09-03 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-10 00:00:00',
                               '2022-09-03 00:00:00'), (
                               144, 119, 201, 103, 1, '2022-09-03 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-10 00:00:00',
                               '2022-09-03 00:00:00'), (
                               145, 119, 201, 104, 1, '2022-09-03 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-10 00:00:00',
                               '2022-09-03 00:00:00'), (
                               146, 119, 201, 105, 1, '2022-09-03 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-10 00:00:00',
                               '2022-09-03 00:00:00'), (
                               147, 119, 201, 106, 1, '2022-09-03 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-10 00:00:00',
                               '2022-09-03 00:00:00'), (
                               148, 119, 201, 107, 1, '2022-09-03 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-10 00:00:00',
                               '2022-09-03 00:00:00'), (
                               149, 119, 201, 108, 1, '2022-09-03 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-10 00:00:00',
                               '2022-09-03 00:00:00'), (
                               150, 119, 201, 109, 1, '2022-09-03 00:00:00', '2022-09-05 00:00:00',
                               '2022-09-10 00:00:00',
                               '2022-09-03 00:00:00'), (
                               151, 119, 201, 110, 1, '2022-09-04 00:00:00', '2022-09-06 00:00:00',
                               '2022-09-11 00:00:00',
                               '2022-09-04 00:00:00'), (
                               152, 119, 201, 111, 1, '2022-09-04 00:00:00', '2022-09-06 00:00:00',
                               '2022-09-11 00:00:00',
                               '2022-09-04 00:00:00'), (
                               153, 119, 201, 112, 1, '2022-09-04 00:00:00', '2022-09-06 00:00:00',
                               '2022-09-11 00:00:00',
                               '2022-09-04 00:00:00'), (
                               154, 119, 201, 113, 1, '2022-09-04 00:00:00', '2022-09-06 00:00:00',
                               '2022-09-11 00:00:00',
                               '2022-09-04 00:00:00'), (
                               155, 119, 201, 114, 1, '2022-09-04 00:00:00', '2022-09-06 00:00:00',
                               '2022-09-11 00:00:00',
                               '2022-09-04 00:00:00'), (
                               156, 119, 201, 115, 1, '2022-09-04 00:00:00', '2022-09-06 00:00:00',
                               '2022-09-11 00:00:00',
                               '2022-09-04 00:00:00'), (
                               157, 119, 201, 116, 1, '2022-09-04 00:00:00', '2022-09-06 00:00:00',
                               '2022-09-11 00:00:00',
                               '2022-09-04 00:00:00'), (
                               158, 119, 201, 117, 1, '2022-09-04 00:00:00', '2022-09-06 00:00:00',
                               '2022-09-11 00:00:00',
                               '2022-09-04 00:00:00'), (
                               159, 119, 201, 118, 1, '2022-09-04 00:00:00', '2022-09-06 00:00:00',
                               '2022-09-11 00:00:00',
                               '2022-09-04 00:00:00'), (
                               160, 119, 201, 119, 1, '2022-09-04 00:00:00', '2022-09-06 00:00:00',
                               '2022-09-11 00:00:00',
                               '2022-09-04 00:00:00'), (
                               161, 119, 201, 100, 1, '2022-09-05 00:00:00', '2022-09-07 00:00:00',
                               '2022-09-12 00:00:00',
                               '2022-09-05 00:00:00'), (
                               162, 119, 201, 101, 1, '2022-09-05 00:00:00', '2022-09-07 00:00:00',
                               '2022-09-12 00:00:00',
                               '2022-09-05 00:00:00'), (
                               163, 119, 201, 102, 1, '2022-09-05 00:00:00', '2022-09-07 00:00:00',
                               '2022-09-12 00:00:00',
                               '2022-09-05 00:00:00'), (
                               164, 119, 201, 103, 1, '2022-09-05 00:00:00', '2022-09-07 00:00:00',
                               '2022-09-12 00:00:00',
                               '2022-09-05 00:00:00'), (
                               165, 119, 201, 104, 1, '2022-09-05 00:00:00', '2022-09-07 00:00:00',
                               '2022-09-12 00:00:00',
                               '2022-09-05 00:00:00'), (
                               166, 119, 201, 105, 1, '2022-09-05 00:00:00', '2022-09-07 00:00:00',
                               '2022-09-12 00:00:00',
                               '2022-09-05 00:00:00'), (
                               167, 119, 201, 106, 1, '2022-09-05 00:00:00', '2022-09-07 00:00:00',
                               '2022-09-12 00:00:00',
                               '2022-09-05 00:00:00'), (
                               168, 119, 201, 107, 1, '2022-09-05 00:00:00', '2022-09-07 00:00:00',
                               '2022-09-12 00:00:00',
                               '2022-09-05 00:00:00'), (
                               169, 119, 201, 108, 1, '2022-09-05 00:00:00', '2022-09-07 00:00:00',
                               '2022-09-12 00:00:00',
                               '2022-09-05 00:00:00'), (
                               170, 119, 201, 109, 1, '2022-09-05 00:00:00', '2022-09-07 00:00:00',
                               '2022-09-12 00:00:00',
                               '2022-09-05 00:00:00'), (
                               171, 119, 201, 110, 1, '2022-09-06 00:00:00', '2022-09-08 00:00:00',
                               '2022-09-13 00:00:00',
                               '2022-09-06 00:00:00'), (
                               172, 119, 201, 111, 1, '2022-09-06 00:00:00', '2022-09-08 00:00:00',
                               '2022-09-13 00:00:00',
                               '2022-09-06 00:00:00'), (
                               173, 119, 201, 112, 1, '2022-09-06 00:00:00', '2022-09-08 00:00:00',
                               '2022-09-13 00:00:00',
                               '2022-09-06 00:00:00'), (
                               174, 119, 201, 113, 1, '2022-09-06 00:00:00', '2022-09-08 00:00:00',
                               '2022-09-13 00:00:00',
                               '2022-09-06 00:00:00'), (
                               175, 119, 201, 114, 1, '2022-09-06 00:00:00', '2022-09-08 00:00:00',
                               '2022-09-13 00:00:00',
                               '2022-09-06 00:00:00'), (
                               176, 119, 201, 115, 1, '2022-09-06 00:00:00', '2022-09-08 00:00:00',
                               '2022-09-13 00:00:00',
                               '2022-09-06 00:00:00'), (
                               177, 119, 201, 116, 1, '2022-09-06 00:00:00', '2022-09-08 00:00:00',
                               '2022-09-13 00:00:00',
                               '2022-09-06 00:00:00'), (
                               178, 119, 201, 117, 1, '2022-09-06 00:00:00', '2022-09-08 00:00:00',
                               '2022-09-13 00:00:00',
                               '2022-09-06 00:00:00'), (
                               179, 119, 201, 118, 1, '2022-09-06 00:00:00', '2022-09-08 00:00:00',
                               '2022-09-13 00:00:00',
                               '2022-09-06 00:00:00'), (
                               180, 119, 201, 119, 1, '2022-09-06 00:00:00', '2022-09-08 00:00:00',
                               '2022-09-13 00:00:00',
                               '2022-09-06 00:00:00'), (
                               181, 119, 201, 100, 1, '2022-09-07 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-14 00:00:00',
                               '2022-09-07 00:00:00'), (
                               182, 119, 201, 101, 1, '2022-09-07 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-14 00:00:00',
                               '2022-09-07 00:00:00'), (
                               183, 119, 201, 102, 1, '2022-09-07 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-14 00:00:00',
                               '2022-09-07 00:00:00'), (
                               184, 119, 201, 103, 1, '2022-09-07 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-14 00:00:00',
                               '2022-09-07 00:00:00'), (
                               185, 119, 201, 104, 1, '2022-09-07 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-14 00:00:00',
                               '2022-09-07 00:00:00'), (
                               186, 119, 201, 105, 1, '2022-09-07 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-14 00:00:00',
                               '2022-09-07 00:00:00'), (
                               187, 119, 201, 106, 1, '2022-09-07 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-14 00:00:00',
                               '2022-09-07 00:00:00'), (
                               188, 119, 201, 107, 1, '2022-09-07 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-14 00:00:00',
                               '2022-09-07 00:00:00'), (
                               189, 119, 201, 108, 1, '2022-09-07 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-14 00:00:00',
                               '2022-09-07 00:00:00'), (
                               190, 119, 201, 109, 1, '2022-09-07 00:00:00', '2022-09-09 00:00:00',
                               '2022-09-14 00:00:00',
                               '2022-09-07 00:00:00'), (
                               191, 119, 201, 110, 1, '2022-09-08 00:00:00', '2022-09-10 00:00:00',
                               '2022-09-15 00:00:00',
                               '2022-09-08 00:00:00'), (
                               192, 119, 201, 111, 1, '2022-09-08 00:00:00', '2022-09-10 00:00:00',
                               '2022-09-15 00:00:00',
                               '2022-09-08 00:00:00'), (
                               193, 119, 201, 112, 1, '2022-09-08 00:00:00', '2022-09-10 00:00:00',
                               '2022-09-15 00:00:00',
                               '2022-09-08 00:00:00'), (
                               194, 119, 201, 113, 1, '2022-09-08 00:00:00', '2022-09-10 00:00:00',
                               '2022-09-15 00:00:00',
                               '2022-09-08 00:00:00'), (
                               195, 119, 201, 114, 1, '2022-09-08 00:00:00', '2022-09-10 00:00:00',
                               '2022-09-15 00:00:00',
                               '2022-09-08 00:00:00'), (
                               196, 119, 201, 115, 1, '2022-09-08 00:00:00', '2022-09-10 00:00:00',
                               '2022-09-15 00:00:00',
                               '2022-09-08 00:00:00'), (
                               197, 119, 201, 116, 1, '2022-09-08 00:00:00', '2022-09-10 00:00:00',
                               '2022-09-15 00:00:00',
                               '2022-09-08 00:00:00'), (
                               198, 119, 201, 117, 1, '2022-09-08 00:00:00', '2022-09-10 00:00:00',
                               '2022-09-15 00:00:00',
                               '2022-09-08 00:00:00'), (
                               199, 119, 201, 118, 1, '2022-09-08 00:00:00', '2022-09-10 00:00:00',
                               '2022-09-15 00:00:00',
                               '2022-09-08 00:00:00'), (
                               200, 119, 201, 119, 1, '2022-09-08 00:00:00', '2022-09-10 00:00:00',
                               '2022-09-15 00:00:00',
                               '2022-09-08 00:00:00'), (
                               201, 119, 201, 100, 1, '2022-09-09 00:00:00', '2022-09-11 00:00:00',
                               '2022-09-16 00:00:00',
                               '2022-09-09 00:00:00'), (
                               202, 119, 201, 101, 1, '2022-09-09 00:00:00', '2022-09-11 00:00:00',
                               '2022-09-16 00:00:00',
                               '2022-09-09 00:00:00'), (
                               203, 119, 201, 102, 1, '2022-09-09 00:00:00', '2022-09-11 00:00:00',
                               '2022-09-16 00:00:00',
                               '2022-09-09 00:00:00'), (
                               204, 119, 201, 103, 1, '2022-09-09 00:00:00', '2022-09-11 00:00:00',
                               '2022-09-16 00:00:00',
                               '2022-09-09 00:00:00'), (
                               205, 119, 201, 104, 1, '2022-09-09 00:00:00', '2022-09-11 00:00:00',
                               '2022-09-16 00:00:00',
                               '2022-09-09 00:00:00'), (
                               206, 119, 201, 105, 1, '2022-09-09 00:00:00', '2022-09-11 00:00:00',
                               '2022-09-16 00:00:00',
                               '2022-09-09 00:00:00'), (
                               207, 119, 201, 106, 1, '2022-09-09 00:00:00', '2022-09-11 00:00:00',
                               '2022-09-16 00:00:00',
                               '2022-09-09 00:00:00'), (
                               208, 119, 201, 107, 1, '2022-09-09 00:00:00', '2022-09-11 00:00:00',
                               '2022-09-16 00:00:00',
                               '2022-09-09 00:00:00'), (
                               209, 119, 201, 108, 1, '2022-09-09 00:00:00', '2022-09-11 00:00:00',
                               '2022-09-16 00:00:00',
                               '2022-09-09 00:00:00'), (
                               210, 119, 201, 109, 1, '2022-09-09 00:00:00', '2022-09-11 00:00:00',
                               '2022-09-16 00:00:00',
                               '2022-09-09 00:00:00'), (
                               211, 119, 201, 110, 1, '2022-09-10 00:00:00', '2022-09-12 00:00:00',
                               '2022-09-17 00:00:00',
                               '2022-09-10 00:00:00'), (
                               212, 119, 201, 111, 1, '2022-09-10 00:00:00', '2022-09-12 00:00:00',
                               '2022-09-17 00:00:00',
                               '2022-09-10 00:00:00'), (
                               213, 119, 201, 112, 1, '2022-09-10 00:00:00', '2022-09-12 00:00:00',
                               '2022-09-17 00:00:00',
                               '2022-09-10 00:00:00'), (
                               214, 119, 201, 113, 1, '2022-09-10 00:00:00', '2022-09-12 00:00:00',
                               '2022-09-17 00:00:00',
                               '2022-09-10 00:00:00'), (
                               215, 119, 201, 114, 1, '2022-09-10 00:00:00', '2022-09-12 00:00:00',
                               '2022-09-17 00:00:00',
                               '2022-09-10 00:00:00'), (
                               216, 119, 201, 115, 1, '2022-09-10 00:00:00', '2022-09-12 00:00:00',
                               '2022-09-17 00:00:00',
                               '2022-09-10 00:00:00'), (
                               217, 119, 201, 116, 1, '2022-09-10 00:00:00', '2022-09-12 00:00:00',
                               '2022-09-17 00:00:00',
                               '2022-09-10 00:00:00'), (
                               218, 119, 201, 117, 1, '2022-09-10 00:00:00', '2022-09-12 00:00:00',
                               '2022-09-17 00:00:00',
                               '2022-09-10 00:00:00'), (
                               219, 119, 201, 118, 1, '2022-09-10 00:00:00', '2022-09-12 00:00:00',
                               '2022-09-17 00:00:00',
                               '2022-09-10 00:00:00'), (
                               220, 119, 201, 119, 1, '2022-09-10 00:00:00', '2022-09-12 00:00:00',
                               '2022-09-17 00:00:00',
                               '2022-09-10 00:00:00'), (
                               221, 119, 201, 100, 1, '2022-09-11 00:00:00', '2022-09-13 00:00:00',
                               '2022-09-18 00:00:00',
                               '2022-09-11 00:00:00'), (
                               222, 119, 201, 101, 1, '2022-09-11 00:00:00', '2022-09-13 00:00:00',
                               '2022-09-18 00:00:00',
                               '2022-09-11 00:00:00'), (
                               223, 119, 201, 102, 1, '2022-09-11 00:00:00', '2022-09-13 00:00:00',
                               '2022-09-18 00:00:00',
                               '2022-09-11 00:00:00'), (
                               224, 119, 201, 103, 1, '2022-09-11 00:00:00', '2022-09-13 00:00:00',
                               '2022-09-18 00:00:00',
                               '2022-09-11 00:00:00'), (
                               225, 119, 201, 104, 1, '2022-09-11 00:00:00', '2022-09-13 00:00:00',
                               '2022-09-18 00:00:00',
                               '2022-09-11 00:00:00'), (
                               226, 119, 201, 105, 1, '2022-09-11 00:00:00', '2022-09-13 00:00:00',
                               '2022-09-18 00:00:00',
                               '2022-09-11 00:00:00'), (
                               227, 119, 201, 106, 1, '2022-09-11 00:00:00', '2022-09-13 00:00:00',
                               '2022-09-18 00:00:00',
                               '2022-09-11 00:00:00'), (
                               228, 119, 201, 107, 1, '2022-09-11 00:00:00', '2022-09-13 00:00:00',
                               '2022-09-18 00:00:00',
                               '2022-09-11 00:00:00'), (
                               229, 119, 201, 108, 1, '2022-09-11 00:00:00', '2022-09-13 00:00:00',
                               '2022-09-18 00:00:00',
                               '2022-09-11 00:00:00'), (
                               230, 119, 201, 109, 1, '2022-09-11 00:00:00', '2022-09-13 00:00:00',
                               '2022-09-18 00:00:00',
                               '2022-09-11 00:00:00'), (
                               231, 119, 201, 110, 1, '2022-09-12 00:00:00', '2022-09-14 00:00:00',
                               '2022-09-19 00:00:00',
                               '2022-09-12 00:00:00'), (
                               232, 119, 201, 111, 1, '2022-09-12 00:00:00', '2022-09-14 00:00:00',
                               '2022-09-19 00:00:00',
                               '2022-09-12 00:00:00'), (
                               233, 119, 201, 112, 1, '2022-09-12 00:00:00', '2022-09-14 00:00:00',
                               '2022-09-19 00:00:00',
                               '2022-09-12 00:00:00'), (
                               234, 119, 201, 113, 1, '2022-09-12 00:00:00', '2022-09-14 00:00:00',
                               '2022-09-19 00:00:00',
                               '2022-09-12 00:00:00'), (
                               235, 119, 201, 114, 1, '2022-09-12 00:00:00', '2022-09-14 00:00:00',
                               '2022-09-19 00:00:00',
                               '2022-09-12 00:00:00'), (
                               236, 119, 201, 115, 1, '2022-09-12 00:00:00', '2022-09-14 00:00:00',
                               '2022-09-19 00:00:00',
                               '2022-09-12 00:00:00'), (
                               237, 119, 201, 116, 1, '2022-09-12 00:00:00', '2022-09-14 00:00:00',
                               '2022-09-19 00:00:00',
                               '2022-09-12 00:00:00'), (
                               238, 119, 201, 117, 1, '2022-09-12 00:00:00', '2022-09-14 00:00:00',
                               '2022-09-19 00:00:00',
                               '2022-09-12 00:00:00'), (
                               239, 119, 201, 118, 1, '2022-09-12 00:00:00', '2022-09-14 00:00:00',
                               '2022-09-19 00:00:00',
                               '2022-09-12 00:00:00'), (
                               240, 119, 201, 119, 1, '2022-09-12 00:00:00', '2022-09-14 00:00:00',
                               '2022-09-19 00:00:00',
                               '2022-09-12 00:00:00'), (
                               241, 119, 201, 100, 1, '2022-09-13 00:00:00', '2022-09-15 00:00:00',
                               '2022-09-20 00:00:00',
                               '2022-09-13 00:00:00'), (
                               242, 119, 201, 101, 1, '2022-09-13 00:00:00', '2022-09-15 00:00:00',
                               '2022-09-20 00:00:00',
                               '2022-09-13 00:00:00'), (
                               243, 119, 201, 102, 1, '2022-09-13 00:00:00', '2022-09-15 00:00:00',
                               '2022-09-20 00:00:00',
                               '2022-09-13 00:00:00'), (
                               244, 119, 201, 103, 1, '2022-09-13 00:00:00', '2022-09-15 00:00:00',
                               '2022-09-20 00:00:00',
                               '2022-09-13 00:00:00'), (
                               245, 119, 201, 104, 1, '2022-09-13 00:00:00', '2022-09-15 00:00:00',
                               '2022-09-20 00:00:00',
                               '2022-09-13 00:00:00'), (
                               246, 119, 201, 105, 1, '2022-09-13 00:00:00', '2022-09-15 00:00:00',
                               '2022-09-20 00:00:00',
                               '2022-09-13 00:00:00'), (
                               247, 119, 201, 106, 1, '2022-09-13 00:00:00', '2022-09-15 00:00:00',
                               '2022-09-20 00:00:00',
                               '2022-09-13 00:00:00'), (
                               248, 119, 201, 107, 1, '2022-09-13 00:00:00', '2022-09-15 00:00:00',
                               '2022-09-20 00:00:00',
                               '2022-09-13 00:00:00'), (
                               249, 119, 201, 108, 1, '2022-09-13 00:00:00', '2022-09-15 00:00:00',
                               '2022-09-20 00:00:00',
                               '2022-09-13 00:00:00'), (
                               250, 119, 201, 109, 1, '2022-09-13 00:00:00', '2022-09-15 00:00:00',
                               '2022-09-20 00:00:00',
                               '2022-09-13 00:00:00'), (
                               251, 119, 201, 110, 1, '2022-09-14 00:00:00', '2022-09-16 00:00:00',
                               '2022-09-21 00:00:00',
                               '2022-09-14 00:00:00'), (
                               252, 119, 201, 111, 1, '2022-09-14 00:00:00', '2022-09-16 00:00:00',
                               '2022-09-21 00:00:00',
                               '2022-09-14 00:00:00'), (
                               253, 119, 201, 112, 1, '2022-09-14 00:00:00', '2022-09-16 00:00:00',
                               '2022-09-21 00:00:00',
                               '2022-09-14 00:00:00'), (
                               254, 119, 201, 113, 1, '2022-09-14 00:00:00', '2022-09-16 00:00:00',
                               '2022-09-21 00:00:00',
                               '2022-09-14 00:00:00'), (
                               255, 119, 201, 114, 1, '2022-09-14 00:00:00', '2022-09-16 00:00:00',
                               '2022-09-21 00:00:00',
                               '2022-09-14 00:00:00'), (
                               256, 119, 201, 115, 1, '2022-09-14 00:00:00', '2022-09-16 00:00:00',
                               '2022-09-21 00:00:00',
                               '2022-09-14 00:00:00'), (
                               257, 119, 201, 116, 1, '2022-09-14 00:00:00', '2022-09-16 00:00:00',
                               '2022-09-21 00:00:00',
                               '2022-09-14 00:00:00'), (
                               258, 119, 201, 117, 1, '2022-09-14 00:00:00', '2022-09-16 00:00:00',
                               '2022-09-21 00:00:00',
                               '2022-09-14 00:00:00'), (
                               259, 119, 201, 118, 1, '2022-09-14 00:00:00', '2022-09-16 00:00:00',
                               '2022-09-21 00:00:00',
                               '2022-09-14 00:00:00'), (
                               260, 119, 201, 119, 1, '2022-09-14 00:00:00', '2022-09-16 00:00:00',
                               '2022-09-21 00:00:00',
                               '2022-09-14 00:00:00'), (
                               261, 119, 201, 100, 1, '2022-09-15 00:00:00', '2022-09-17 00:00:00',
                               '2022-09-22 00:00:00',
                               '2022-09-15 00:00:00'), (
                               262, 119, 201, 101, 1, '2022-09-15 00:00:00', '2022-09-17 00:00:00',
                               '2022-09-22 00:00:00',
                               '2022-09-15 00:00:00'), (
                               263, 119, 201, 102, 1, '2022-09-15 00:00:00', '2022-09-17 00:00:00',
                               '2022-09-22 00:00:00',
                               '2022-09-15 00:00:00'), (
                               264, 119, 201, 103, 1, '2022-09-15 00:00:00', '2022-09-17 00:00:00',
                               '2022-09-22 00:00:00',
                               '2022-09-15 00:00:00'), (
                               265, 119, 201, 104, 1, '2022-09-15 00:00:00', '2022-09-17 00:00:00',
                               '2022-09-22 00:00:00',
                               '2022-09-15 00:00:00'), (
                               266, 119, 201, 105, 1, '2022-09-15 00:00:00', '2022-09-17 00:00:00',
                               '2022-09-22 00:00:00',
                               '2022-09-15 00:00:00'), (
                               267, 119, 201, 106, 1, '2022-09-15 00:00:00', '2022-09-17 00:00:00',
                               '2022-09-22 00:00:00',
                               '2022-09-15 00:00:00'), (
                               268, 119, 201, 107, 1, '2022-09-15 00:00:00', '2022-09-17 00:00:00',
                               '2022-09-22 00:00:00',
                               '2022-09-15 00:00:00'), (
                               269, 119, 201, 108, 1, '2022-09-15 00:00:00', '2022-09-17 00:00:00',
                               '2022-09-22 00:00:00',
                               '2022-09-15 00:00:00'), (
                               270, 119, 201, 109, 1, '2022-09-15 00:00:00', '2022-09-17 00:00:00',
                               '2022-09-22 00:00:00',
                               '2022-09-15 00:00:00'), (
                               271, 119, 201, 110, 1, '2022-09-16 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-23 00:00:00',
                               '2022-09-16 00:00:00'), (
                               272, 119, 201, 111, 1, '2022-09-16 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-23 00:00:00',
                               '2022-09-16 00:00:00'), (
                               273, 119, 201, 112, 1, '2022-09-16 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-23 00:00:00',
                               '2022-09-16 00:00:00'), (
                               274, 119, 201, 113, 1, '2022-09-16 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-23 00:00:00',
                               '2022-09-16 00:00:00'), (
                               275, 119, 201, 114, 1, '2022-09-16 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-23 00:00:00',
                               '2022-09-16 00:00:00'), (
                               276, 119, 201, 115, 1, '2022-09-16 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-23 00:00:00',
                               '2022-09-16 00:00:00'), (
                               277, 119, 201, 116, 1, '2022-09-16 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-23 00:00:00',
                               '2022-09-16 00:00:00'), (
                               278, 119, 201, 117, 1, '2022-09-16 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-23 00:00:00',
                               '2022-09-16 00:00:00'), (
                               279, 119, 201, 118, 1, '2022-09-16 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-23 00:00:00',
                               '2022-09-16 00:00:00'), (
                               280, 119, 201, 119, 1, '2022-09-16 00:00:00', '2022-09-18 00:00:00',
                               '2022-09-23 00:00:00',
                               '2022-09-16 00:00:00'), (
                               281, 119, 201, 100, 1, '2022-09-17 00:00:00', '2022-09-19 00:00:00',
                               '2022-09-24 00:00:00',
                               '2022-09-17 00:00:00'), (
                               282, 119, 201, 101, 1, '2022-09-17 00:00:00', '2022-09-19 00:00:00',
                               '2022-09-24 00:00:00',
                               '2022-09-17 00:00:00'), (
                               283, 119, 201, 102, 1, '2022-09-17 00:00:00', '2022-09-19 00:00:00',
                               '2022-09-24 00:00:00',
                               '2022-09-17 00:00:00'), (
                               284, 119, 201, 103, 1, '2022-09-17 00:00:00', '2022-09-19 00:00:00',
                               '2022-09-24 00:00:00',
                               '2022-09-17 00:00:00'), (
                               285, 119, 201, 104, 1, '2022-09-17 00:00:00', '2022-09-19 00:00:00',
                               '2022-09-24 00:00:00',
                               '2022-09-17 00:00:00'), (
                               286, 119, 201, 105, 1, '2022-09-17 00:00:00', '2022-09-19 00:00:00',
                               '2022-09-24 00:00:00',
                               '2022-09-17 00:00:00'), (
                               287, 119, 201, 106, 1, '2022-09-17 00:00:00', '2022-09-19 00:00:00',
                               '2022-09-24 00:00:00',
                               '2022-09-17 00:00:00'), (
                               288, 119, 201, 107, 1, '2022-09-17 00:00:00', '2022-09-19 00:00:00',
                               '2022-09-24 00:00:00',
                               '2022-09-17 00:00:00'), (
                               289, 119, 201, 108, 1, '2022-09-17 00:00:00', '2022-09-19 00:00:00',
                               '2022-09-24 00:00:00',
                               '2022-09-17 00:00:00'), (
                               290, 119, 201, 109, 1, '2022-09-17 00:00:00', '2022-09-19 00:00:00',
                               '2022-09-24 00:00:00',
                               '2022-09-17 00:00:00'), (
                               291, 119, 201, 110, 1, '2022-09-18 00:00:00', '2022-09-20 00:00:00',
                               '2022-09-25 00:00:00',
                               '2022-09-18 00:00:00'), (
                               292, 119, 201, 111, 1, '2022-09-18 00:00:00', '2022-09-20 00:00:00',
                               '2022-09-25 00:00:00',
                               '2022-09-18 00:00:00'), (
                               293, 119, 201, 112, 1, '2022-09-18 00:00:00', '2022-09-20 00:00:00',
                               '2022-09-25 00:00:00',
                               '2022-09-18 00:00:00'), (
                               294, 119, 201, 113, 1, '2022-09-18 00:00:00', '2022-09-20 00:00:00',
                               '2022-09-25 00:00:00',
                               '2022-09-18 00:00:00'), (
                               295, 119, 201, 114, 1, '2022-09-18 00:00:00', '2022-09-20 00:00:00',
                               '2022-09-25 00:00:00',
                               '2022-09-18 00:00:00'), (
                               296, 119, 201, 115, 1, '2022-09-18 00:00:00', '2022-09-20 00:00:00',
                               '2022-09-25 00:00:00',
                               '2022-09-18 00:00:00'), (
                               297, 119, 201, 116, 1, '2022-09-18 00:00:00', '2022-09-20 00:00:00',
                               '2022-09-25 00:00:00',
                               '2022-09-18 00:00:00'), (
                               298, 119, 201, 117, 1, '2022-09-18 00:00:00', '2022-09-20 00:00:00',
                               '2022-09-25 00:00:00',
                               '2022-09-18 00:00:00'), (
                               299, 119, 201, 118, 1, '2022-09-18 00:00:00', '2022-09-20 00:00:00',
                               '2022-09-25 00:00:00',
                               '2022-09-18 00:00:00'), (
                               300, 119, 201, 119, 1, '2022-09-18 00:00:00', '2022-09-20 00:00:00',
                               '2022-09-25 00:00:00',
                               '2022-09-18 00:00:00'), (
                               301, 119, 201, 100, 1, '2022-09-19 00:00:00', '2022-09-21 00:00:00',
                               '2022-09-26 00:00:00',
                               '2022-09-19 00:00:00'), (
                               302, 119, 201, 101, 1, '2022-09-19 00:00:00', '2022-09-21 00:00:00',
                               '2022-09-26 00:00:00',
                               '2022-09-19 00:00:00'), (
                               303, 119, 201, 102, 1, '2022-09-19 00:00:00', '2022-09-21 00:00:00',
                               '2022-09-26 00:00:00',
                               '2022-09-19 00:00:00'), (
                               304, 119, 201, 103, 1, '2022-09-19 00:00:00', '2022-09-21 00:00:00',
                               '2022-09-26 00:00:00',
                               '2022-09-19 00:00:00'), (
                               305, 119, 201, 104, 1, '2022-09-19 00:00:00', '2022-09-21 00:00:00',
                               '2022-09-26 00:00:00',
                               '2022-09-19 00:00:00'), (
                               306, 119, 201, 105, 1, '2022-09-19 00:00:00', '2022-09-21 00:00:00',
                               '2022-09-26 00:00:00',
                               '2022-09-19 00:00:00'), (
                               307, 119, 201, 106, 1, '2022-09-19 00:00:00', '2022-09-21 00:00:00',
                               '2022-09-26 00:00:00',
                               '2022-09-19 00:00:00'), (
                               308, 119, 201, 107, 1, '2022-09-19 00:00:00', '2022-09-21 00:00:00',
                               '2022-09-26 00:00:00',
                               '2022-09-19 00:00:00'), (
                               309, 119, 201, 108, 1, '2022-09-19 00:00:00', '2022-09-21 00:00:00',
                               '2022-09-26 00:00:00',
                               '2022-09-19 00:00:00'), (
                               310, 119, 201, 109, 1, '2022-09-19 00:00:00', '2022-09-21 00:00:00',
                               '2022-09-26 00:00:00',
                               '2022-09-19 00:00:00'), (
                               311, 119, 201, 110, 1, '2022-09-20 00:00:00', '2022-09-22 00:00:00',
                               '2022-09-27 00:00:00',
                               '2022-09-20 00:00:00'), (
                               312, 119, 201, 111, 1, '2022-09-20 00:00:00', '2022-09-22 00:00:00',
                               '2022-09-27 00:00:00',
                               '2022-09-20 00:00:00'), (
                               313, 119, 201, 112, 1, '2022-09-20 00:00:00', '2022-09-22 00:00:00',
                               '2022-09-27 00:00:00',
                               '2022-09-20 00:00:00'), (
                               314, 119, 201, 113, 1, '2022-09-20 00:00:00', '2022-09-22 00:00:00',
                               '2022-09-27 00:00:00',
                               '2022-09-20 00:00:00'), (
                               315, 119, 201, 114, 1, '2022-09-20 00:00:00', '2022-09-22 00:00:00',
                               '2022-09-27 00:00:00',
                               '2022-09-20 00:00:00'), (
                               316, 119, 201, 115, 1, '2022-09-20 00:00:00', '2022-09-22 00:00:00',
                               '2022-09-27 00:00:00',
                               '2022-09-20 00:00:00'), (
                               317, 119, 201, 116, 1, '2022-09-20 00:00:00', '2022-09-22 00:00:00',
                               '2022-09-27 00:00:00',
                               '2022-09-20 00:00:00'), (
                               318, 119, 201, 117, 1, '2022-09-20 00:00:00', '2022-09-22 00:00:00',
                               '2022-09-27 00:00:00',
                               '2022-09-20 00:00:00'), (
                               319, 119, 201, 118, 1, '2022-09-20 00:00:00', '2022-09-22 00:00:00',
                               '2022-09-27 00:00:00',
                               '2022-09-20 00:00:00'), (
                               320, 119, 201, 119, 1, '2022-09-20 00:00:00', '2022-09-22 00:00:00',
                               '2022-09-27 00:00:00',
                               '2022-09-20 00:00:00'), (
                               321, 119, 201, 100, 1, '2022-09-21 00:00:00', '2022-09-23 00:00:00',
                               '2022-09-28 00:00:00',
                               '2022-09-21 00:00:00'), (
                               322, 119, 201, 101, 1, '2022-09-21 00:00:00', '2022-09-23 00:00:00',
                               '2022-09-28 00:00:00',
                               '2022-09-21 00:00:00'), (
                               323, 119, 201, 102, 1, '2022-09-21 00:00:00', '2022-09-23 00:00:00',
                               '2022-09-28 00:00:00',
                               '2022-09-21 00:00:00'), (
                               324, 119, 201, 103, 1, '2022-09-21 00:00:00', '2022-09-23 00:00:00',
                               '2022-09-28 00:00:00',
                               '2022-09-21 00:00:00'), (
                               325, 119, 201, 104, 1, '2022-09-21 00:00:00', '2022-09-23 00:00:00',
                               '2022-09-28 00:00:00',
                               '2022-09-21 00:00:00'), (
                               326, 119, 201, 105, 1, '2022-09-21 00:00:00', '2022-09-23 00:00:00',
                               '2022-09-28 00:00:00',
                               '2022-09-21 00:00:00'), (
                               327, 119, 201, 106, 1, '2022-09-21 00:00:00', '2022-09-23 00:00:00',
                               '2022-09-28 00:00:00',
                               '2022-09-21 00:00:00'), (
                               328, 119, 201, 107, 1, '2022-09-21 00:00:00', '2022-09-23 00:00:00',
                               '2022-09-28 00:00:00',
                               '2022-09-21 00:00:00'), (
                               329, 119, 201, 108, 1, '2022-09-21 00:00:00', '2022-09-23 00:00:00',
                               '2022-09-28 00:00:00',
                               '2022-09-21 00:00:00'), (
                               330, 119, 201, 109, 1, '2022-09-21 00:00:00', '2022-09-23 00:00:00',
                               '2022-09-28 00:00:00',
                               '2022-09-21 00:00:00'), (
                               331, 119, 201, 110, 1, '2022-09-22 00:00:00', '2022-09-24 00:00:00',
                               '2022-09-29 00:00:00',
                               '2022-09-22 00:00:00'), (
                               332, 119, 201, 111, 1, '2022-09-22 00:00:00', '2022-09-24 00:00:00',
                               '2022-09-29 00:00:00',
                               '2022-09-22 00:00:00'), (
                               333, 119, 201, 112, 1, '2022-09-22 00:00:00', '2022-09-24 00:00:00',
                               '2022-09-29 00:00:00',
                               '2022-09-22 00:00:00'), (
                               334, 119, 201, 113, 1, '2022-09-22 00:00:00', '2022-09-24 00:00:00',
                               '2022-09-29 00:00:00',
                               '2022-09-22 00:00:00'), (
                               335, 119, 201, 114, 1, '2022-09-22 00:00:00', '2022-09-24 00:00:00',
                               '2022-09-29 00:00:00',
                               '2022-09-22 00:00:00'), (
                               336, 119, 201, 115, 1, '2022-09-22 00:00:00', '2022-09-24 00:00:00',
                               '2022-09-29 00:00:00',
                               '2022-09-22 00:00:00'), (
                               337, 119, 201, 116, 1, '2022-09-22 00:00:00', '2022-09-24 00:00:00',
                               '2022-09-29 00:00:00',
                               '2022-09-22 00:00:00'), (
                               338, 119, 201, 117, 1, '2022-09-22 00:00:00', '2022-09-24 00:00:00',
                               '2022-09-29 00:00:00',
                               '2022-09-22 00:00:00'), (
                               339, 119, 201, 118, 1, '2022-09-22 00:00:00', '2022-09-24 00:00:00',
                               '2022-09-29 00:00:00',
                               '2022-09-22 00:00:00'), (
                               340, 119, 201, 119, 1, '2022-09-22 00:00:00', '2022-09-24 00:00:00',
                               '2022-09-29 00:00:00',
                               '2022-09-22 00:00:00'), (
                               341, 119, 201, 100, 1, '2022-09-23 00:00:00', '2022-09-25 00:00:00',
                               '2022-09-30 00:00:00',
                               '2022-09-23 00:00:00'), (
                               342, 119, 201, 101, 1, '2022-09-23 00:00:00', '2022-09-25 00:00:00',
                               '2022-09-30 00:00:00',
                               '2022-09-23 00:00:00'), (
                               343, 119, 201, 102, 1, '2022-09-23 00:00:00', '2022-09-25 00:00:00',
                               '2022-09-30 00:00:00',
                               '2022-09-23 00:00:00'), (
                               344, 119, 201, 103, 1, '2022-09-23 00:00:00', '2022-09-25 00:00:00',
                               '2022-09-30 00:00:00',
                               '2022-09-23 00:00:00'), (
                               345, 119, 201, 104, 1, '2022-09-23 00:00:00', '2022-09-25 00:00:00',
                               '2022-09-30 00:00:00',
                               '2022-09-23 00:00:00'), (
                               346, 119, 201, 105, 1, '2022-09-23 00:00:00', '2022-09-25 00:00:00',
                               '2022-09-30 00:00:00',
                               '2022-09-23 00:00:00'), (
                               347, 119, 201, 106, 1, '2022-09-23 00:00:00', '2022-09-25 00:00:00',
                               '2022-09-30 00:00:00',
                               '2022-09-23 00:00:00'), (
                               348, 119, 201, 107, 1, '2022-09-23 00:00:00', '2022-09-25 00:00:00',
                               '2022-09-30 00:00:00',
                               '2022-09-23 00:00:00'), (
                               349, 119, 201, 108, 1, '2022-09-23 00:00:00', '2022-09-25 00:00:00',
                               '2022-09-30 00:00:00',
                               '2022-09-23 00:00:00'), (
                               350, 119, 201, 109, 1, '2022-09-23 00:00:00', '2022-09-25 00:00:00',
                               '2022-09-30 00:00:00',
                               '2022-09-23 00:00:00'), (
                               351, 119, 201, 110, 1, '2022-09-24 00:00:00', '2022-09-26 00:00:00',
                               '2022-10-01 00:00:00',
                               '2022-09-24 00:00:00'), (
                               352, 119, 201, 111, 1, '2022-09-24 00:00:00', '2022-09-26 00:00:00',
                               '2022-10-01 00:00:00',
                               '2022-09-24 00:00:00'), (
                               353, 119, 201, 112, 1, '2022-09-24 00:00:00', '2022-09-26 00:00:00',
                               '2022-10-01 00:00:00',
                               '2022-09-24 00:00:00'), (
                               354, 119, 201, 113, 1, '2022-09-24 00:00:00', '2022-09-26 00:00:00',
                               '2022-10-01 00:00:00',
                               '2022-09-24 00:00:00'), (
                               355, 119, 201, 114, 1, '2022-09-24 00:00:00', '2022-09-26 00:00:00',
                               '2022-10-01 00:00:00',
                               '2022-09-24 00:00:00'), (
                               356, 119, 201, 115, 1, '2022-09-24 00:00:00', '2022-09-26 00:00:00',
                               '2022-10-01 00:00:00',
                               '2022-09-24 00:00:00'), (
                               357, 119, 201, 116, 1, '2022-09-24 00:00:00', '2022-09-26 00:00:00',
                               '2022-10-01 00:00:00',
                               '2022-09-24 00:00:00'), (
                               358, 119, 201, 117, 1, '2022-09-24 00:00:00', '2022-09-26 00:00:00',
                               '2022-10-01 00:00:00',
                               '2022-09-24 00:00:00'), (
                               359, 119, 201, 118, 1, '2022-09-24 00:00:00', '2022-09-26 00:00:00',
                               '2022-10-01 00:00:00',
                               '2022-09-24 00:00:00'), (
                               360, 119, 201, 119, 1, '2022-09-24 00:00:00', '2022-09-26 00:00:00',
                               '2022-10-01 00:00:00',
                               '2022-09-24 00:00:00'), (
                               361, 119, 201, 100, 1, '2022-09-25 00:00:00', '2022-09-27 00:00:00',
                               '2022-10-02 00:00:00',
                               '2022-09-25 00:00:00'), (
                               362, 119, 201, 101, 1, '2022-09-25 00:00:00', '2022-09-27 00:00:00',
                               '2022-10-02 00:00:00',
                               '2022-09-25 00:00:00'), (
                               363, 119, 201, 102, 1, '2022-09-25 00:00:00', '2022-09-27 00:00:00',
                               '2022-10-02 00:00:00',
                               '2022-09-25 00:00:00'), (
                               364, 119, 201, 103, 1, '2022-09-25 00:00:00', '2022-09-27 00:00:00',
                               '2022-10-02 00:00:00',
                               '2022-09-25 00:00:00'), (
                               365, 119, 201, 104, 1, '2022-09-25 00:00:00', '2022-09-27 00:00:00',
                               '2022-10-02 00:00:00',
                               '2022-09-25 00:00:00'), (
                               366, 119, 201, 105, 1, '2022-09-25 00:00:00', '2022-09-27 00:00:00',
                               '2022-10-02 00:00:00',
                               '2022-09-25 00:00:00'), (
                               367, 119, 201, 106, 1, '2022-09-25 00:00:00', '2022-09-27 00:00:00',
                               '2022-10-02 00:00:00',
                               '2022-09-25 00:00:00'), (
                               368, 119, 201, 107, 1, '2022-09-25 00:00:00', '2022-09-27 00:00:00',
                               '2022-10-02 00:00:00',
                               '2022-09-25 00:00:00'), (
                               369, 119, 201, 108, 1, '2022-09-25 00:00:00', '2022-09-27 00:00:00',
                               '2022-10-02 00:00:00',
                               '2022-09-25 00:00:00'), (
                               370, 119, 201, 109, 1, '2022-09-25 00:00:00', '2022-09-27 00:00:00',
                               '2022-10-02 00:00:00',
                               '2022-09-25 00:00:00'), (
                               371, 119, 201, 110, 1, '2022-09-26 00:00:00', '2022-09-28 00:00:00',
                               '2022-10-03 00:00:00',
                               '2022-09-26 00:00:00'), (
                               372, 119, 201, 111, 1, '2022-09-26 00:00:00', '2022-09-28 00:00:00',
                               '2022-10-03 00:00:00',
                               '2022-09-26 00:00:00'), (
                               373, 119, 201, 112, 1, '2022-09-26 00:00:00', '2022-09-28 00:00:00',
                               '2022-10-03 00:00:00',
                               '2022-09-26 00:00:00'), (
                               374, 119, 201, 113, 1, '2022-09-26 00:00:00', '2022-09-28 00:00:00',
                               '2022-10-03 00:00:00',
                               '2022-09-26 00:00:00'), (
                               375, 119, 201, 114, 1, '2022-09-26 00:00:00', '2022-09-28 00:00:00',
                               '2022-10-03 00:00:00',
                               '2022-09-26 00:00:00'), (
                               376, 119, 201, 115, 1, '2022-09-26 00:00:00', '2022-09-28 00:00:00',
                               '2022-10-03 00:00:00',
                               '2022-09-26 00:00:00'), (
                               377, 119, 201, 116, 1, '2022-09-26 00:00:00', '2022-09-28 00:00:00',
                               '2022-10-03 00:00:00',
                               '2022-09-26 00:00:00'), (
                               378, 119, 201, 117, 1, '2022-09-26 00:00:00', '2022-09-28 00:00:00',
                               '2022-10-03 00:00:00',
                               '2022-09-26 00:00:00'), (
                               379, 119, 201, 118, 1, '2022-09-26 00:00:00', '2022-09-28 00:00:00',
                               '2022-10-03 00:00:00',
                               '2022-09-26 00:00:00'), (
                               380, 119, 201, 119, 1, '2022-09-26 00:00:00', '2022-09-28 00:00:00',
                               '2022-10-03 00:00:00',
                               '2022-09-26 00:00:00'), (
                               381, 119, 201, 100, 1, '2022-09-27 00:00:00', '2022-09-29 00:00:00',
                               '2022-10-04 00:00:00',
                               '2022-09-27 00:00:00'), (
                               382, 119, 201, 101, 1, '2022-09-27 00:00:00', '2022-09-29 00:00:00',
                               '2022-10-04 00:00:00',
                               '2022-09-27 00:00:00'), (
                               383, 119, 201, 102, 1, '2022-09-27 00:00:00', '2022-09-29 00:00:00',
                               '2022-10-04 00:00:00',
                               '2022-09-27 00:00:00'), (
                               384, 119, 201, 103, 1, '2022-09-27 00:00:00', '2022-09-29 00:00:00',
                               '2022-10-04 00:00:00',
                               '2022-09-27 00:00:00'), (
                               385, 119, 201, 104, 1, '2022-09-27 00:00:00', '2022-09-29 00:00:00',
                               '2022-10-04 00:00:00',
                               '2022-09-27 00:00:00'), (
                               386, 119, 201, 105, 1, '2022-09-27 00:00:00', '2022-09-29 00:00:00',
                               '2022-10-04 00:00:00',
                               '2022-09-27 00:00:00'), (
                               387, 119, 201, 106, 1, '2022-09-27 00:00:00', '2022-09-29 00:00:00',
                               '2022-10-04 00:00:00',
                               '2022-09-27 00:00:00'), (
                               388, 119, 201, 107, 1, '2022-09-27 00:00:00', '2022-09-29 00:00:00',
                               '2022-10-04 00:00:00',
                               '2022-09-27 00:00:00'), (
                               389, 119, 201, 108, 1, '2022-09-27 00:00:00', '2022-09-29 00:00:00',
                               '2022-10-04 00:00:00',
                               '2022-09-27 00:00:00'), (
                               390, 119, 201, 109, 1, '2022-09-27 00:00:00', '2022-09-29 00:00:00',
                               '2022-10-04 00:00:00',
                               '2022-09-27 00:00:00'), (
                               391, 119, 201, 110, 1, '2022-09-28 00:00:00', '2022-09-30 00:00:00',
                               '2022-10-05 00:00:00',
                               '2022-09-28 00:00:00'), (
                               392, 119, 201, 111, 1, '2022-09-28 00:00:00', '2022-09-30 00:00:00',
                               '2022-10-05 00:00:00',
                               '2022-09-28 00:00:00'), (
                               393, 119, 201, 112, 1, '2022-09-28 00:00:00', '2022-09-30 00:00:00',
                               '2022-10-05 00:00:00',
                               '2022-09-28 00:00:00'), (
                               394, 119, 201, 113, 1, '2022-09-28 00:00:00', '2022-09-30 00:00:00',
                               '2022-10-05 00:00:00',
                               '2022-09-28 00:00:00'), (
                               395, 119, 201, 114, 1, '2022-09-28 00:00:00', '2022-09-30 00:00:00',
                               '2022-10-05 00:00:00',
                               '2022-09-28 00:00:00'), (
                               396, 119, 201, 115, 1, '2022-09-28 00:00:00', '2022-09-30 00:00:00',
                               '2022-10-05 00:00:00',
                               '2022-09-28 00:00:00'), (
                               397, 119, 201, 116, 1, '2022-09-28 00:00:00', '2022-09-30 00:00:00',
                               '2022-10-05 00:00:00',
                               '2022-09-28 00:00:00'), (
                               398, 119, 201, 117, 1, '2022-09-28 00:00:00', '2022-09-30 00:00:00',
                               '2022-10-05 00:00:00',
                               '2022-09-28 00:00:00'), (
                               399, 119, 201, 118, 1, '2022-09-28 00:00:00', '2022-09-30 00:00:00',
                               '2022-10-05 00:00:00',
                               '2022-09-28 00:00:00'), (
                               400, 119, 201, 119, 1, '2022-09-28 00:00:00', '2022-09-30 00:00:00',
                               '2022-10-05 00:00:00',
                               '2022-09-28 00:00:00')]

        self.assertEqual(result, expected_result)

    # TODO test do get_rental_rate
    # TODO test do get_customers
    # TODO test do get_new_customers
    # TODO test do return_offset_fun
    # TODO test do daily_rentals
    # TODO test do weekend_check
    # TODO test do latest_date_fun
    # TODO test do latest_index
    # TODO test do get_free_cars
    # TODO test do get_rented_cars


def generate_sample(x, k):
    return x[:k]


def return_offset_stub(x):
    return [2 for _ in x]


def return_cust_id(x, weights, k):
    return x[:k]


def return_staff_id(x, y):
    return x


if __name__ == '__main__':
    unittest.main()
