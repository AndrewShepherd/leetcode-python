import unittest

from special_array_ii import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        nums = [3,4,1,2,6]
        queries = [[0,4]]
        expected_result = [False]
        result = sol.isArraySpecial(nums, queries)
        self.assertEqual(expected_result, result)

    def test_2(self):
        sol = Solution()
        nums = [4,3,1,6]
        queries = [[0,2],[2,3]]
        expected_result = [False,True]
        result = sol.isArraySpecial(nums, queries)
        self.assertEqual(expected_result, result)

    def test_3(self):
        sol = Solution()
        nums = [1]
        queries = [[0,0]]
        expected_result = [True]
        result = sol.isArraySpecial(nums, queries)
        self.assertEqual(expected_result, result)

    def test_0(self):
        sol = Solution()
        nums = [5,1,5]
        queries = [[0,1]]
        expected_result = [False]
        result = sol.isArraySpecial(nums, queries)
        self.assertEqual(expected_result, result)


try:
    unittest.main()
except SystemExit:
    None

