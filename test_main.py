import csv
import unittest
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