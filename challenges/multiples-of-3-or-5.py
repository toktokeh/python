# Solve in one line
import unittest


def sum_of_multiples(number):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(sum_of_multiples(0), 0)
        self.assertEquals(sum_of_multiples(1), 0)
        self.assertEquals(sum_of_multiples(10), 23)
        self.assertEquals(sum_of_multiples(20), 78)
        self.assertEquals(sum_of_multiples(200), 9168)


if __name__ == '__main__':
    unittest.main()
