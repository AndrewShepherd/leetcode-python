import unittest

from find_the_integer_added_to_array_ii import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        nums1 = [4,20,16,12,8]
        nums2 = [14,18,10]
        result = sol.minimumAddedInteger(nums1, nums2)
        self.assertEqual(-2, result)

    def test_2(self):
        sol = Solution()
        nums1 = [3,5,5,3]
        nums2 = [7,7]
        result = sol.minimumAddedInteger(nums1, nums2)
        self.assertEqual(2, result)

try:
    unittest.main()
except SystemExit:
    None


















