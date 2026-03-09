import csv
import unittest
from unittest import result

import main
from data import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = [
            User(1, 80, 3, "Procrastination", True),
            User( 2, 228, 5, "Habit", False),
            User(3, 30, 6, "Entertainment", False),
            User(4, 101, 3, "Habit", True)
        ]

# convert_bool tests
    def test_convert_bool_true(self):
        self.assertTrue(main.convert_bool("true"))
        self.assertTrue(main.convert_bool(" TRUE "))
        self.assertTrue(main.convert_bool(True))

    def test_convert_bool_false(self):
        self.assertFalse(main.convert_bool("false"))
        self.assertFalse(main.convert_bool(" FALSE "))
        self.assertFalse(main.convert_bool(False))

    def test_convert_bool_unexpected(self):
        self.assertFalse(main.convert_bool("maybe"))
        self.assertFalse(main.convert_bool(""))
        self.assertFalse(main.convert_bool(None))

# average_time tests
    def test_average_time_normal(self):
        avg = main.average_time(self.users)
        self.assertAlmostEqual(avg, 109.75, places = 2)

    def test_average_time_empty_list(self):
        self.assertEqual(main.average_time([]), 0)

#highest_and_lowest tests
    def test_highest_and_lowest_normal(self):
        result = main.highest_and_lowest(self.users)
        highest = result[0]
        lowest = result[1]

        self.assertEqual(highest.user_id, 2)
        self.assertEqual(lowest.user_id, 3)

    def test_highest_and_lowest_empty(self):
        result = main.highest_and_lowest([])
        highest = result[0]
        lowest = result[1]

        self.assertIsNone(highest)
        self.assertIsNone(lowest)


