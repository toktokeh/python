import unittest


def duplicate_encode(word):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(duplicate_encode("din"), "(((")
        self.assertEqual(duplicate_encode("recede"), "()()()")
        self.assertEqual(duplicate_encode("Success"), ")())())", "should ignore case")
        self.assertEqual(duplicate_encode("(( @"), "))((")


if __name__ == '__main__':
    unittest.main()
