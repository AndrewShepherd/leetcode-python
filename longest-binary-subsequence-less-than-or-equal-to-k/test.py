from longest_binary_subsequence import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.longestSubsequence("1001010", 5)
        self.assertEqual(5,result)

    def test_2(self):
        s = Solution()
        result = s.longestSubsequence("00101001", 1)
        self.assertEqual(6,result)

try:
    unittest.main()
except SystemExit:
    None