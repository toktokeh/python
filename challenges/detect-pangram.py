# Solve in one line
import unittest


def is_pangram(s):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_pangram("The quick, brown fox jumps over the lazy dog!"))
        self.assertFalse(is_pangram("The quick"))
        self.assertFalse(is_pangram(" "))


if __name__ == '__main__':
    unittest.main()
