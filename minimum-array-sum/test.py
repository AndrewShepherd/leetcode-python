from minimum_array_sum import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_03(self):
        nums = [2,8,3,19,3]
        k = 3
        op1 = 1
        op2 = 1
        expectedResult = 23
        s = Solution()
        result = s.minArraySum(nums, k, op1, op2)
        self.assertEqual(expectedResult, result)

    def test_02(self):
        nums = [2,4,3]
        k = 3
        op1 = 2
        op2 = 1
        expectedResult = 3
        s = Solution()
        result = s.minArraySum(nums, k, op1, op2)
        self.assertEqual(expectedResult, result)

    def test_01(self):
        nums = [10]
        k = 0
        op1 = 0
        op2 = 1
        expectedResult = 10
        s = Solution()
        result = s.minArraySum(nums, k, op1, op2)
        self.assertEqual(expectedResult, result)

    def test_04(self):
        nums = [5]
        k = 2
        op1 = 1
        op2 = 0
        expectedResult = 3
        s = Solution()
        result = s.minArraySum(nums, k, op1, op2)
        self.assertEqual(expectedResult, result)

    def test_05(self):
        nums = [9]
        k = 5
        op1 = 1
        op2 = 1
        expectedResult = 0
        s = Solution()
        result = s.minArraySum(nums, k, op1, op2)
        self.assertEqual(expectedResult, result)

    def test_06(self):
        nums = [2,10,9,0,4]
        k = 3
        op1 = 5
        op2 = 2
        expectedResult = 7
        s = Solution()
        result = s.minArraySum(nums, k, op1, op2)
        self.assertEqual(expectedResult, result)

    def test_07(self):
        nums = [9]
        k = 6
        op1 = 0
        op2 = 1
        expectedResult = 3
        s = Solution()
        result = s.minArraySum(nums, k, op1, op2)
        self.assertEqual(expectedResult, result)

    def test_08(self):
        nums = [0,4]
        k = 3
        op1 = 1
        op2 = 1
        expectedResult = 1
        s = Solution()
        result = s.minArraySum(nums, k, op1, op2)
        self.assertEqual(expectedResult, result)

    def test_09(self):
        nums = [4,10,9,1,7]
        k = 4
        op1 = 4
        op2 = 2
        expectedResult = 9
        s = Solution()
        result = s.minArraySum(nums, k, op1, op2)
        self.assertEqual(expectedResult, result)


try:
    unittest.main()
except SystemExit:
    None











