import unittest

from min_absolute_difference import Solution


class TestSolution(unittest.TestCase):

    def test_2(self):
        s = Solution()
        nums = [4,3,2,4]
        x = 2
        result = s.minAbsoluteDifference(nums, x)
        self.assertEqual(0, result)


    def test_1(self):
        s = Solution()
        nums = [5,3,2,10,15]
        x = 1
        result = s.minAbsoluteDifference(nums, x)
        self.assertEqual(1, result)

    def test_3(self):
        s = Solution()
        nums = [1,2,3,4]
        x = 3
        result = s.minAbsoluteDifference(nums, x)
        self.assertEqual(3, result)
    
       

try:
    unittest.main()
except SystemExit:
    None






