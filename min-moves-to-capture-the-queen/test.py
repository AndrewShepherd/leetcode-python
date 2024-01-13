import unittest

from min_moves_to_capture_the_queen import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        a = 1
        b = 1
        c = 8
        d = 8
        e = 2
        f = 3
        result = s.minMovesToCaptureTheQueen(a, b, c, d, e, f)
        self.assertEqual(2, result)

    def test_2(self):
        s = Solution()
        a = 5
        b = 3
        c = 3
        d = 4
        e = 5
        f = 2
        result = s.minMovesToCaptureTheQueen(a, b, c, d, e, f)
        self.assertEqual(1, result)

try:
    unittest.main()
except SystemExit:
    None











