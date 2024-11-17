from count_number_of_balanced_permutations import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_00(self):
        num = "46453"
        expectedResult = 6
        s = Solution()
        result = s.countBalancedPermutations(num)
        self.assertEqual(expectedResult, result)

    def test_10(self):
        num = "13"
        expectedResult = 0
        s = Solution()
        result = s.countBalancedPermutations(num)
        self.assertEqual(expectedResult, result)

    def test_09(self):
        num = "112"
        expectedResult = 1
        s = Solution()
        result = s.countBalancedPermutations(num)
        self.assertEqual(expectedResult, result)

    def test_01(self):
        num = "123"
        expectedResult = 2
        s = Solution()
        result = s.countBalancedPermutations(num)
        self.assertEqual(expectedResult, result)



    def test_03(self):
        num = "12345"
        expectedResult = 0
        s = Solution()
        result = s.countBalancedPermutations(num)
        self.assertEqual(expectedResult, result)

    def test_04(self):
        num = "13382000723440273390243968113390621505381854429237522088"
        expectedResult = 227758719
        s = Solution()
        result = s.countBalancedPermutations(num)
        self.assertEqual(expectedResult, result)

    def test_05(self):
        num = "89251972215511481873807982661331125862844105353966954144"
        expectedResult = 22596432
        s = Solution()
        result = s.countBalancedPermutations(num)
        self.assertEqual(expectedResult, result)

    def test_06(self):
        num = "162500453871196483978844245089667454919688548737112124087"
        expectedResult = 820671148
        s = Solution()
        result = s.countBalancedPermutations(num)
        self.assertEqual(expectedResult, result)

    def test_07(self):
        num = "7116572441"
        expectedResult = 14400
        s = Solution()
        result = s.countBalancedPermutations(num)
        self.assertEqual(expectedResult, result)

    def test_08(self):
        num = "13382000723440273390243968113390621505381854429237522088"
        expectedResult = 227758719
        s = Solution()
        result = s.countBalancedPermutations(num)
        self.assertEqual(expectedResult, result)

try:
    unittest.main()
except SystemExit:
    None






