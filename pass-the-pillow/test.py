import unittest
from pass_the_pillow import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        n = 4
        time = 5
        s = Solution()
        self.assertEqual(2, s.passThePillow(n, time))

    def test_0(self):
        n = 3
        time = 2
        s = Solution()
        self.assertEqual(3, s.passThePillow(n, time))

try:
    unittest.main()
except SystemExit:
    None






