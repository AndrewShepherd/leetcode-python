import unittest
from closest_primes import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        left = 10
        right = 19
        self.assertEqual([11,13], Solution().closestPrimes(left, right))

    def test_2(self):
        left = 4
        right = 6
        self.assertEqual([-1,-1], Solution().closestPrimes(left, right))

    def test_3(self):
        left = 1000
        right = 1000000
        # I don't know
        self.assertEqual([1019, 1021], Solution().closestPrimes(left, right))

try:
    unittest.main()
except SystemExit:
    None



