import unittest


def get_middle(s):
    return s[(len(s) - 1) // 2: len(s) // 2 + 1]


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_middle("test"), 'es')
        self.assertEqual(get_middle("testing"), 't')
        self.assertEqual(get_middle("middle"), 'dd')
        self.assertEqual(get_middle("A"), 'A')
        self.assertEqual(get_middle("of"), 'of')


if __name__ == '__main__':
    unittest.main()
