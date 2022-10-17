import main
import unittest
from datetime import date, datetime
from calendar import monthrange


class TestDailyRentals(unittest.TestCase):

    def test_num_days(self):

        last_date = date(2022, 1, 1)
        expected_num_days = 28
        multi, num_days = main.daily_rentals(last_date)

        self.assertEqual(expected_num_days, num_days)

    def test_next_month (self):
        last_date = date(2022, 1, 1)
        exp_month = 2
        next_month = last_date.month + 1

        self.assertEqual(exp_month, next_month)

    def test_year(self):
        last_date = date(2022, 1, 1)
        year = last_date.year
        exp_year = 2022

        self.assertEqual(exp_year, year)

    def test_days (self):
        year=2022
        next_month= 2
        num_days = 28

        days = [date(year, next_month, day) for day in range(1, num_days + 1)]

        exp_days =[date(2022, 2, 1), date(2022, 2, 2), date(2022, 2, 3), date(2022, 2, 4), date(2022, 2, 5),
                   date(2022, 2, 6), date(2022, 2, 7), date(2022, 2, 8), date(2022, 2, 9), date(2022, 2, 10),
                   date(2022, 2, 11), date(2022, 2, 12), date(2022, 2, 13), date(2022, 2, 14), date(2022, 2, 15),
                   date(2022, 2, 16), date(2022, 2, 17), date(2022, 2, 18), date(2022, 2, 19), date(2022, 2, 20),
                   date(2022, 2, 21), date(2022, 2, 22), date(2022, 2, 23), date(2022, 2, 24), date(2022, 2, 25),
                   date(2022, 2, 26), date(2022, 2, 27), date(2022, 2, 28)]

        self.assertEqual(days, exp_days)


    def test_N (self):

        n = 1
        next_month = 2

        if next_month in [7, 8]:
            N = 1.2
        else:
            N = 1

        self.assertEqual(n, N)

    def test_n_daily (self):

        days = [date(2022, 2, 1), date(2022, 2, 2), date(2022, 2, 3), date(2022, 2, 4), date(2022, 2, 5),
                   date(2022, 2, 6), date(2022, 2, 7), date(2022, 2, 8), date(2022, 2, 9), date(2022, 2, 10),
                   date(2022, 2, 11), date(2022, 2, 12), date(2022, 2, 13), date(2022, 2, 14), date(2022, 2, 15),
                   date(2022, 2, 16), date(2022, 2, 17), date(2022, 2, 18), date(2022, 2, 19), date(2022, 2, 20),
                   date(2022, 2, 21), date(2022, 2, 22), date(2022, 2, 23), date(2022, 2, 24), date(2022, 2, 25),
                   date(2022, 2, 26), date(2022, 2, 27), date(2022, 2, 28)]

        n_daily = list()

        for i in days:
            if main.weekend_check(i):
                n_daily.append(1.5)
            else:
                n_daily.append(1)

        exp_n_daily =[1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5, 1]

        self.assertEqual(exp_n_daily, n_daily)

    def test_multi(self):

        N = 1
        n_daily = [1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5,
                       1, 1, 1, 1, 1, 1.5, 1.5, 1]

        multi = [element * N for element in n_daily]

        self.assertEqual(n_daily, multi)

    def test_happy_path(self):

        last_date = date(2022, 1, 1)
        daily_rentals, num_days = main.daily_rentals(last_date)

        n_daily = [1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5,
                   1, 1, 1, 1, 1, 1.5, 1.5, 1]

        self.assertEqual(daily_rentals, n_daily)


    def test_next_month(self):

        last_date = date(2022, 12, 1)
        exp_next_month = 1

        if last_date.month != 12:
            next_month = last_date.month + 1

        else:
            next_month = 1

        self.assertEqual(next_month, exp_next_month)

    def test_next_year (self):

        last_date = date(2022, 12, 1)
        exp_year = 2023

        if last_date.month != 12:
            year = last_date.year
        else:
            year = last_date.year + 1

        self.assertEqual(year, exp_year)

    def test_month_in_summer (self):

        next_month = 7

        exp_N = 1.2

        if next_month in [7, 8]:
            N = 1.2
        else:
            N = 1

        self.assertEqual(exp_N, N)

    def test_multi_in_summer (self):

        N = 1.2


        n_daily = [1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5, 1, 1, 1, 1,
                   1, 1.5, 1.5, 1, 1, 1, 1, 1, 1.5, 1.5, 1]

        multi = [element * N for element in n_daily]

        exp_multi = [1.2, 1.2, 1.2, 1.2, 1.7999999999999998, 1.7999999999999998, 1.2, 1.2, 1.2, 1.2, 1.2, 1.7999999999999998, 1.7999999999999998, 1.2, 1.2, 1.2, 1.2, 1.2,
                     1.7999999999999998, 1.7999999999999998, 1.2, 1.2, 1.2, 1.2, 1.2, 1.7999999999999998, 1.7999999999999998, 1.2]

        self.assertEqual(multi, exp_multi)













