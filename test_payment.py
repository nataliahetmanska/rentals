import payment
import unittest
from decimal import Decimal
import datetime


class TesPaymentGenerator(unittest.TestCase):

    def test_generating_payment_id(self):
        amount = 10
        result = payment.payment_id(amount)
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(result, expected_result)

    def test_generate_payment_date(self):
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

def random_randint(x, y):
    return 1


if __name__ == '__main__':
    unittest.main()
