import unittest

from happy_students import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        nums = [1,1]
        result = solution.countWays(nums)
        self.assertEqual(2, result)

    def test_0(self):
        solution = Solution()
        nums = [6,0,3,3,6,7,2,7]
        result = solution.countWays(nums)
        self.assertEqual(3, result)
try:
    unittest.main()
except SystemExit:
    None









