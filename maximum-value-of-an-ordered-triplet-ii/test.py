import unittest

from maximum_triplet_value import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        nums = [12,6,1,2,7]
        result = s.maximumTripletValue(nums)
        self.assertEqual(77, result)

    def test_0(self):
        s = Solution()
        nums = [1,10,3,4,19]
        result = s.maximumTripletValue(nums)
        self.assertEqual(133, result)

    def test_3(self):
        s = Solution()
        nums = [1,2,3]
        result = s.maximumTripletValue(nums)
        self.assertEqual(0, result)

try:
    unittest.main()
except SystemExit:
    None







