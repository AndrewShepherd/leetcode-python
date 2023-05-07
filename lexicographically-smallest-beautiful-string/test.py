import unittest
from lexicographically_smallest_beautiful_string import Solution

class TestSolution(unittest.TestCase):

    def test_0(self):
        st = "abcz"
        k = 26
        s = Solution()
        result = s.smallestBeautifulString(st, k)
        self.assertEqual("abda", result)

    def test_1(self):
        st = "dc"
        k = 4
        s = Solution()
        result = s.smallestBeautifulString(st, k)
        self.assertEqual("", result)

try:
    unittest.main()
except SystemExit:
    None


















