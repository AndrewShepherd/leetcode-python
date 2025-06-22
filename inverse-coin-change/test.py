from inverse_coin_change import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        numWays = [0,1,0,2,0,3,0,4,0,5]
        expected_result = [2,4,6]

        sol = Solution()
        result = sol.findCoins(numWays)
        self.assertEqual(expected_result, result)

    def test_2(self):
        numWays = [1,2,2,3,4]
        expected_result = [1,2,5]

        sol = Solution()
        result = sol.findCoins(numWays)
        self.assertEqual(expected_result, result)

    def test_3(self):
        numWays = [1,2,3,4,15]
        expected_result = []

        sol = Solution()
        result = sol.findCoins(numWays)
        self.assertEqual(expected_result, result)
try:
    unittest.main()
except SystemExit:
    None

