import unittest

from distribute_elements import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        nums = [2,1,3,3]
        expected_result = [2,3,1,3]
        self.assertEqual(expected_result, s.resultArray(nums))

    def test_2(self):
        s = Solution()
        nums = [5,14,3,1,2]
        expected_result = [5,3,1,2,14]
        self.assertEqual(expected_result, s.resultArray(nums))

       

try:
    unittest.main()
except SystemExit:
    None











