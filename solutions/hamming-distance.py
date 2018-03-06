# Solve in one line
import unittest


def hamming_distance(x, y):
    return bin(x ^ y).count('1')


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hamming_distance(125, 4), 5)    # 1111101, 0000100
        self.assertEqual(hamming_distance(70, 4), 2)     # 1000110, 0000100
        self.assertEqual(hamming_distance(4, 4), 0)


if __name__ == '__main__':
    unittest.main()
