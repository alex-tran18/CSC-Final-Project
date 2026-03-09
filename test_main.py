import csv
import unittest
from unittest import result

import main
from data import User
#sdjfd
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

    # Count Watch Reasons
    def test_count_watch_reasons_count1(self):
        result = main.count_watch_reasons(self.user)
        self.assertEqual(result["Habit"], 2)
        self.assertEqual(result["Procrastination"], 1)
        self.assertEqual(result["Entertainment"], 1)

    def test_count_watch_reasons_count2(self):
        self.assertEqual(main.count_watch_reasons([]), {})

    # summary test
    def test_build_summary_text(self):
        if hasattr(main, "build_summary_text"):
            result = main.build_summary_text(self.user)
            self.assertIn("Total users", result)
            self.assertIn("Overall average", text)

    # load_users test
    def test_load_users(self):
        filename = "test_data.csv"

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "user_id",
                    "total_time_spent",
                    "productivity_loss",
                    "watch_reason",
                    "Debt"
                ]
            )
            writer.writeheader()
            writer.writerow({
                "user_id": "10",
                "total_time_spent": "150",
                "productivity_loss": "4",
                "watch_reason": "Boredom",
                "Debt": "true"
            })

        users = main.load_users(filename)

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].user_id, 10)
        self.assertTrue(users[0].debt)

if __name__ == "__main__":
    unittest.main()




