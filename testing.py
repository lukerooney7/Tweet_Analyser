import unittest
from main import *

class TestClass(unittest.TestCase):

    def test_format_date_for_valid_input(self):
        new_date = datetime.datetime(2014, 12, 5, 18, 7)
        self.assertEqual(format_date("05/12/2014 18:07"), new_date)

    def test_format_date_for_invalid_input(self):
            self.assertEqual(format_date("hello"), "invalid input")

if __name__ == '__main__':
    unittest.main()