import main
import unittest
from datetime import datetime, date


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

        expected_result = main.csv_read('test_generate_rentals_happy_path')
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

    def test_insert_data_list_happy_path(self):
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
        result = main.insert_data_list(rental_list, latest_index_from_db, customers, new_customers, rental_rates)

        expected_result = main.csv_read('test_insert_data_list_happy_path')
        self.assertEqual(result, expected_result)

    def test_get_rental_rate(self):
        main.interaction.connection = fake_connection_get_rental_rate
        result = main.get_rental_rate()
        expected_result = {1: 2, 4: 3}
        self.assertEqual(result, expected_result)
        self.assertIsInstance(result, dict)

    def test_get_customers(self):
        main.interaction.connection = fake_connection_get_customers
        result = main.get_customers()

        good_order = False
        for customer in result:
            if customer[1] - 1 < customer[1]:
                good_order = True
        self.assertTrue(good_order)

        good_len = True
        for i in result:
            if len(i) != 3:
                good_len = False
                break
        self.assertTrue(good_len)
        self.assertIsInstance(result[0][2], datetime)

    def test_get_new_customers(self):
        main.interaction.connection = fake_connection_get_new_customers
        latest_date_from_db = datetime(2020, 11, 11, 0, 0)
        result = main.get_new_customers(latest_date_from_db)
        good_date = True
        for i in result:
            if i[1] < latest_date_from_db:
                good_date = False
                break
        self.assertTrue(good_date)

        good_len = True
        for i in result:
            if len(i) != 2:
                good_len = False
                break
        self.assertTrue(good_len)
        self.assertIsInstance(result[0][1], datetime)

    def test_get_latest_date(self):
        main.interaction.connection = fake_connection_get_latest_date
        result = main.get_latest_date()
        self.assertIsInstance(result, date)

    def test_get_latest_index(self):
        main.interaction.connection = fake_connection_get_latest_index
        result = main.get_latest_index()
        self.assertIsInstance(result, int)

    def test_get_free_cars(self):
        main.interaction.connection = fake_connection_get_cars
        latest_date = date(2022, 7, 22)
        result = main.get_free_cars(latest_date)
        expected_result = set()
        self.assertEqual(result, expected_result)

    def test_get_rented_cars(self):
        main.interaction.connection = fake_connection_get_cars
        latest_date = date(2022, 7, 22)
        result = main.get_rented_cars(latest_date)
        expected_result = {641}
        self.assertEqual(result, expected_result)

    def test_daily_rentals(self):
        last_date = date(2022, 1, 1)
        expected_num_days = 28
        multi, num_days = main.daily_rentals(last_date)
        self.assertEqual(expected_num_days, num_days)

    def test_weekend_check(self):
        days = [date(2022, 2, i) for i in range(1, 29)]
        n_daily = list()
        for i in days:
            if main.weekend_check(i):
                n_daily.append(1.5)
            else:
                n_daily.append(1)
        exp_n_daily = [1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5,
                       1]
        self.assertEqual(exp_n_daily, n_daily)

    def test_return_offset_fun_returns_list_with_x_len(self):
        x = [4, 4, 4, 4]
        result = main.return_offset_fun(x)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(x))


class FakeCursorGetRentalRate():
    def execute(self, _):
        pass

    def fetchall(self):
        return [(1, 2), (4, 3)]


class FakeCursorGetCustomers():
    def execute(self, _):
        pass

    def fetchall(self):
        return [(1, 2, datetime(2022, 6, 7, 0, 0)), (4, 3, datetime(2022, 5, 5, 0, 0))]


class FakeCursorGetNewCustomers():
    def execute(self, _):
        pass

    def fetchall(self):
        return [(1, datetime(2022, 6, 7, 0, 0)), (4, datetime(2022, 5, 5, 0, 0))]


class FakeCursorLatestDate():
    def execute(self, _):
        pass

    def fetchall(self):
        return [[date(2022, 1, 1)]]


class FakeCursorLatestIndex():
    def execute(self, _):
        pass

    def fetchall(self):
        return [[1]]


class FakeCursorGetCars():
    def execute(self, _):
        pass

    def fetchall(self):
        return [(641, date(2022, 7, 23), date(2022, 8, 2))]


def fake_connection_get_rental_rate():
    fake_cursor = FakeCursorGetRentalRate()
    return None, fake_cursor


def fake_connection_get_customers():
    fake_cursor = FakeCursorGetCustomers()
    return None, fake_cursor


def fake_connection_get_new_customers():
    fake_cursor = FakeCursorGetNewCustomers()
    return None, fake_cursor


def fake_connection_get_latest_date():
    fake_cursor = FakeCursorLatestDate()
    return None, fake_cursor


def fake_connection_get_latest_index():
    fake_cursor = FakeCursorLatestIndex()
    return None, fake_cursor


def fake_connection_get_cars():
    fake_cursor = FakeCursorGetCars()
    return None, fake_cursor


def generate_sample(x, k):
    return x[:k]


def return_offset_stub(x):
    return [2 for _ in x]


def return_cust_id(x, weights, k):
    return x[:k]


def return_staff_id(x, _):
    return x


if __name__ == '__main__':
    unittest.main()
