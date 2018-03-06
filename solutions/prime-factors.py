import unittest


def prime_factors(num):
    result = []
    a = num
    b = 2

    while a > 1:
        if a % b == 0:
            a /= b
            result.append(int(b))
        else:
            b += 1
    return result


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_factors(1), [])
        self.assertEqual(prime_factors(10), [2, 5])
        self.assertEqual(prime_factors(8), [2, 2, 2])


if __name__ == '__main__':
    unittest.main()
