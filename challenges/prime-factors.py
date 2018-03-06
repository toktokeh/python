import unittest


def prime_factors(num):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_factors(1), [])
        self.assertEqual(prime_factors(10), [2, 5])
        self.assertEqual(prime_factors(8), [2, 2, 2])


if __name__ == '__main__':
    unittest.main()
