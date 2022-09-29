import main
import unittest
from datetime import date, timedelta, datetime


class TestRentalGenerator(unittest.TestCase):

    def test_generate_rentals_happy_path(self):
        main.rnd.sample = generate_sample
        main.return_offset_fun = return_offset_stub
        latest_date = datetime.strptime("2022-08-30", '%Y-%m-%d')
        available = set(range(100, 200))

        month = 30
        daily_rent_wage = [1 for _ in range(month)]
        daily_rent_number = 10
        result = main.generate_rentals(available, latest_date, daily_rent_number, daily_rent_wage, month)

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
        result = main.generate_rentals(available, latest_date, daily_rent_number, daily_rent_wage, month)
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

        self.assertRaises(ValueError, main.generate_rentals, available, latest_date, daily_rent_number, daily_rent_wage,
                          month)

    def test_generating_with_negative_daily_rent_wages(self):
        main.rnd.sample = generate_sample
        main.return_offset_fun = return_offset_stub
        latest_date = datetime.strptime("2022-08-30", '%Y-%m-%d')
        available = set(range(100, 200))

        month = 30
        daily_rent_wage = [-1 for _ in range(month)]
        daily_rent_number = 10
        self.assertRaises(ValueError, main.generate_rentals, available, latest_date, daily_rent_number, daily_rent_wage, month)

    def test_if_the_same_car_is_not_rented_twice_at_the_same_time(self):
        main.rnd.sample = generate_sample
        main.return_offset_fun = return_offset_stub
        latest_date = datetime.strptime("2022-08-30", '%Y-%m-%d')
        available = set(range(100, 200))

        month = 30
        daily_rent_wage = [1 for _ in range(month)]
        daily_rent_number = 90

        result = main.generate_rentals(available, latest_date, daily_rent_number, daily_rent_wage,
                          month)

        rented = []
        for i in result[5]:
            rented.append(i["car_id"])

        rented_with_no_duplicates = list(set(rented))
        self.assertEqual(len(rented), len(rented_with_no_duplicates))


def generate_sample(x, k):
    return x[:k]


def return_offset_stub(x):
    return [2 for _ in x]


if __name__ == '__main__':
    unittest.main()
