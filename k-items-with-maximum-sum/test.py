import unittest
from k_items_with_maximum_sum import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [4,9,6,10]
        s = Solution()
        self.assertEqual(2, s.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))

    def test_2(self):
        numOnes = 3
        numZeros = 2
        numNegOnes = 0
        k = 4
        s = Solution()
        self.assertEqual(3, s.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))


try:
    unittest.main()
except SystemExit:
    None









