import unittest


def persistence(num):
    digits = [int(d) for d in str(num)]
    if len(digits) == 1:
        return 0
    p = 1
    for i in digits:
        p *= i
    return 1 + persistence(p)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(persistence(39), 3, "persistence(39) failed!")
        self.assertEqual(persistence(4), 0, "persistence(4) failed!")
        self.assertEqual(persistence(25), 2, "persistence(25) failed!")
        self.assertEqual(persistence(999), 4, "persistence(999) failed!")


if __name__ == '__main__':
    unittest.main()
