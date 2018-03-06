import unittest


def lonely_integer(numbers):
    # Any number xor'd with itself will give zero.
    # Any number xor'd with zero will give the number.
    a = [int(s) for s in numbers.split(",")]
    n = 0
    for i in a:
        n ^= i
    return n


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lonely_integer("1, 1, 2"), 2)
        self.assertEqual(lonely_integer("0, 0, 1, 2, 1"), 2)


if __name__ == '__main__':
    unittest.main()
