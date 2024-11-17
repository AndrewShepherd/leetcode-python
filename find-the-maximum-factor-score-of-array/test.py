import unittest

from find_the_maximum_factor_score_of_array import Solution, gcd

class TestSolution(unittest.TestCase):

    def test_2(self):
        nums = [2,4,8,16]
        sol = Solution()
        result = sol.maxScore(nums)
        self.assertEqual(result, 64)

    def test_1(self):
        nums = [1,2,3,4,5]
        sol = Solution()
        self.assertEqual(gcd(12, 5), 1)
        result = sol.maxScore(nums)
        self.assertEqual(result, 60)







try:
    unittest.main()
except SystemExit:
    None


















