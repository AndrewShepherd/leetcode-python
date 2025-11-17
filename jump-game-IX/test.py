from jump_game_ix import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [2,1,3]
        expected_result = [2,2,3]

        sol = Solution()
        result = sol.maxValue(nums)
        self.assertEqual(expected_result, result)

    def test_2(self):
        nums = [2,3,1]
        expected_result = [3,3,3]

        sol = Solution()
        result = sol.maxValue(nums)
        self.assertEqual(expected_result, result)

    def test_3(self):
        nums = [1]
        expected_result = [1]
        sol = Solution()
        result = sol.maxValue(nums)
        self.assertEqual(expected_result, result)
 
    def test_4(self):
        nums = [30,21,5,35,24]
        expected_result = [35,35,35,35,35]
        sol = Solution()
        result = sol.maxValue(nums)
        self.assertEqual(expected_result, result)

try:
    unittest.main()
except SystemExit:
    None







