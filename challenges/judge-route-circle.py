# Solve in one line
import unittest


def judge_circle(moves):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(judge_circle("UD"))
        self.assertFalse(judge_circle("LL"))
        self.assertTrue(judge_circle("UDLR"))
        self.assertTrue(judge_circle(""))


if __name__ == '__main__':
    unittest.main()
