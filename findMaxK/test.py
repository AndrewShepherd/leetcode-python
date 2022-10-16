import unittest

from findMaxK import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, nums, expected_result):
        sol= Solution()
        result = sol.findMaxK(nums)
        self.assertEqual(result, expected_result)


    def test_1(self):
        self.run_test([-1,2,-3,3], 3)

    def test_2(self):
        self.run_test([-1,10,6,7,-7,1], 7)

    def test_0(self):
        self.run_test([-10,8,6,7,-2,-3], -1)




try:
    unittest.main()
except SystemExit:
    None








