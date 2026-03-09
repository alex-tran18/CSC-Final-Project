import csv
import unittest
import main
from data import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.users = [
            User(1, 80, 3, True),
            User( 2, 228, 5, False),
            User(3, 30, 6, False),
            User(4, 101, 3, True)
        ]

    #user method tests
    def test_assign_usage_level_low(self):
        u = User(99, 80, 1, False)
        self.assertEqual(u.assign_usage_level(), "low")

    def test_assign_usage_level_medium(self):
        u = User(99, 150, 1, False)
        self.assertEqual(u.assign_usage_level(), "medium")

    def test_assign_usage_level_high(self):
        u = User(99, 250, 1, False)
        self.assertEqual(u.assign_usage_level(), "high")

    def test_calculate_productivity_ratio_normal(self):
        u = User(99, 100, 25, False)
        self.assertAlmostEqual(u.calculate_productivity_ratio(), 0.25, places = 3)

    def test_calculate_productivity_ratio_zero_time(self):
        u = User(99, 0, 25, False)
        self.assertEqual(u.calculate_productivity_ratio(), 0)

    def test_high_risk_true(self):
        u = User(99, 250, 25, True)
        self.assertTrue(u.high_risk())

    def test_high_risk_false(self):
        u = User(99, 80, 5, True)
        self.assertFalse(u.high_risk())

    def test_high_risk_no_debt(self):
        u = User(99, 250, 5, False)
        self.assertFalse(u.high_risk())

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

    #Correlation between screen time and debt
    def test_correlation_time_and_debt_empty(self):
        self.assertEqual(main.correlation_time_and_debt([]), 0)

    def test_correlation_time_and_debt_all_same_debt(self):
        users = [
            User(1, 10, 1,  True),
            User(2,50,1,  True),
            User(3, 100, 1,  True)

        ]
        self.assertEqual(main.correlation_time_and_debt(users), 0)

    def test_correlation_time_and_debt_positive(self):
        users = [
            User(1, 10, 1,  False),
            User(2, 20, 1,  False),
            User(3, 80, 1,  True),
            User(4, 100, 1, True)
        ]
        corr = main.correlation_time_and_debt(users)
        self.assertGreater(corr,0)

    def test_correlation_time_and_debt_negative(self):
        users = [
            User(1, 10, 1,True),
            User(2, 20, 1,True),
            User(3, 80, 1,False),
            User(4, 100, 1,False)
        ]
        corr = main.correlation_time_and_debt(users)
        self.assertLess(corr,0)

    #average time by debt case
    def test_average_time_by_debt_empty(self):
        result = main.average_time_by_debt([])
        self.assertEqual(result[0], 0)  # debt_avg
        self.assertEqual(result[1], 0)  # no_debt_avg
        self.assertEqual(result[2], 0)  # debt_count
        self.assertEqual(result[3], 0)  # no_debt_count

    def test_average_time_by_debt_mixed(self):
        users = [
            User(1, 100, 1, True),
            User(2, 300, 1, True),
            User(3, 50, 1,False),
            User(4, 150, 1, False),
        ]

        result = main.average_time_by_debt(users)
        debt_avg = result[0]
        no_debt_avg = result[1]
        debt_count = result[2]
        no_debt_count = result[3]

        self.assertAlmostEqual(debt_avg, 200.0, places=3)
        self.assertAlmostEqual(no_debt_avg, 100.0, places=3)

        self.assertEqual(debt_count, 2)
        self.assertEqual(no_debt_count, 2)

    def test_average_time_by_debt_all_debt(self):
        users = [
            User(1, 100, 1, True),
            User(2, 200, 1, True)
        ]

        result = main.average_time_by_debt(users)
        self.assertAlmostEqual(result[0], 150.0, places=3)
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], 2)
        self.assertEqual(result[3], 0)

    #debt and high screen time ratio
    def test

    def test_average_time_by_debt_no_debt(self):
        users = [
            User(1, 100, 1,False),
            User(2, 200, 1,False)
        ]

        result = main.average_time_by_debt(users)
        self.assertEqual(result[0], 0)
        self.assertAlmostEqual(result[1], 150.0, places=3)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 2)

    # summary test
    def test_build_summary_text(self):
        result = main.build_summary_text(self.users)
        self.assertIn("Total users", result)
        self.assertIn("Overall average", result)

    # load_users test
    def test_load_users(self):
        filename = "test_data.csv"

        with open(filename, "w", newline="",) as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "UserID",
                    "Total Time Spent",
                    "ProductivityLoss",
                    "Debt"
                ]
            )
            writer.writeheader()
            writer.writerow({
                "UserID": "10",
                "Total Time Spent": "150",
                "ProductivityLoss": "4",
                "Debt": "true"
            })

        users = main.load_users(filename)

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].user_id, 10)
        self.assertTrue(users[0].debt)

if __name__ == "__main__":
    unittest.main()



