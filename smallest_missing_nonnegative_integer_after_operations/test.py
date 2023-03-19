import unittest
from find_smallest_integer import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1,-10,7,13,6,8]
        value = 7
        s = Solution()
        self.assertEqual(2, s.findSmallestInteger(nums, value))

    def test_0(self):
        nums = [1,-10,7,13,6,8]
        value = 5
        s = Solution()
        self.assertEqual(4, s.findSmallestInteger(nums, value))





try:
    unittest.main()
except SystemExit:
    None











