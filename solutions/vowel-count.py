# Solve in one line
import unittest


def get_count(s):
    return sum(c in 'aeiou' for c in s)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_count("abracadabra"), 5)
        self.assertEqual(get_count("abcdefghi"), 3)


if __name__ == '__main__':
    unittest.main()
