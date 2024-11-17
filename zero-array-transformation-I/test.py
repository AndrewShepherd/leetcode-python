from zero_array_transformation_I import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_00(self):
        nums = [4,3,2,1]
        queries = [[1,3],[0,2]]
        expectedResult = False
        s = Solution()
        result = s.isZeroArray(nums, queries)
        self.assertEqual(expectedResult, result)

    def test_01(self):
        nums = [1,0,1]
        queries = [[0,2]]
        expectedResult = True
        s = Solution()
        result = s.isZeroArray(nums, queries)
        self.assertEqual(expectedResult, result)

    def test_02(self):
        nums = [0,6,1,7]
        queries = [[2,3],[0,2],[0,0],[1,3],[2,2],[1,3],[0,3],[3,3],[0,0],[2,3],[2,3],[0,2],[3,3],[3,3]]
        expectedResult = False
        s = Solution()
        result = s.isZeroArray(nums, queries)
        self.assertEqual(expectedResult, result)


try:
    unittest.main()
except SystemExit:
    None








