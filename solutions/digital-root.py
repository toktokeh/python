import unittest


def digital_root(n):
    # while n > 10:
    #     n = sum(int(digit) for digit in str(n))
    # return n
    return n % 9 or n and 9


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root(132189), 6)
        self.assertEqual(digital_root(493193), 2)


if __name__ == '__main__':
    unittest.main()
