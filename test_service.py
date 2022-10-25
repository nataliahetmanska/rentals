import service
import unittest
import datetime

class TestServicesGenerator(unittest.TestCase):

    def test_get_cars_in_stock(self):
        service.interaction.connection = fake_connection_get_last_service_id
        service_date1 = datetime.datetime(2015, 2, 1, 0, 0)
        service_date2 = datetime.datetime(2017, 2, 1, 0, 0)
        service_date3 = datetime.datetime(2020, 2, 1, 0, 0)
        result1 = service.get_cars_in_stock(service_date1)
        result2 = service.get_cars_in_stock(service_date2)
        result3 = service.get_cars_in_stock(service_date3)
        self.assertEqual(result1, [])
        self.assertEqual(result2, [1, 2])
        self.assertEqual(result3, [3])




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