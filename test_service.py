import services
from services import get_rented_cars
import unittest
import datetime
from freezegun import freeze_time


class TestServicesGenerator(unittest.TestCase):

    def test_get_cars_in_stock(self):
        services.interaction.connection = fake_connection_get_last_service_id
        service_date1 = datetime.datetime(2015, 2, 1, 0, 0)
        service_date2 = datetime.datetime(2017, 2, 1, 0, 0)
        service_date3 = datetime.datetime(2020, 2, 1, 0, 0)
        result1 = services.get_cars_in_stock(service_date1)
        result2 = services.get_cars_in_stock(service_date2)
        result3 = services.get_cars_in_stock(service_date3)
        self.assertEqual(result1, [])
        self.assertEqual(result2, [1, 2])
        self.assertEqual(result3, [3])

    def test_get_rented_cars(self):
        services.get_rented_cars = get_rented_cars
        services.interaction.connection = fake_connection_get_rented_cars
        service_date1 = datetime.datetime(2017, 2, 14, 0, 0)
        result = services.get_rented_cars(service_date1)
        expected_result = [{1: datetime.date(2017, 2, 16)}, {5: datetime.date(2017, 2, 22)},
                           {6: datetime.date(2017, 2, 15)}]
        self.assertEqual(result, expected_result)

    def test_check_if_car_is_rented(self):
        services.get_rented_cars = get_rented_cars_mp
        inv_id1 = 5
        inv_id2 = 3
        service_date = datetime.datetime(2017, 1, 10, 0, 0)
        result1 = services.check_if_car_is_rented(inv_id1, service_date)
        result2 = services.check_if_car_is_rented(inv_id2, service_date)
        expected_result_1 = 5, datetime.date(2017, 1, 11)
        expected_result_2 = 3, datetime.date(2017, 1, 10)
        self.assertEqual(result1, expected_result_1)
        self.assertEqual(result2, expected_result_2)

    @freeze_time("Aug 29th, 2018")
    def test_create_service_dates(self):
        expected_result = [datetime.datetime(2016, 7, 1, 0, 0), datetime.datetime(2017, 1, 3, 0, 0),
                           datetime.datetime(2017, 7, 8, 0, 0), datetime.datetime(2018, 1, 10, 0, 0),
                           datetime.datetime(2018, 7, 15, 0, 0)]
        result = services.create_service_dates()
        self.assertEqual(result, expected_result)

    @freeze_time("Aug 29th, 2018")
    def test_create_tire_change_dates(self):
        expected_result = [datetime.datetime(2016, 3, 15, 0, 0), datetime.datetime(2016, 11, 15, 0, 0),
                           datetime.datetime(2017, 3, 15, 0, 0), datetime.datetime(2017, 11, 15, 0, 0),
                           datetime.datetime(2018, 3, 15, 0, 0)]
        result = services.create_tire_change_dates()
        self.assertEqual(result, expected_result)


class FakeCursorLastServiceId():
    def execute(self, _):
        pass

    def fetchall(self):
        return [(1, datetime.datetime(2016, 1, 1, 0, 0), datetime.datetime(2018, 1, 1, 0, 0)),
                (2, datetime.datetime(2016, 1, 1, 0, 0), datetime.datetime(2018, 1, 1, 0, 0)),
                (3, datetime.datetime(2020, 1, 1, 0, 0), datetime.datetime(2020, 1, 1, 0, 0))]


def fake_connection_get_last_service_id():
    fake_cursor = FakeCursorLastServiceId()
    return None, fake_cursor


class FakeCursorRentedCars():
    def execute(self, _):
        pass

    def fetchall(self):
        return [(1, datetime.date(2017, 2, 13), datetime.date(2017, 2, 16)),
                (5, datetime.date(2017, 2, 14), datetime.date(2017, 2, 22)),
                (6, datetime.date(2017, 2, 14), datetime.date(2017, 2, 15)),
                (8, datetime.date(2017, 2, 16), datetime.date(2017, 2, 20))]


def fake_connection_get_rented_cars():
    fake_cursor = FakeCursorRentedCars()
    return None, fake_cursor


def test_datetime():
    assert datetime.date.today() == datetime.date(2018, 8, 29)


def get_rented_cars_mp(service_date):
    return [{1: datetime.date(2017, 1, 16)}, {5: datetime.date(2017, 1, 11)}, {6: datetime.date(2017, 1, 15)}]
