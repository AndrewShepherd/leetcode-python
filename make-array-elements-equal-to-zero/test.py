from make_array_elements_equal_to_zero import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_00(self):
        nums = [1,0,1]
        queries = [[0,2]]
        expectedResult = True
        s = Solution()
        result = s.countValidSelections(nums, queries)
        self.assertEqual(expectedResult, result)

    def test_01(self):
        nums = [4,3,2,1]
        queries = [[1,3],[0,2]]
        expectedResult = False
        s = Solution()
        result = s.countValidSelections(nums, queries)
        self.assertEqual(expectedResult, result)

try:
    unittest.main()
except SystemExit:
    None







