import unittest
from reach_end_of_array_with_max_score import Solution

class TestSolution(unittest.TestCase):

    def test_002(self):
        nums = [1,3,1,5]
        sol = Solution()
        output = sol.findMaximumScore(nums)
        self.assertEqual(output, 7)

    def test_001(self):
        nums = [4,3,1,3,2]
        sol = Solution()
        output = sol.findMaximumScore(nums)
        self.assertEqual(output, 16)











try:
    unittest.main()
except SystemExit:
    None


















