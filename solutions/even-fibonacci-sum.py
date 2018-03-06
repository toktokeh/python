import unittest


def even_fib(num):
    a, b = 0, 1
    result = 0
    while b < num:
        if b % 2 == 0:
            result += b
        a, b = b, a + b
    return result


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_fib(1), 0)
        self.assertEqual(even_fib(0), 0)
        self.assertEqual(even_fib(10), 10)
        self.assertEqual(even_fib(5), 2)
        self.assertEqual(even_fib(33), 10)
        self.assertEqual(even_fib(25997544), 19544084)


if __name__ == '__main__':
    unittest.main()
