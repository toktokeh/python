# Solve in one line
import unittest
import string


def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_pangram("The quick, brown fox jumps over the lazy dog!"))
        self.assertFalse(is_pangram("The quick"))
        self.assertFalse(is_pangram(" "))


if __name__ == '__main__':
    unittest.main()
