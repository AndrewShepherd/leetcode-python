import unittest
from median_of_two_sorted_arrays import Solution

class TestSolution(unittest.TestCase):

    def test_0(self):
        nums1 = [1,3]
        nums2 = [2]
        sol = Solution()
        output = sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(output, 2.0)

    def test_1(self):
        nums1 = [1,2]
        nums2 = [3,4]
        sol = Solution()
        output = sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(output, 2.5)

    def test_2(self):
        nums1 = []
        nums2 = [1]
        sol = Solution()
        output = sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(output, 1)

    def test_3(self):
        nums1 = [0,0,0,0,0]
        nums2 = [-1,0,0,0,0,0,1]
        sol = Solution()
        output = sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(output, 0)






try:
    unittest.main()
except SystemExit:
    None















