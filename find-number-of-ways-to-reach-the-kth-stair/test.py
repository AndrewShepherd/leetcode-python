import unittest

from find_number_of_ways_to_reach_the_kth_stair import Solution


class TestSolution(unittest.TestCase):

    def test_2(self):
        sol = Solution()
        k = 0
        expected_result = 2
        result = sol.waysToReachStair(k)
        self.assertEqual(expected_result, result)

    def test_1(self):
        sol = Solution()
        k = 1
        expected_result = 4
        result = sol.waysToReachStair(k)
        self.assertEqual(expected_result, result)

    def test_0(self):
        sol = Solution()
        k = 10**9
        expected_result = 0
        result = sol.waysToReachStair(k)
        self.assertEqual(expected_result, result)



try:
    unittest.main()
except SystemExit:
    None



