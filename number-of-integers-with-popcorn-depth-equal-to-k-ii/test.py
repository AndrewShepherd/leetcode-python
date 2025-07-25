from number_of_integers_with_popcorn_depth_equal_to_k_ii import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [2,4]
        queries = [[1,0,1,1],[2,1,1],[1,0,1,0]]
        expected_result = [2,1]

        sol = Solution()
        result = sol.popcountDepth(nums, queries)
        self.assertEqual(expected_result, result)

    def test_2(self):
        nums = [3,5,6]
        queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]]
        expected_result = [3,1,0]

        sol = Solution()
        result = sol.popcountDepth(nums, queries)
        self.assertEqual(expected_result, result)

    def test_3(self):
        nums = [1,2]
        queries = [[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]]
        expected_result = [1,0,1]

        sol = Solution()
        result = sol.popcountDepth(nums, queries)
        self.assertEqual(expected_result, result)

    def test_4(self):
        nums = [8]
        queries = [[2,0,8],[1,0,0,2],[2,0,5],[1,0,0,4],[2,0,9],[2,0,9],[1,0,0,2],[2,0,10],[1,0,0,5],[1,0,0,0]]
        expected_result = [0, 0, 1, 0, 0]

        sol = Solution()
        result = sol.popcountDepth(nums, queries)
        self.assertEqual(expected_result, result)

    def test_5(self):
        nums = [18,19,9]
        queries = [[2,0,14],[2,2,4],[2,1,8],[1,1,1,3],[2,0,19],[1,1,1,5],[2,0,15],[2,1,7],[1,0,1,3],[1,0,0,3],[1,0,0,3],[1,1,2,1],[1,2,2,0],[2,1,15],[1,1,1,1],[2,1,3],[2,1,18],[1,0,1,2]]
        expected_result = [0,0,1,0,0,1,0,0,2]

        sol = Solution()
        result = sol.popcountDepth(nums, queries)
        self.assertEqual(expected_result, result)

try:
    unittest.main()
except SystemExit:
    None






