import unittest
from mice_and_cheese import Solution

class TestSolution(unittest.TestCase):

    def test_0(self):
        reward1 = [1,1,3,4]
        reward2 = [4,4,1,1]
        k = 2
        output = 15
        sol = Solution()
        self.assertEqual(output, sol.miceAndCheese(reward1, reward2, k))

    def test_1(self):
        reward1 = [1,1]
        reward2 =[1,1]
        k = 2
        output = 2
        sol = Solution()
        self.assertEqual(output, sol.miceAndCheese(reward1, reward2, k))






try:
    unittest.main()
except SystemExit:
    None














