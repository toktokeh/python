# Solve in one line
import unittest


def cookie(x):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cookie("Ryan"),
                         "Who ate the last cookie? It was Zach!")
        self.assertEqual(cookie(2.3),
                         "Who ate the last cookie? It was Monica!")
        self.assertEqual(cookie(26),
                         "Who ate the last cookie? It was Monica!")
        self.assertEqual(cookie(True),
                         "Who ate the last cookie? It was the dog!")


if __name__ == '__main__':
    unittest.main()
