# Solve in one line
import unittest


def spin_words(sentence):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(spin_words("Welcome"), "emocleW", "Expected 'emocleW', got '" + spin_words("Welcome") + "'")
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw", "Expected 'Hey wollef sroirraw', got '" + spin_words("Hey fellow warriors") + "'")
        self.assertEqual(spin_words("This is a test"), "This is a test", "Expected 'This is a test', got '" + spin_words("This is a test") + "'")
        self.assertEqual(spin_words("This is another test"), "This is rehtona test", "Expected 'This is rehtona test', got '" + spin_words("This is another test") + "'")


if __name__ == '__main__':
    unittest.main()
