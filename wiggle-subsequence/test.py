import unittest
from wiggle_subsequence import Solution

class TestSolution(unittest.TestCase):


    def test_0(self):
        s = Solution()
        result = s.wiggleMaxLength([1,7,4,9,2,5])
        self.assertEqual(result, 6)

    def test_2(self):
        s = Solution()
        result = s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
        self.assertEqual(result, 7)

    def test_3(self):
        s = Solution()
        result = s.wiggleMaxLength([0, 0])
        self.assertEqual(result, 1)

try:
    unittest.main()
except SystemExit:
    None