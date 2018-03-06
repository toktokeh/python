import unittest

# Use iterative method rather than recursive


def binary_search(nums, target):
    """
    returns index of target or false if not found
    """
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(binary_search([12, 28, 32, 45, 50], 50), 4)
        self.assertFalse(binary_search([1], 50))


if __name__ == '__main__':
    unittest.main()
