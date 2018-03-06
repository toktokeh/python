import unittest


def lonely_integer(numbers):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lonely_integer("1, 1, 2"), 2)
        self.assertEqual(lonely_integer("0, 0, 1, 2, 1"), 2)


if __name__ == '__main__':
    unittest.main()
