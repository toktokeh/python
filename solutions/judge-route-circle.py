# Solve in one line
import unittest


def judge_circle(moves):
    return (moves.count("L") == moves.count("R") and
            moves.count("U") == moves.count("D"))


'''
Alternative solution:
Initially, the robot is at (x, y) = (0, 0). If the move is 'U', the robot goes to (x, y-1);
if the move is 'R', the robot goes to (x, y) = (x+1, y), and so on.

def judge_circle(self, moves):
    x = y = 0
    for move in moves:
        if move == 'U': y -= 1
        elif move == 'D': y += 1
        elif move == 'L': x -= 1
        elif move == 'R': x += 1

    return x == y == 0
'''


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(judge_circle("UD"))
        self.assertFalse(judge_circle("LL"))
        self.assertTrue(judge_circle("UDLR"))
        self.assertTrue(judge_circle(""))


if __name__ == '__main__':
    unittest.main()
