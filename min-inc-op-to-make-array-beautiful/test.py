import unittest

from test_min_operations import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        nums = [2,3,0,0,2]
        k = 4
        result = s.minIncrementOperations(nums, k)
        self.assertEqual(3, result)

    def test_2(self):
        s = Solution()
        nums = [0,1,3,3]
        k = 5
        result = s.minIncrementOperations(nums, k)
        self.assertEqual(2, result)

    def test_3(self):
        s = Solution()
        nums = [1,1,2]
        k = 1
        result = s.minIncrementOperations(nums, k)
        self.assertEqual(0, result)

try:
    unittest.main()
except SystemExit:
    None











