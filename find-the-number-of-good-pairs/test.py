import unittest

from find_the_number_of_good_pairs import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        nums1 = [1,3,4]
        nums2 = [1,3,4]
        k = 1
        expected_result = 5
        result = sol.numberOfPairs(nums1, nums2, k)
        self.assertEqual(expected_result, result)

    def test_2(self):
        sol = Solution()
        nums1 = [1,2,4,12]
        nums2 = [2,4]
        k = 3
        expected_result = 2
        result = sol.numberOfPairs(nums1, nums2, k)
        self.assertEqual(expected_result, result)


try:
    unittest.main()
except SystemExit:
    None




