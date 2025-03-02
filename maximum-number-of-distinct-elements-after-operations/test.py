from max_number_of_distinct_elements_after_operations import Solution
import unittest
import big_input

class TestSolution(unittest.TestCase):

    def test_01(self):
        nums = [1,2,2,3,3,4]
        k = 2
        expectedResult = 6
        s = Solution()
        result = s.maxDistinctElements(nums, k)
        self.assertEqual(expectedResult, result)

    def test_02(self):
        nums = [4,4,4,4] 
        k = 1
        expectedResult = 3
        s = Solution()
        result = s.maxDistinctElements(nums, k)
        self.assertEqual(expectedResult, result)

    def test_03(self):
        nums = [8,8,10,9,9]
        k = 1
        expectedResult = 5
        s = Solution()
        result = s.maxDistinctElements(nums, k)
        self.assertEqual(expectedResult, result)

    def test_04(self):
        nums = [8,7,8,7,10]
        k = 1
        expectedResult = 5
        s = Solution()
        result = s.maxDistinctElements(nums, k)
        self.assertEqual(expectedResult, result)

    def test_05(self):
        nums = [13,10,9,9,13,10,13,11]
        k = 1
        expectedResult = 7
        s = Solution()
        result = s.maxDistinctElements(nums, k)
        self.assertEqual(expectedResult, result)

    def test_06(self):
        nums = [6,7,6,6,7]
        k = 1
        expectedResult = 4
        s = Solution()
        result = s.maxDistinctElements(nums, k)
        self.assertEqual(expectedResult, result)

    def test_07(self):
        nums = big_input.nums
        k = 279204
        expectedResult = 100000
        s = Solution()
        result = s.maxDistinctElements(nums, k)
        self.assertEqual(expectedResult, result)

try:
    unittest.main()
except SystemExit:
    None












