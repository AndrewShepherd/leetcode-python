import unittest
from min_additions_to_make_valid_string import Solution

class TestSolution(unittest.TestCase):

    def test_0(self):
        word = "b"
        output = 2
        s = Solution()
        self.assertEqual(output, s.addMinimum(word))

    def test_1(self):
        word = "aaa"
        output = 6
        s = Solution()
        self.assertEqual(output, s.addMinimum(word))

    def test_2(self):
        word = "abc"
        output = 0
        s = Solution()
        self.assertEqual(output, s.addMinimum(word))





try:
    unittest.main()
except SystemExit:
    None













