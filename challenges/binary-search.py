import unittest

# Use iterative method rather than recursive


def binary_search(nums, target):
    """
    returns index of target or false if not found
    """
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(binary_search([12, 28, 32, 45, 50], 50), 4)
        self.assertFalse(binary_search([1], 50))


if __name__ == '__main__':
    unittest.main()
