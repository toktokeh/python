import unittest


def high_and_low(numbers):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(high_and_low("4 5 29 54 4 0 -214 543 -64 1 -3 6 -6"), "543 -214")
        self.assertEqual(high_and_low("1 -1"), "1 -1")
        self.assertEqual(high_and_low("1 1"), "1 1")
        self.assertEqual(high_and_low("-1 -1"), "-1 -1")
        self.assertEqual(high_and_low("1 -1 0"), "1 -1")
        self.assertEqual(high_and_low("1 1 0"), "1 0")
        self.assertEqual(high_and_low("-1 -1 0"), "0 -1")
        self.assertEqual(high_and_low("1 -1"), "1 -1")
        self.assertEqual(high_and_low("42"), "42 42")


if __name__ == '__main__':
    unittest.main()
