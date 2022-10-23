import unittest

from subarrayGCD import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, nums, k, expected_result):
        sol= Solution()
        result = sol.subarrayGCD(nums, k)
        self.assertEqual(result, expected_result)


    def test_1(self):
        self.run_test(nums = [9,3,1,2,6,3], k = 3, expected_result = 4)

    def test_2(self):
        self.run_test(nums = [4], k = 7, expected_result = 0)

    def test_3(self):
        nums = list(range(1, 1000))
        self.run_test(nums, k = 1, expected_result = 0)


try:
    unittest.main()
except SystemExit:
    None











