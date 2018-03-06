# Solve in one line
import unittest


def accum(s):
    pass


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(accum("ZpglnRxqenU"),
                         "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
        self.assertEqual(accum("NyffsGeyylB"),
                         "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
        self.assertEqual(accum("abcd"),
                         "A-Bb-Ccc-Dddd")
        self.assertEqual(accum("RqaEzty"),
                         "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy")
        self.assertEqual(accum("cwAt"),
                         "C-Ww-Aaa-Tttt")


if __name__ == '__main__':
    unittest.main()
