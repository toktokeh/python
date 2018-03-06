import unittest


def what_is_the_time(num):
    hour, minute = map(int, num.split(':'))
    return '{:02}:{:02}'.format(-(hour + (minute != 0)) % 12 or 12,
                                -minute % 60)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(what_is_the_time("06:35"), "05:25", "didn't work for '06:35'")
        self.assertEqual(what_is_the_time("11:59"), "12:01", "didn't work for '11:59'")
        self.assertEqual(what_is_the_time("12:02"), "11:58", "didn't work for '12:02'")
        self.assertEqual(what_is_the_time("04:00"), "08:00", "didn't work for '04:00'")
        self.assertEqual(what_is_the_time("06:00"), "06:00", "didn't work for '06:00'")
        self.assertEqual(what_is_the_time("12:00"), "12:00", "didn't work for '12:00'")


if __name__ == '__main__':
    unittest.main()
