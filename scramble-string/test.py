import unittest
from scramble_string import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.isScramble(s1 = "great", s2 = "rgeat")
        self.assertEqual(True, result)

    def test_2(self):
        s = Solution()
        result = s.isScramble(s1 = "abcde", s2 = "caebd")
        self.assertEqual(False, result)

    def test_3(self):
        s = Solution()
        result = s.isScramble(s1 = "a", s2 = "a")
        self.assertEqual(True, result)
try:
    unittest.main()
except SystemExit:
    None



