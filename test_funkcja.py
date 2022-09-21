from funkcja import generate_rentals
import unittest
import random as rnd

class TestRentalGenerator(unittest.TestCase):

    def test_generate_rentals_happy_path (self):
        inv = set(range(30))
        rented = set(rnd.sample(range(30), k=20))
        daily_rentals = 5
        available = inv - rented

        result = generate_rentals(available, daily_rentals)

        self.assertIsInstance(result, list)


    def test_generate_rentals_when_nothing_is_rented(self):
        inv = set(range(30))
        rented = set(rnd.sample(range(30), k=20))
        daily_rentals = 0
        available = inv - rented

        result = generate_rentals(available, daily_rentals)

        self.assertEqual(result, [list() for _ in range(30)])



if __name__ == '__main__':

    unittest.main()


