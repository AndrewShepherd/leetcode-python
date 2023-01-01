import unittest
from distinct_prime_factors import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2,4,3,7,10,6]
        self.assertEqual(4, Solution().distinctPrimeFactors(nums))

    def test_2(self):
        nums = [2,4,8,16]
        self.assertEqual(1, Solution().distinctPrimeFactors(nums))

    def test_3(self):
        nums = list(range(2, 1001))
        self.assertEqual(168, Solution().distinctPrimeFactors(nums))


try:
    unittest.main()
except SystemExit:
    None

