import unittest
import functions

class TestCases(unittest.TestCase):

    def test_lower(self):
        self.assertEqual('MALIK'.lower(), 'malik')

    def test_upper(self):
        self.assertEqual('lyba'.upper(), 'LYBA')

    def test_square(self):
        self.assertEqual(functions.square(7),49)

    def test_divide(self):
        self.assertEqual(functions.divide(50, 10),5)

    def test_add(self):
        self.assertEqual(functions.add(33, 2), 35)


if __name__ == '__main__':
    unittest.main()


