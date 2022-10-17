import payment
import unittest
from decimal import Decimal
import datetime
from freezegun import freeze_time

class TesPaymentGenerator(unittest.TestCase):

    def test_payment_id(self):
        amount = 10
        result = payment.payment_id(amount)
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(result, expected_result)

    def test_payment_date(self):
        payment.rnd.randint = random_randint
        payment_deadline = [datetime.date(2017, 3, 4), datetime.date(2016, 2, 20), datetime.date(2016, 1, 16),
                            datetime.date(2016, 9, 9), datetime.date(2016, 7, 24), datetime.date(2016, 5, 8),
                            datetime.date(2016, 1, 9), datetime.date(2016, 12, 9), datetime.date(2016, 8, 14),
                            datetime.date(2016, 7, 18)]
        amt = 10
        result = payment.payment_date(payment_deadline, amt)
        expected_result = [datetime.date(2017, 3, 5), datetime.date(2016, 2, 21), datetime.date(2016, 1, 17),
                           datetime.date(2016, 9, 10), datetime.date(2016, 7, 25), datetime.date(2016, 5, 9),
                           datetime.date(2016, 1, 10), datetime.date(2016, 12, 10), datetime.date(2016, 8, 15),
                           datetime.date(2016, 7, 19)]
        self.assertEqual(result, expected_result)
        
    def test_pay_amount(self):

        rental_rate = [Decimal('149.00'), Decimal('149.00'), Decimal('279.00'), Decimal('149.00'), Decimal('189.00')]
        rental_date = [datetime.date(2017, 2, 25), datetime.date(2016, 2, 13), datetime.date(2016, 1, 2), datetime.date(2016, 9, 2), datetime.date(2016, 7, 17)]
        return_date = [datetime.date(2017, 2, 26), datetime.date(2016, 2, 17), datetime.date(2016, 1, 4), datetime.date(2016, 9, 6), datetime.date(2016, 7, 18)]
        result = payment.pay_amount(rental_rate, rental_date, return_date)
        expected_result = [Decimal('149.00'), Decimal('596.00'), Decimal('558.00'), Decimal('596.00'), Decimal('189.00')]
        self.assertEqual(result, expected_result)
        
    @freeze_time("Sep 29th, 2022")
    def test_last_update(self):

        payment.rnd.randint = random_randint
        rental_date = [datetime.date(2022, 9, 11), datetime.date(2022, 9, 14),
                       datetime.date(2022, 9, 17), datetime.date(2022, 9, 20), datetime.date(2022, 7, 21)]
        result = payment.last_update(rental_date)
        expected_result = [datetime.date(2022, 9, 12), datetime.date(2022, 9, 15),
                       datetime.date(2022, 9, 18), datetime.date(2022, 9, 21), datetime.date(2022, 7, 22)]
        self.assertEqual(result, expected_result)
        
        
    def test_get_rentals(self):
        payment.connection = fake_connection_get_rentals
        latest_date_from_db = datetime.date(2017, 3, 4)
        rental_id, rental_rate, customer_id, rental_date, return_date, payment_deadline, amount = payment.get_rentals(latest_date_from_db)
        self.assertEqual(rental_id, [1300001, 1300007])
        self.assertEqual(rental_rate, [Decimal('149.00'), Decimal('149.00')])
        self.assertEqual(customer_id, [94714, 89117])
        self.assertEqual(rental_date, [datetime.date(2017, 2, 25), datetime.date(2016, 2, 13)])
        self.assertEqual(return_date, [datetime.date(2017, 3, 6), datetime.date(2016, 2, 17)])
        self.assertEqual(payment_deadline, [datetime.date(2017, 3, 4), datetime.date(2016, 2, 20)])
        
    def test_max_payment_id(self):
        payment.connection = fake_connection_max_payment_id
        result = payment.max_payment_id()
        expected_result = 4
        self.assertEqual(result, expected_result)
        

def random_randint(x, y):
    return 1

def test_nice_datetime():
    assert date.today() == date(2022, 9, 29)
    
class FakeCursorGetRentals():
    def execute(self, _):
        pass

    def fetchall(self):
        return [(1300001, Decimal('149.00'), 94714, datetime.date(2017, 2, 25), datetime.date(2017, 3, 6), datetime.date(2017, 3, 4)),
                (1300007, Decimal('149.00'), 89117, datetime.date(2016, 2, 13), datetime.date(2016, 2, 17), datetime.date(2016, 2, 20))]

def fake_connection_get_rentals():
    fake_cursor = FakeCursorGetRentals()
    return None, fake_cursor

class FakeCursorMaxPaymentId():
    def execute(self, _):
        pass

    def fetchall(self):
        return [(1,), (2,), (3,), (4,)]

def fake_connection_max_payment_id():
    fake_cursor = FakeCursorMaxPaymentId()
    return None, fake_cursor

if __name__ == '__main__':
    unittest.main()
