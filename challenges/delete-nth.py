# Solve in one line
import unittest


def delete_nth(nums, n):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(delete_nth([1, 1, 1, 1], 2), [1, 1])
        self.assertEqual(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
        self.assertEqual(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3),
                         [1, 1, 3, 3, 7, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
