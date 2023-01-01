import unittest
from palindrome_partitioning_ii import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.minCut("ab")
        self.assertEqual(1, result)

    def test_2(self):
        s = Solution()
        result = s.minCut("aab")
        self.assertEqual(1, result)

try:
    unittest.main()
except SystemExit:
    None

