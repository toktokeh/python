# Solve in one line
import unittest


def num_jewels_in_stones(J, S):
    return sum(map(S.count, J))

    # Alternative solution:
    # return sum(S.count(j) for j in J)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(num_jewels_in_stones("z", "ZZ"), 0)
        self.assertEqual(num_jewels_in_stones("aA", "a"), 1)
        self.assertEqual(num_jewels_in_stones("aA", "aAAbbbb"), 3)


if __name__ == '__main__':
    unittest.main()
