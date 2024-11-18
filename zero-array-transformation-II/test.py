from zero_array_transformation_II import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_00(self):
        nums = [1,4,2,7]
        queries = [[3,3,2],[0,1,3],[0,2,1],[0,2,2],[3,3,5],[2,3,2],[1,2,2]]
        expectedResult = 5
        s = Solution()
        result = s.minZeroArray(nums, queries)
        self.assertEqual(expectedResult, result)

    def test_07(self):
        nums = [0,10]
        queries = [[0,1,2],[0,0,2],[0,1,2],[1,1,4],[0,1,3],[1,1,4],[0,1,2],[0,1,2],[0,1,2],[0,0,2],[1,1,2],[0,0,2],[0,0,3],[1,1,3],[0,0,5]]
        expectedResult = 5
        s = Solution()
        result = s.minZeroArray(nums, queries)
        self.assertEqual(expectedResult, result)

    def test_06(self):
        nums = [6,10,0,0]
        queries = [[0,0,3],[0,2,1],[3,3,1],[1,1,4],[1,3,2],[3,3,3],[0,0,5],[0,1,5],[0,2,1],[1,1,1],[0,3,1],[0,2,4],[1,3,4],[1,2,5],[1,2,3]]
        expectedResult = 8
        s = Solution()
        result = s.minZeroArray(nums, queries)
        self.assertEqual(expectedResult, result)

    def test_05(self):
        nums = [2,0,2]
        queries = [[0,2,1],[0,2,1],[1,1,3]]
        expectedResult = 2
        s = Solution()
        result = s.minZeroArray(nums, queries)
        self.assertEqual(expectedResult, result)

    def test_01(self):
        nums = [4,3,2,1]
        queries = [[1,3,2],[0,2,1]]
        expectedResult = -1
        s = Solution()
        result = s.minZeroArray(nums, queries)
        self.assertEqual(expectedResult, result)

    def test_02(self):
        nums = [8,4]
        queries = [[0,1,5],[1,1,5],[1,1,3],[1,1,4],[0,0,3],[1,1,4],[0,1,2],[1,1,3],[1,1,1]]
        expectedResult = 5
        s = Solution()
        result = s.minZeroArray(nums, queries)
        self.assertEqual(expectedResult, result)

    def test_03(self):
        nums = [8,1]
        queries = [[1,1,3],[0,0,2],[0,1,2],[1,1,2],[0,0,2],[0,0,5],[1,1,3],[0,0,4],[1,1,5],[0,0,5],[0,0,2],[0,1,5],[0,1,2],[0,0,4],[1,1,1]]
        expectedResult = 6
        s = Solution()
        result = s.minZeroArray(nums, queries)
        self.assertEqual(expectedResult, result)

    def test_04(self):
        nums = [0,1,5]
        queries = [[2,2,5],[2,2,3],[0,2,4],[2,2,1],[2,2,1],[2,2,5],[2,2,4],[2,2,1],[2,2,2],[0,0,1],[0,1,1],[2,2,3]]
        expectedResult = 3
        s = Solution()
        result = s.minZeroArray(nums, queries)
        self.assertEqual(expectedResult, result)



try:
    unittest.main()
except SystemExit:
    None









