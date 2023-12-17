import unittest

from make_smallest_array_by_swapping_elements import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        nums = [1,5,3,9,8]
        limit = 2
        result = sol.lexicographicallySmallestArray(nums, limit)
        self.assertEqual([1,3,5,8,9], result)

    def test_2(self):
        sol = Solution()
        nums = [1,7,6,18,2,1]
        limit = 3
        result = sol.lexicographicallySmallestArray(nums, limit)
        self.assertEqual([1,6,7,18,1,2], result)

    def test_3(self):
        sol = Solution()
        nums = [1,7,28,19,10]
        limit = 4
        result = sol.lexicographicallySmallestArray(nums, limit)
        self.assertEqual([1,7,28,19,10], result)

    def test_0(self):
        sol = Solution()
        nums = [1,60,34,84,62,56,39,76,49,38]
        limit = 4
        result = sol.lexicographicallySmallestArray(nums, limit)
        self.assertEqual([1,56,34,84,60,62,38,76,49,39], result)

try:
    unittest.main()
except SystemExit:
    None












