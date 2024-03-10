import unittest

from distribute_elements import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()
        nums = [2,1,3]
        expected_result = [2,3,1]
        self.assertEqual(expected_result, s.resultArray(nums))

    def test_1(self):
        s = Solution()
        nums = [5,4,3,8]
        expected_result = [5,3,4,8]
        self.assertEqual(expected_result, s.resultArray(nums))


    def test_2(self):
        s = Solution()
        nums = [1,2,14,15]
        expected_result = [1,2,14,15]
        self.assertEqual(expected_result, s.resultArray(nums))

       

try:
    unittest.main()
except SystemExit:
    None









